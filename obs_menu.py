import obspython as obs

# Description displayed in the Scripts dialog window
def script_description():
  return """<h2>Wiggles!</h2>
            <p>Load the wiggle-cannon with wiggles!</p>"""

# Called to set default values of data settings
def script_defaults(settings):
  obs.obs_data_set_default_string(settings, "wiggle_path", "")
  obs.obs_data_set_default_string(settings, "wiggle_reg", "")

# Called to display the properties GUI
def script_properties():
  props = obs.obs_properties_create()
  obs.obs_properties_add_text(props, "wiggle_path", "Wiggle Folder", obs.OBS_TEXT_DEFAULT)
  obs.obs_properties_add_text(props, "wiggle_reg", "Wiggle Regex", obs.OBS_TEXT_DEFAULT)
  return props

# Called after change of settings including once after script load
def script_update(settings):
  global wiggle_path, wiggle_reg
  wiggle_path = obs.obs_data_get_string(settings, "wiggle_path")
  wiggle_reg = obs.obs_data_get_double(settings, "wiggle_reg")
