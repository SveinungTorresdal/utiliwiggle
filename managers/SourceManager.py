import obspython as obs
import os

class SourceManager:
    # Manages a scene and its items

    def __init__(self, scene, filepath):
        self.settings = obs.obs_data_create()
        self.scene = scene
        self.source = None
        self.filepath = filepath
        self.createSource()

        self.position = obs.vec2()

    def __del__ (self):
        obs.obs_data_release(self.settings)
        obs.obs_source_release(self.source)

    def createSource (self):
        obs.obs_data_set_string(self.settings, "file", self.filepath)
        obs.obs_data_set_bool(self.settings, "unload", False)
        self.source = obs.obs_source_create_private("image_source", os.path.split(self.filepath)[1], self.settings)
        scene = obs.obs_scene_from_source(self.scene)
        obs.obs_scene_add(scene, self.source)

if __name__ == "__main__":
    print('Wrong file. Run main.py.')
