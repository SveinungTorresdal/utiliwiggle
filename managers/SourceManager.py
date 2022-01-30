import obspython as obs
import os
import utils.screen_math_helper as pixel
from typing import Union, List, Tuple

class SourceManager:
    # Manages a scene and its items

    def __init__(self, scene, filepath, starting_pos, target_pos: Union[obs.vec2, None] = None):
        self.settings = obs.obs_data_create()
        self.scene = scene
        self.scene_item = None
        self.source = None
        self.filepath: str = filepath

        self.createSource()
        
        self.slot = pixel.Slot(starting_pos, 0, self.scene_item, target_pos)

    def __del__ (self):
        obs.obs_sceneitem_remove(self.scene_item)
        obs.obs_sceneitem_release(self.scene_item)
        obs.obs_source_release(self.source)
        obs.obs_data_release(self.settings)

    def createSource (self):
        obs.obs_data_set_string(self.settings, "file", self.filepath)
        obs.obs_data_set_bool(self.settings, "unload", False)
        self.source = obs.obs_source_create_private("image_source", os.path.split(self.filepath)[1], self.settings)
        self.scene_item = obs.obs_scene_add(self.scene, self.source)

    def move(self, duration: int):
        self.slot.move_s(duration)

if __name__ == "__main__":
    print('Wrong file. Run main.py.')
