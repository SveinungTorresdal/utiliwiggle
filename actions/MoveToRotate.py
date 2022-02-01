import actions.MoveTo as MoveTo
import actions.Rotate as Rotate
import obspython as obs

from typing import Union


class MoveToRotate(MoveTo, Rotate):
    # Move to a given position on the screen while rotating

    def __init__(self, duration: float, scene_item: object, target_pos: obs.vec2, target_rot: float):
        MoveTo.__init__(duration, scene_item, target_pos, True)
        Rotate.__init__(duration, scene_item, target_rot, True)

    def start(self):
        MoveTo.start()
        Rotate.start()

    def update(self, normal: Union[float, None] = None) -> bool:
        normal = MoveTo.normie_time()
        MoveTo.update(normal)
        Rotate.update(normal)

        # Returns either 0 (not done) or 1 (done)
        return False if normal < 1 else True


if __name__ == "__main__":
    print('Wrong file. Run main.py.')
