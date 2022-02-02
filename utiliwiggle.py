from obs.description import script_description
from obs.properties import script_defaults, script_properties
from obs.lifecycle import script_update, script_tick

# This file mostly exists to setup for OBS;
# Most of the main loop is done through the OBS lifecycles, such as script_update

if __name__ == "__main__":
    print('Launched Utiliwiggle.')
