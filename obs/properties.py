import obspython as obs

# Called to set default values of data settings
def script_defaults(settings):
  obs.obs_data_set_default_string(settings, "wiggle_scene", "Wiggles")
  obs.obs_data_set_default_string(settings, "wiggle_path", "")
  obs.obs_data_set_default_string(settings, "wiggle_reg", "")

# Called to display the properties GUI
def script_properties():
  props = obs.obs_properties_create()
  obs.obs_properties_add_text(props, "wiggle_scene", "Scene", obs.OBS_TEXT_DEFAULT)
  obs.obs_properties_add_path(props, "wiggle_path", "Folder", obs.OBS_PATH_DIRECTORY, "", "")
  obs.obs_properties_add_text(props, "wiggle_reg", "Regex", obs.OBS_TEXT_DEFAULT)
  return props
  
if __name__== "__main__":
    print('Wrong file. Run main.py.')