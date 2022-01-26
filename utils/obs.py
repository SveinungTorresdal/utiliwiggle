import obspython as obs


# Fills the given list property object with the names of all scenes plus an empty one
def populate_list_property_with_scene_names(list_property):
    scenes = obs.obs_frontend_get_scenes()
    obs.obs_property_list_clear(list_property)

    for scene in scenes:
        name = obs.obs_source_get_name(scene)
        obs.obs_property_list_add_string(list_property, name, name)

    obs.source_list_release(scenes)

if __name__ == "__main__":
    print('Wrong file. Run main.py.')
