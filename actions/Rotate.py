import obspython as obs

from actions.Action import Action
from typing import Union


class Rotate(Action):
    """
    Rotates a scene_item to an angle over some amount of given time.
    """

    starting_rot: Union[float, None]
    target_rot: float
    delta_rot:  Union[float, None]

    def __init__(self, duration: float, scene_item: object, target_rot: float):
        """
        Initializes self and parent Action class.

        @params:
        duration: float                 | Time spent rotating item.
        scene_item: 'obs_sceneitem_t'   | The scene item to rotate.
        target_rot: float               | The target angle desired.
        """

        super().__init__(duration, scene_item)

        self.starting_rot = None
        self.target_rot = target_rot
        self.delta_rot = None

    def start(self):
        """
        Starts the timer.
        Gets current angle of scene item and calculates a delta between it and target.
        """

        super().start()
        self.starting_rot = obs.obs_sceneitem_get_rot(self.scene_item)
        self.delta_rot = self.target_rot - self.starting_rot

    def update(self) -> bool:
        """
        Updates rotation to a normalized position based on the time passed.

        @returns whether action is completed.
        """

        normal = super().normie_time()
        step_rot: float = self.delta_rot * normal
        obs.obs_sceneitem_set_rot(self.scene_item, step_rot)

        return False if normal < 1 else True


if __name__ == "__main__":
    print('Wrong file. Run main.py.')
