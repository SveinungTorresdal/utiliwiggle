import obspython as obs
import os
import managers.ActionManager as Actions
from typing import Union, List, Tuple


class SourceManager:
    """
    Creates and manages the 'obs_source_t' and its associated data.
    """

    settings: object    # 'obs_data_t'
    scene: object       # 'obs_scene_t'
    scene_item: object  # 'obs_sceneitem_t'
    source: object      # 'obs_source_t'
    filepath: str

    def __init__(self, scene, filepath: str, index: int):
        """
        Initializes, creates and begins managing source object data.

        @params:
        scene: 'obs_scene_t'    | Scene to add source to.
        filepath: str           | Location of file on disk.
        index: int              | Position in SceneManager list.
        """

        self.settings = obs.obs_data_create()
        self.scene = scene
        self.scene_item = None
        self.source = None
        self.filepath: str = filepath

        self.createSource()

        self.Actions = Actions.ActionManager(self.scene_item, index)

    def __del__(self):
        """
        Releases a number of references during deletion.
        """

        obs.obs_sceneitem_remove(self.scene_item)
        obs.obs_sceneitem_release(self.scene_item)
        obs.obs_source_release(self.source)
        obs.obs_data_release(self.settings)

    def createSource(self):
        """
        Creates a source and adds it to the scene.
        """

        obs.obs_data_set_string(self.settings, "file", self.filepath)
        obs.obs_data_set_bool(self.settings, "unload", False)
        self.source = obs.obs_source_create_private("image_source", os.path.split(self.filepath)[1], self.settings)
        self.scene_item = obs.obs_scene_add(self.scene, self.source)
        obs.obs_sceneitem_set_alignment(self.scene_item, 0)

    def start(self):
        """
        Begins playing the source's associated actions to make it move.
        """
        
        self.Actions.start()

    def update(self, seconds):
        self.Actions.update(seconds)


if __name__ == "__main__":
    print('Wrong file. Run main.py.')
