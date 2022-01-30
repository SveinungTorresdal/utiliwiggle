import obspython as obs
import managers.SceneManager
import os

SceneManager = managers.SceneManager.Instance


# Called after change of settings including once after script load
def script_update(settings):
    print(obs.__file__)
    path = os.path.dirname(obs.__file__)

    wiggle_path = obs.obs_data_get_string(settings, "wiggle_path")
    wiggle_reg = obs.obs_data_get_string(settings, "wiggle_reg")
    wiggle_scene = obs.obs_data_get_string(settings, "wiggle_scene")

    SceneManager.setConfig(settings, wiggle_scene, wiggle_path, wiggle_reg)

    if SceneManager.getIsLoaded():
        SceneManager.execute()
    else:
        # We need to wait for OBS to finish loading frontend
        # Subsequent calls are fine to call SceneManager
        obs.obs_frontend_add_event_callback(event_callback)


def event_callback(event):
    if event is obs.OBS_FRONTEND_EVENT_FINISHED_LOADING:
        SceneManager.execute()


if __name__ == "__main__":
    print('Wrong file. Run main.py.')
