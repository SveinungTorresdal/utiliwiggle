import obspython as obs
import os

class SourceManager:
    # Manages a scene and its items

    def __init__(self, scene, filepath):
        self.settings = obs.obs_data_create()
        self.scene = scene
        self.scene_item = None
        self.source = None
        self.filepath = filepath
        self.createSource()

        self.position = obs.vec2()

    def __del__ (self):
        obs.obs_sceneitem_remove(self.scene_item)
        obs.obs_sceneitem_release(self.scene_item)
        obs.obs_source_release(self.source)
        obs.obs_data_release(self.settings)

    def createSource (self):
        self.settings = obs.obs_data_create()

        obs.obs_data_set_string(self.settings, "file", self.filepath)
        obs.obs_data_set_bool(self.settings, "unload", False)
        self.source = obs.obs_source_create_private("image_source", os.path.split(self.filepath)[1], self.settings)
        scene = obs.obs_scene_from_source(self.scene)
        self.scene_item = obs.obs_scene_add(scene, self.source)

if __name__ == "__main__":
    print('Wrong file. Run main.py.')
