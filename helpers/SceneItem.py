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
    scene_item: object      # 'obs_sceneitem_t'

    _transformation: Transformation
    _transformations: list

    def __init__(self, scene: object, anchor: Anchor, filepath: str):
        """
        Initializes scene item from filepath.
        
        @params:
        filepath: str
        """
        self.source = None
        self.sceneitem = None

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
    
    @property
    def scale(self) -> Tuple[float, float]:
        """
        Gets the scale of the sceneitem.

        @returns Tuple[int, int] | (x, y) scale of sceneitem
        """
        vec = obs.vec2()
        obs.obs_sceneitem_get_scale(self.sceneitem, vec)
        return (vec[0], vec[1])
    
    @scale.setter
    def scale(self, scale: Tuple[float, float]):
        """
        Gets the scale of the sceneitem.

        @params:
        scale: Tuple[float, float] | New (x, y) scale of sceneitem
        """
        vec = obs.vec2()
        obs.vec2_set(vec, scale[0], scale[1])
        obs.obs_sceneitem_set_scale(self.sceneitem, scale)
