import obspython as obs

from utils.io import get_filepaths_by_extension


class SceneManager:
    # Manages a scene and its items

    def __init__(self):
        self.settings = None
        self.scene_name = ''
        self.directory = ''
        self.filetype = ''
        self.loaded = False

    def setConfig(self, settings, scene_name='', directory='', filetype=''):
        self.settings = settings
        self.scene_name = scene_name
        self.directory = directory
        self.filetype = filetype

    def draw(self):
        if not self.loaded:
            self.loaded = True

        self.getScene()
        return

    def getIsLoaded(self):
        return self.loaded

    def getScene(self):
        wiggle_scene = obs.obs_data_get_string(self.settings, "wiggle_scene")
        scene = obs.obs_get_source_by_name(wiggle_scene)
        print(wiggle_scene)
        print(scene)


if __name__ != "__main__":
    Instance = SceneManager()
else:
    print('Wrong file. Run main.py.')
