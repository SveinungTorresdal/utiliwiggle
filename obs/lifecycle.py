import obspython as obs
from utils.io import get_filepaths_by_extension


# Called after change of settings including once after script load
def script_update(settings):
    global wiggle_path, wiggle_reg, wiggle_scene
    wiggle_path = obs.obs_data_get_string(settings, "wiggle_path")
    wiggle_reg = obs.obs_data_get_string(settings, "wiggle_reg")
    wiggle_scene = obs.obs_data_get_string(settings, "wiggle_scene")

    files = get_filepaths_by_extension(wiggle_path, wiggle_reg)

    print(files)


if __name__ == "__main__":
    print('Wrong file. Run main.py.')
