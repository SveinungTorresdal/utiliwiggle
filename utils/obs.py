import obspython as obs


# Returns a list of sources
def get_source_names():
    sources = obs.obs_enum_sources()
    names = [obs.obs_source_get_name(source) for source in sources]
    obs.source_list_release(sources)

    return names


# Returns a list of names of all existing scenes
def get_scene_names():
    scenes = obs.obs_frontend_get_scenes()
    names = [obs.obs_source_get_name(scene) for scene in scenes]
    obs.source_list_release(scenes)

    return names


# Fills the given list property with the existing scene names
def populate_list_property_with_scene_names(list_property):
    scenes = get_scene_names()

    obs.obs_property_list_clear(list_property)

    obs.obs_property_list_add_string(list_property, '', '')
    
    for scene in scenes:
        obs.obs_property_list_add_string(list_property, scene, scene)

if __name__ == "__main__":
    print('Wrong file. Run main.py.')
