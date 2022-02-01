from actions.Action import Action

from typing import Union
class Wait(Action):
    # Just... waits some time.

    def __init__(self, duration: float, scene_item: object):
        super().__init__(duration, scene_item)
    
    def start(self):
        super().start()

    def update(self, normal: Union[float, None] = None) -> bool:
        normal = normal if normal is not None else super().normie_time()

        # This function does nothing other than wait.
        # Returns either 0 (not done) or 1 (done)
        return bool(int(normal))


if __name__ == "__main__":
    print('Wrong file. Run main.py.')
