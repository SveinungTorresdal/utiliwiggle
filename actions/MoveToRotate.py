import actions.MoveTo as MoveTo
import actions.Rotate as Rotate
import obspython as obs

from typing import Union


class MoveToRotate(MoveTo, Rotate):
    """
    Ostensibly, this moves AND rotates the scene item in a single action.
    """

    def __init__(self, duration: float, scene_item: object, target_pos: obs.vec2, target_rot: float):
        """
        Initializes parent actions.
        """

        MoveTo.__init__(duration, scene_item, target_pos, True)
        Rotate.__init__(duration, scene_item, target_rot, True)

    def start(self):
        """
        Start parent actions' timers and calculations.
        """

        MoveTo.start()
        Rotate.start()

    def update(self) -> bool:
        """
        Updates movement and rotation to a normalized position based on the time passed.

        @params:
        normal: float   | value between 0 and 1

        @returns whether action is completed.
        """

        normal = super().normie_time()
        MoveTo.update(normal)
        Rotate.update(normal)

        # Returns either 0 (not done) or 1 (done)
        return False if normal < 1 else True


if __name__ == "__main__":
    print('Wrong file. Run main.py.')
