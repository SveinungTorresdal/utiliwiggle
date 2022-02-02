from actions.Action import Action
from typing import Union


class Wait(Action):
    """
    Action that simply... waits.
    Useful for when you, well, want to delay an action from being taken.
    """

    def __init__(self, duration: float, scene_item: object):
        """
        Initializes self and parent Action class.

        @params:
        duration: float                 | How long to wait.
        scene_item: 'obs_sceneitem_t'   | The scene item affected.
        """

        super().__init__(duration, scene_item)

    def start(self):
        """
        Starts the timer.
        """

        super().start()

    def update(self, normal: Union[float, None] = None) -> bool:
        """
        Updates based on the timer.

        @params:
        normal: float   | value between 0 and 1

        @returns whether action is completed.
        """

        normal = normal if normal is not None else super().normie_time()
        return False if normal < 1 else True


if __name__ == "__main__":
    print('Wrong file. Run main.py.')
