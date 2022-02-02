import obspython as obs
from utils.obs import populate_list_property_with_scene_names


def script_defaults(settings):
    """
    Called after script properties are created to set default values of properties;
    the user's own selections are set afterwards.

    @params:
    settings: 'obs_data_t'
    """

    current_scene = obs.obs_frontend_get_current_scene()
    current_scene_name = obs.obs_source_get_name(current_scene)
    obs.obs_data_set_default_string(settings, "wiggle_scene", current_scene_name)
    obs.obs_data_set_default_string(settings, "wiggle_path", "")
    obs.obs_data_set_default_string(settings, "wiggle_reg", "")

def script_properties():
    """
    Called when creating the properties shown in the GUI;
    defaults are set after creating the properties.
    """

    props = obs.obs_properties_create()
    scenes_property = obs.obs_properties_add_list(props, "wiggle_scene", "Scene", obs.OBS_COMBO_TYPE_LIST, obs.OBS_COMBO_FORMAT_STRING)
    populate_list_property_with_scene_names(scenes_property)
    obs.obs_properties_add_path(props, "wiggle_path", "Folder", obs.OBS_PATH_DIRECTORY, "", "")
    obs.obs_properties_add_text(props, "wiggle_reg", "Filetype", obs.OBS_TEXT_DEFAULT)
    return props


if __name__ == "__main__":
    print('Wrong file. Run main.py.')
