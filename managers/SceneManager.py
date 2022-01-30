import obspython as obs

from managers.SourceManager import SourceManager as Source
from utils.io import get_filepaths_by_extension


class SceneManager:
    # Manages a scene and its items

    def __init__(self):
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

    def setConfig(self, settings, scene_name: str = '', directory: str = '', filetype: str = '') -> None:
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

    def setScene(self, scene=None) -> None:
        if scene is None:
            self.scene_src = obs.obs_get_source_by_name(self.scene_name)
            self.scene = obs.obs_scene_from_source(self.scene_src)
        else:
            self.scene = scene

    def setSources(self):
        self.items.clear()

        starting_x = obs.obs_source_get_width(self.scene_src)

        starting_pos = obs.vec2()
        target_pos = obs.vec2()

        for idx, filepath in enumerate(self.filepaths):
            obs.vec2_set(starting_pos, starting_x + 112, 720 - 112)
            obs.vec2_set(target_pos, -112, 720 - 112)

            newSource = Source(self.scene, filepath, starting_pos, target_pos)
            self.items.append(newSource)
            newSource.move(10)

    def getIsLoaded(self) -> bool:
        return self.loaded

    def execute(self) -> None:
        if not self.loaded:
            print('SceneManager loading.')
            self.loaded = True
            self.setScene()
            self.setSources()
            print(f'We have {len(self.items)} files to load.')

        if self.scene is None:
            return


if __name__ != "__main__":
    Instance = SceneManager()
else:
    print('Wrong file. Run main.py.')
