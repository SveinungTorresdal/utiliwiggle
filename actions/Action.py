import time


class Action:
    # Base class for "NPC" "actions"

    scene_item: object

    duration: float
    start_time: float
    end_time: float

    def __init__(self, duration: float, scene_item: object):
        self.duration = duration
        self.scene_item = scene_item

    def start(self) -> None:
        self.start_time = time.time()
        self.end_time = self.start_time + self.duration

    def normie_time(self) -> float:
        current_time = time.time()
        running = current_time < self.end_time
        if running:
            elapsed = current_time - self.start_time
            normalized = elapsed / self.duration
            return normalized
        else:
            return 1
