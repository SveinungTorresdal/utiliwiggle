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
        obs.obs_data_get_string(self.settings, key)
    
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
        return self.scene
    
    @scene.setter
    def scene(self, scene_name = str):
        scene_name = obs.obs_data_get_string(self.settings, "wiggle_scene")
        scene_source = obs.obs_get_source_by_name(scene_name)
        self.scene = obs.obs_scene_from_source(scene_source)

    def start(self):
        """
        """
        self.loaded(True)
        self.timestamp = time.time()

        # set scene
        self.scene(self.get_setting("wiggle_scene"))

        # get files
        directory = self.get_setting("wiggle_path")
        filetype = self.get_setting("wiggle_reg")
        files = get_filepaths_by_extension(directory, filetype)

        self.sceneitems = [SceneItem(self.scene, Anchor.Center, file) for file in files]