"""
Utility functions and classes to help create layouts
"""
from math import sqrt
from typing import Union, List, Tuple


class Slot:
    """container class to wrap an OBS Object (e.g. image) with on-screen coordinates and rotation"""
    x_coord: int  # the X coordinate of the object in pixel
    y_coord: int  # the Y coordinate of the object in pixel
    rotation: int  # rotation of the objects in degree
    image_object: object

    target_x: int
    target_y: int
    target_rotation: int

    target_vector: Union[Tuple[int, int, int], None] = None

    def __init__(self, x_coord: int, y_coord: int, rotation: int, image_object,
                 target_x: Union[int, None] = None, target_y: Union[int, None] = None, target_rotation: Union[int, None] = None):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.rotation = rotation
        self.image_object = image_object
        self.target_x = target_x if target_x is not None else self.x_coord  # assign targets if given, otherwise assign current position
        self.target_y = target_y if target_y is not None else self.y_coord
        self.target_rotation = target_rotation if target_rotation is not None else self.rotation

    def set_target(self, target_x: Union[int, None] = None, target_y: Union[int, None] = None, target_rotation: Union[int, None] = None):
        self.target_x = target_x if target_x is not None else self.x_coord  # assign targets if given, otherwise assign current position
        self.target_y = target_y if target_y is not None else self.y_coord
        self.target_rotation = target_rotation if target_rotation is not None else self.rotation

    def get_distance(self) -> float:
        d_x, d_y, d_rot = self.get_target_vector()
        return sqrt(d_x**2 + d_y**2 + d_rot**2)

    def get_target_vector(self) -> Tuple[int, int, int]:
        if self.target_vector:
            return self.target_vector
        else:
            delta_x = self.target_x-self.x_coord
            delta_y = self.target_y-self.y_coord
            delta_rot = self.target_rotation-self.rotation
            self.target_vector = (delta_x, delta_y, delta_rot)
            return self.target_vector

