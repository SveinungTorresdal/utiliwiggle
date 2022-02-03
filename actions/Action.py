import time


class Action:
    """
    The base class for any Actions that a scene item can perform.
    """

    scene_item: object  # 'obs_sceneitem_t'

    duration: float
    start_time: float
    end_time: float

    def __init__(self, duration: float, scene_item: object):
        """
        Initializes self.

        @params:
        duration: float                 | Time spent rotating item.
        scene_item: 'obs_sceneitem_t'   | The scene item to rotate.
        """

        self.duration = duration
        self.scene_item = scene_item

    def start(self):
        """
        Starts the timer.
        """

        self.start_time = time.time()
        self.end_time = self.start_time + self.duration

    def normie_time(self) -> float:
        """
        Converts the timer to a normalized value between 0 and 1.
        """

        current_time = time.time()
        running = current_time < self.end_time
        if running:
            elapsed = current_time - self.start_time
            normalized = elapsed / self.duration
            return normalized
        else:
            return 1


if __name__ == "__main__":
    print('Wrong file. Run main.py.')
