import obspython as obs

from managers.SourceManager import SourceManager as Source
from utils.io import get_filepaths_by_extension


class SceneManager:
    """
    Manages a scene and its items
    """

    # Basic configuration
    settings: object    # 'obs_data_t'
    scene_name: str
    directory: str
    filetype: str
    loaded: bool

    # Dynamically updated configuration
    scene_src: object   # 'obs_source_t'
    scene: object       # 'obs_scene_t'
    items: list

    def __init__(self):
        """
        Simple init to set basic variables, because SceneManager is instantiated before it can be used.
        """

        # Basic conf set via setConfig
        self.settings = None
        self.scene_name = ''
        self.directory = ''
        self.filetype = ''

        # "Loaded" checkflag to verify we're allowed to get scenes and sources.
        self.loaded = False

        # Filepaths
        self.filepaths = []

        # Scene source, scene item sources
        self.scene_src = None
        self.scene = None
        self.items = []

    def setConfig(self, settings):
        """
        Updates the config when script_update is called.

        @params:
        settings: 'obs_data_t'  | Object containing settings from OBS.
        """

        directory = obs.obs_data_get_string(settings, "wiggle_path")
        filetype = obs.obs_data_get_string(settings, "wiggle_reg")
        scene_name = obs.obs_data_get_string(settings, "wiggle_scene")

        self.settings = settings

        changed = False

        if self.scene_name != scene_name:
            self.scene_name = scene_name
            changed = True

        if self.directory != directory:
            self.directory = directory
            changed = True

        if self.filetype != filetype:
            self.filetype = filetype
            changed = True

        if changed:
            self.setScene()
            self.filepaths = get_filepaths_by_extension(directory, filetype)

            if self.loaded:
                self.setSources()

    def setScene(self):
        """
        Finds the scene's source object (obs_source_t) by name, and the separate scene object (obs_scene_t) from the source.
        """

        self.scene_src = obs.obs_get_source_by_name(self.scene_name)
        self.scene = obs.obs_scene_from_source(self.scene_src)

    def setSources(self):
        """
        Takes the filepaths we've received and creates a list of source objects with them, then begins letting them animate.
        Removes existing sources when called.
        """

        self.items.clear()

        for idx, filepath in enumerate(self.filepaths):
            newSource = Source(self.scene, filepath, idx)
            self.items.append(newSource)

        for idx, source in enumerate(self.items):
            source.start()

    def getIsLoaded(self) -> bool:
        """
        OBS calls script_update before the sources, and thus scenes, are even created.
        So we need to wait for the actual loading of OBS to finish before trying to execute the SceneManager's functionality.
        This function is used to block calls to this object until OBS has finished loading.
        """

        return self.loaded

    def load(self):
        """
        Loads the SceneManager - which in turn sets the scene and loads all the scene assets.
        """

        if not self.loaded:
            print('SceneManager loading.')
            self.loaded = True
            self.setScene()
            self.setSources()
            print(f'We have {len(self.items)} files to load.')

    def tick(self, seconds):
        for source in self.items:
            source.update(seconds)

if __name__ != "__main__":
    Instance = SceneManager()
else:
    print('Wrong file. Run main.py.')
