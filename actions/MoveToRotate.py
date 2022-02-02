from actions.Action import Action
import obspython as obs

from typing import Union


class MoveToRotate(Action):
    """
    Ostensibly, this moves AND rotates the scene item in a single action.
    """

    starting_pos: obs.vec2
    target_pos: obs.vec2
    delta_v: obs.vec2

    starting_rot: float
    target_rot: float
    delta_rot: float

    def __init__(self, duration: float, scene_item: object, target_x: float, target_y: float, target_rot: float):
        """
        Initializes parent actions.

        @params:
        duration: float                 | Time spent rotating item.
        scene_item: 'obs_sceneitem_t'   | The scene item to rotate.
        target_x: int                   | The target x position.
        target_y: int                   | The target y position.
        target_rot: float               | The target angle desired.
        """

        super().__init__(duration, scene_item)

        self.starting_pos = obs.vec2()
        self.target_pos = obs.vec2()
        self.delta_v = obs.vec2()

        obs.vec2_set(self.target_pos, target_x, target_y)

        self.starting_rot = None
        self.target_rot = target_rot
        self.delta_rot = None

    def start(self):
        """
        Start parent actions' timers and calculations.
        """

        super().start()
        obs.obs_sceneitem_get_pos(self.scene_item, self.starting_pos)
        obs.vec2_sub(self.delta_v, self.target_pos, self.starting_pos)
        self.starting_rot = obs.obs_sceneitem_get_rot(self.scene_item)
        self.delta_rot = self.target_rot - self.starting_rot

    def update(self, normal: Union[float, None] = None) -> bool:
        """
        Updates movement and rotation to a normalized position based on the time passed.

        @params:
        normal: float   | value between 0 and 1

        @returns whether action is completed.
        """

        normal = normal if normal is not None else super().normie_time()

        # Move object
        normal_v = obs.vec2()  # time between 0 and 1
        step_v = obs.vec2()  # calculated distance to move
        new_pos = obs.vec2()  # old position + new addition
        obs.vec2_set(normal_v, normal, normal)
        obs.vec2_mul(step_v, self.delta_v, normal_v)
        obs.vec2_add(new_pos, self.starting_pos, step_v)

        obs.obs_sceneitem_set_pos(self.scene_item, new_pos)

        # Rotate object
        step_rot: float = self.delta_rot * normal
        obs.obs_sceneitem_set_rot(self.scene_item, step_rot)

        return False if normal < 1 else True


if __name__ == "__main__":
    print('Wrong file. Run main.py.')
