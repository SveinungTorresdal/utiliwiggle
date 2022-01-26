import obspython as obs

from utils.io import get_filepaths_by_extension

class SceneManager:
    # Attempts to load files
    # and add them to designated scene

    def __init__(self, scene = '', source = '', filetype = ''):
        self.scene = scene
        self.source = source
        self.filetype = filetype
        pass

if __name__ == "__main__":
    print('Wrong file. Run main.py.')
