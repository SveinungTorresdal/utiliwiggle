from actions.Action import Action
import obspython as obs

from typing import Union


class MoveTo(Action):
    """
    Moves a scene item to a new position on the screen.
    """

    starting_pos: obs.vec2
    target_pos: obs.vec2
    delta_v: obs.vec2

    def __init__(self, duration: float, scene_item: object, target_x: float, target_y: float):
        """
        Initializes self and parent Action class.

        @params:
        duration: float                 | Time spent rotating item.
        scene_item: 'obs_sceneitem_t'   | The scene item to rotate.
        target_x: int                   | The target x position.
        target_y: int                   | The target y position.
        """

        super().__init__(duration, scene_item)

        self.starting_pos = obs.vec2()
        self.target_pos = obs.vec2()
        self.delta_v = obs.vec2()

        obs.vec2_set(self.target_pos, target_x, target_y)

    def start(self):
        """
        Starts the timer.
        Gets the current position and calculates the delta between itself and the target location.
        """

        super().start()
        obs.obs_sceneitem_get_pos(self.scene_item, self.starting_pos)
        obs.vec2_sub(self.delta_v, self.target_pos, self.starting_pos)

    def update(self) -> bool:
        """
        Updates movement to a normalized position based on the time passed.

        @params:
        normal: float   | value between 0 and 1

        @returns whether action is completed.
        """

        normal = super().normie_time()

        normal_v = obs.vec2()  # time between 0 and 1
        step_v = obs.vec2()  # calculated distance to move
        new_pos = obs.vec2()  # old position + new addition
        obs.vec2_set(normal_v, normal, normal)
        obs.vec2_mul(step_v, self.delta_v, normal_v)
        obs.vec2_add(new_pos, self.starting_pos, step_v)

        obs.obs_sceneitem_set_pos(self.scene_item, new_pos)

        return False if normal < 1 else True


if __name__ == "__main__":
    print('Wrong file. Run main.py.')
