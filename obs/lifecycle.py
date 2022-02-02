import obspython as obs
import managers.SceneManager

SceneManager = managers.SceneManager.Instance


def script_update(settings):
    """
    Called after change of settings including once after script load

    @params:
    settings: 'obs_data_t'
    """

    SceneManager.setConfig(settings)

    if SceneManager.getIsLoaded():
        SceneManager.load()
    else:
        # We need to wait for OBS to finish loading frontend
        # Subsequent calls are fine to call SceneManager
        obs.obs_frontend_add_event_callback(event_callback)


def event_callback(event):
    """
    The initial script_update occurs before the scenes and such are ready.
    As a result, we need to wait until OBS reports it's finished loading before we run SceneManager first time.
    
    @params:
    event: int | Int value represented by enum. We only really care about 'OBS_FRONTEND_EVENT_FINISHED_LOADING'
    """
    
    if event is obs.OBS_FRONTEND_EVENT_FINISHED_LOADING:
        SceneManager.load()


if __name__ == "__main__":
    print('Wrong file. Run main.py.')
