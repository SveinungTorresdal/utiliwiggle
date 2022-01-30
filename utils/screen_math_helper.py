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
    starting_pos: obs.vec2
    starting_rotation: float  # rotation of the objects in degree
    scene_item: object

    target_pos: obs.vec2
    target_rotation: float

    target_vector: Union[Tuple[int, int, float], None] = None

    start_time: float = 0
    end_time: float = 0

    def __init__(self, starting_pos: obs.vec2, rotation: float, scene_item,
                 target_pos: Union[obs.vec2, None] = None, target_rotation: Union[float, None] = None):
        self.starting_pos = starting_pos
        self.starting_rotation = rotation
        self.scene_item = scene_item
        self.target_pos = target_pos if target_pos is not None else self.starting_pos  # assign targets if given, otherwise assign current position
        self.target_rotation = target_rotation if target_rotation is not None else self.starting_rotation
        obs.obs_sceneitem_set_rot(self.scene_item, self.starting_rotation)
        obs.obs_sceneitem_set_pos(self.scene_item, self.starting_pos)

    def set_target(self, target_position_new: Union[obs.vec2, None] = None, target_rotation: Union[float, None] = None):
        self.target_pos = target_position_new if target_position_new is not None else self.starting_pos  # assign targets if given, otherwise assign current position
        self.target_rotation = target_rotation if target_rotation is not None else self.starting_rotation
        self.target_vector = None

    def get_distance(self) -> float:
        d_x, d_y, d_rot = self.get_target_vector()
        return sqrt(d_x ** 2 + d_y ** 2 + d_rot ** 2)

    def get_target_vector(self) -> Tuple[int, int, float]:
        if self.target_vector:
            return self.target_vector
        else:
            delta_x: int = self.target_pos.x - self.starting_pos.x
            delta_y: int = self.target_pos.y - self.starting_pos.y
            delta_rot = self.target_rotation - self.starting_rotation
            self.target_vector = (delta_x, delta_y, delta_rot)
            return self.target_vector

    def step(self, normalized_time: float):
        d_x, d_y, d_rot = self.get_target_vector()

        step_x = d_x * normalized_time
        step_y = d_y * normalized_time
        step_rot = d_rot * normalized_time

        vect2 = obs.vec2()
        obs.vec2_set(vect2, self.starting_pos.x + step_x, self.starting_pos.y + step_y)

        obs.obs_sceneitem_set_rot(self.scene_item, self.starting_rotation + step_rot)
        obs.obs_sceneitem_set_pos(self.scene_item, vect2)

    def timer_callback(self):
        if time.time() < self.end_time:
            elapsed_time = time.time() - self.start_time
            delta_t = self.end_time - self.start_time
            normalized_time = elapsed_time / delta_t
            self.step(normalized_time)
        else:
            obs.remove_current_callback()
            self.step(1)
            self.save_current_pos()

    def move_s(self, duration: int, delay: int = 0):
        current_time = time.time()
        self.end_time = current_time + duration + delay
        self.start_time = current_time + delay
        obs.timer_add(self.timer_callback, TIMER_DURATION_ms)

    def save_current_pos(self):
        self.starting_rotation = obs.obs_sceneitem_get_rot(self.scene_item)
        obs.obs_sceneitem_get_pos(self.scene_item, self.starting_pos)
