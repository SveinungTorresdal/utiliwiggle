import time
import obspython as obs

from helpers.Anchor import Anchor
from helpers.SceneItem import SceneItem
from utils.io import get_filepaths_by_extension

class Scene:
    """
    Python representation of an OBS scene (obs_scene_t).
    """
    _loaded: bool = False
    _settings: object
    _scene: object
    sceneitems: list
    timestamp: float

    def get_setting(self, key: str) -> str:
        return obs.obs_data_get_string(self._settings, key)
    
    def set_settings(self, settings: object):
        self._settings = settings

    @property
    def loaded(self) -> bool:
        return self._loaded
    
    @loaded.setter
    def loaded(self, truth: bool):
        self._loaded = truth

    @property
    def scene(self) -> object: 
        return self._scene
    
    @scene.setter
    def scene(self, scene_name: str = ''):
        scene_source = obs.obs_get_source_by_name(scene_name)
        self._scene = obs.obs_scene_from_source(scene_source)

    def start(self):
        """
        Loads files, creates scene items
        """
        self.timestamp = time.time()

        # set scene
        self.scene = self.get_setting("wiggle_scene")

        # get files
        directory = self.get_setting("wiggle_path")
        filetype = self.get_setting("wiggle_reg")
        files = get_filepaths_by_extension(directory, filetype)

        transforms = [
            {
                'duration': 0,
                'position': (1280+56, 720-56),
                'rotation': 360,
                'scale': (1, 1)
            },
            {
                'duration': 10,
                'position': (1280/2, 720/2),
                'rotation': 360,
                'scale': (1.5, 1.5)
            }
        ]

        self.sceneitems = [SceneItem(self.scene, Anchor.Center, transforms, file) for file in files]

        self.loaded = True

        current = time.time()
        [sceneitem.transform(current) for sceneitem in self.sceneitems]

    def tick(self):
        if self.loaded is not True:
            return
        
        #current = time.time()
        #[sceneitem.transform(current) for sceneitem in self.sceneitems]
