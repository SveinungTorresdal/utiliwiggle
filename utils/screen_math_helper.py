"""
Utility functions and classes to help create layouts
"""
import time
from math import sqrt
from typing import Union, List, Tuple
import obspython as obs


TIMER_DURATION_ms = 10


class Slot:
    """container class to wrap an OBS Object (e.g. image) with on-screen coordinates and rotation"""
    x_origin: int  # the X coordinate of the object in pixel
    y_origin: int  # the Y coordinate of the object in pixel
    rot_origin: int  # rotation of the objects in degree
    image_object: object

    target_x: int
    target_y: int
    target_rotation: int

    target_vector: Union[Tuple[int, int, int], None] = None

    start_time: int = 0
    end_time: int = 0

    def __init__(self, x_coord: int, y_coord: int, rotation: int, image_object,
                 target_x: Union[int, None] = None, target_y: Union[int, None] = None, target_rotation: Union[int, None] = None):
        self.x_origin = x_coord
        self.y_origin = y_coord
        self.rot_origin = rotation
        self.image_object = image_object
        self.target_x = target_x if target_x is not None else self.x_origin  # assign targets if given, otherwise assign current position
        self.target_y = target_y if target_y is not None else self.y_origin
        self.target_rotation = target_rotation if target_rotation is not None else self.rot_origin
        obs.obs_sceneitem_set_rot(self.image_object, self.rot_origin)
        obs.obs_sceneitem_set_pos(self.image_object, (self.x_origin, self.y_origin))

    def set_target(self, target_x: Union[int, None] = None, target_y: Union[int, None] = None, target_rotation: Union[int, None] = None):
        self.target_x = target_x if target_x is not None else self.x_origin  # assign targets if given, otherwise assign current position
        self.target_y = target_y if target_y is not None else self.y_origin
        self.target_rotation = target_rotation if target_rotation is not None else self.rot_origin

    def get_distance(self) -> float:
        d_x, d_y, d_rot = self.get_target_vector()
        return sqrt(d_x ** 2 + d_y ** 2 + d_rot ** 2)

    def get_target_vector(self) -> Tuple[int, int, int]:
        if self.target_vector:
            return self.target_vector
        else:
            delta_x = self.target_x - self.x_origin
            delta_y = self.target_y - self.y_origin
            delta_rot = self.target_rotation - self.rot_origin
            self.target_vector = (delta_x, delta_y, delta_rot)
            return self.target_vector

    def step(self, normalized_time: float):
        d_x, d_y, d_rot = self.get_target_vector()
        step_x = d_x * normalized_time
        step_y = d_y * normalized_time
        step_rot = d_rot * normalized_time
        obs.obs_sceneitem_set_rot(self.image_object, self.rot_origin + step_rot)
        obs.obs_sceneitem_set_pos(self.image_object, (self.x_origin + step_x, self.y_origin + step_y))

    def timer_callback(self):
        if time.time_ns() < self.end_time:
            elapsed_time_ns = time.time_ns() - self.start_time
            delta_t_ns = self.end_time - self.start_time
            normalized_time = elapsed_time_ns / delta_t_ns
            self.step(normalized_time)
        else:
            obs.remove_current_callback()
            self.step(1)
            self.save_current_pos()

    def move_s(self, duration: int):
        current_time = time.time_ns()
        self.end_time = current_time + duration * 1000000
        self.start_time = current_time
        obs.timer_add(self.timer_callback, TIMER_DURATION_ms)

    def save_current_pos(self):
        self.rot_origin = obs.obs_sceneitem_get_rot(self.image_object)
        self.x_origin, self.y_origin = obs.obs_sceneitem_get_pos(self.image_object)
