import obspython as obs
import os
import managers.ActionManager as Actions
from typing import Union, List, Tuple


class SourceManager:
    # Manages a scene and its items

    settings: object    # 'obs_data_t'
    scene: object       # 'obs_scene_t'
    scene_item: object  # 'obs_sceneitem_t'
    source: object      # 'obs_source_t'
    filepath: str

    def __init__(self, scene, filepath, index: int):
        self.settings = obs.obs_data_create()
        self.scene = scene
        self.scene_item = None
        self.source = None
        self.filepath: str = filepath

        self.createSource()

        self.Actions = Actions.ActionManager(self.scene_item, index)

    def __del__(self):
        obs.obs_sceneitem_remove(self.scene_item)
        obs.obs_sceneitem_release(self.scene_item)
        obs.obs_source_release(self.source)
        obs.obs_data_release(self.settings)

    def createSource(self):
        obs.obs_data_set_string(self.settings, "file", self.filepath)
        obs.obs_data_set_bool(self.settings, "unload", False)
        self.source = obs.obs_source_create_private("image_source", os.path.split(self.filepath)[1], self.settings)
        self.scene_item = obs.obs_scene_add(self.scene, self.source)

    def move(self):
        self.Actions.start()


if __name__ == "__main__":
    print('Wrong file. Run main.py.')
