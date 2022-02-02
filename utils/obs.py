import obspython as obs


def get_source_names():
    """
    Returns a list of input sources by name.

    @returns list | List containing names of input sources.
    """

    sources = obs.obs_enum_sources()
    names = [obs.obs_source_get_name(source) for source in sources]
    obs.source_list_release(sources)

    return names


def get_scene_names():
    """
    Returns a list of names of all existing scenes

    @returns list | List containing all scenes by name.
    """

    scenes = obs.obs_frontend_get_scenes()
    names = [obs.obs_source_get_name(scene) for scene in scenes]
    obs.source_list_release(scenes)

    return names


# Fills the given list property with the existing scene names
def populate_list_property_with_scene_names(list_property):
    """
    Adds scenes to a given list dropdown property.

    @params:
    list_property: 'obs_property_t' | List property to add scenes to.
    """

    scenes = get_scene_names()

    obs.obs_property_list_clear(list_property)

    obs.obs_property_list_add_string(list_property, '', '')
    
    for scene in scenes:
        obs.obs_property_list_add_string(list_property, scene, scene)


if __name__ == "__main__":
    print('Wrong file. Run main.py.')
