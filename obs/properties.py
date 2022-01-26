import obspython as obs
from utils.obs import populate_list_property_with_scene_names

# Called to set default values of data settings
def script_defaults(settings):
    obs.obs_data_set_default_string(settings, "wiggle_path", "")
    obs.obs_data_set_default_string(settings, "wiggle_reg", "")


# Called to display the properties GUI
def script_properties():
    props = obs.obs_properties_create()
    scenes_property = obs.obs_properties_add_list(props, "wiggle_scene", "Scene",
              obs.OBS_COMBO_TYPE_LIST, obs.OBS_COMBO_FORMAT_STRING)
    populate_list_property_with_scene_names(scenes_property)
    obs.obs_properties_add_path(props, "wiggle_path", "Folder", obs.OBS_PATH_DIRECTORY, "", "")
    obs.obs_properties_add_text(props, "wiggle_reg", "Filetype", obs.OBS_TEXT_DEFAULT)
    return props


if __name__ == "__main__":
    print('Wrong file. Run main.py.')
