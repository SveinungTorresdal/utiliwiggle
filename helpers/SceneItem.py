from typing import Tuple
import obspython as obs
import os

from helpers.Anchor import Anchor
from helpers.Transformation import Transformation

class SceneItem:
    """
    Python representation of an OBS sceneitem (obs_sceneitem_t).
    """
    source: object          # 'obs_source_t'
    sceneitem: object      # 'obs_sceneitem_t'

    transformations: list
    transformation: Transformation

    def __init__(self, scene: object, anchor: Anchor, transformations: list, filepath: str):
        """
        Initializes scene item from filepath.
        
        @params:
        filepath: str
        """
        self.source = None
        self.sceneitem = None
        
        self.transformations = transformations
        self.transformation = None

        settings = obs.obs_data_create()

        obs.obs_data_set_string(settings, "file", filepath)
        obs.obs_data_set_bool(settings, "unload", False)

        self.source = obs.obs_source_create_private("image_source", os.path.split(filepath)[1], settings)
        obs.obs_data_release(settings)

        self.sceneitem = obs.obs_scene_add(scene, self.source)
        obs.obs_sceneitem_set_alignment(self.sceneitem, anchor)
    
    def __del__(self):
        """
        Removes from scene, releases the references to scene item and source.
        """
        obs.obs_sceneitem_remove(self.sceneitem)
        obs.obs_sceneitem_release(self.sceneitem)
        obs.obs_source_release(self.source)

    """
    Gets or sets the anchor point of sceneitem
    """
    @property
    def anchor(self) -> Anchor:
        """
        Gets current anchor point of sceneitem.

        @returns Anchor | Anchor point of sceneitem; enum value representing int
        """
        return Anchor(obs.obs_sceneitem_get_alignment(self.sceneitem))
    
    @anchor.setter
    def anchor(self, anchor: Anchor):
        """
        Sets new anchor point of sceneitem.

        @params:
        anchor: Anchor | Desired anchor point; enum value representing int
        """
        obs.obs_sceneitem_set_alignment(self.sceneitem, anchor)

    """
    Gets or sets the position of sceneitem
    """
    @property
    def position(self) -> Tuple[float, float]:
        """
        Gets the position of the sceneitem.

        @returns Tuple[int, int] | (x,y) values of position
        """
        pos = obs.vec2()
        obs.obs_sceneitem_get_pos(self.sceneitem, pos)
        return (pos.x, pos.y)

    @position.setter
    def position(self, position: Tuple[float, float]):
        """
        Sets the new position of the sceneitem.

        @params
        position: Tuple[int, int] | New (x,y) values of position
        """
        vec = obs.vec2()
        obs.vec2_set(vec, position[0], position[1])
        obs.obs_sceneitem_set_pos(self.sceneitem, vec)
    
    """
    Gets or sets the rotation of sceneitem
    """
    @property
    def rotation(self) -> float:
        """
        Gets the angle of the sceneitem.

        @returns float | Angle of sceneitem
        """
        return obs.obs_sceneitem_get_rot(self.sceneitem)
    
    @rotation.setter
    def rotation(self, angle: float):
        """
        Sets the new angle of the sceneitem.

        @params 
        angle: float | New angle of sceneitem
        """
        obs.obs_sceneitem_set_rot(self.sceneitem, angle)
    
    """
    Gets or sets the scale of sceneitem
    """
    @property
    def scale(self) -> Tuple[float, float]:
        """
        Gets the scale of the sceneitem.

        @returns Tuple[int, int] | (x, y) scale of sceneitem
        """
        vec = obs.vec2()
        obs.obs_sceneitem_get_scale(self.sceneitem, vec)
        return (vec.x, vec.y)

    @scale.setter
    def scale(self, scale: Tuple[float, float]):
        """
        Gets the scale of the sceneitem.

        @params:
        scale: Tuple[float, float] | New (x, y) scale of sceneitem
        """
        vec = obs.vec2()
        obs.vec2_set(vec, scale[0], scale[1])
        obs.obs_sceneitem_set_scale(self.sceneitem, vec)

    """
    Run transformation
    """
    def transform(self, time: float):
        print(len(self.transformations))

        if self.transformation is None and len(self.transformations) > 0:
            init_transforms = self.transformations.pop(0)
            self.transformation = Transformation(self, time, **init_transforms)
        
        complete = self.transformation.transform(time)

        if complete:
            start_time = self.transformation.get_endtime()
            transforms = self.transformation.get_transforms()
            self.transformations.append(transforms)
            new_transforms = self.transformations.pop(0)
            self.transformation = Transformation(self, start_time, **new_transforms)
        
