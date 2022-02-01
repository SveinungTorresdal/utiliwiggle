from actions.Action import Action

class Wait(Action):
    # Just... waits some time.

    def __init__(self, duration: float, scene_item: object):
        super().__init__(duration, scene_item)
    
    def start(self):
        super().start()

    def update(self) -> bool:
        # This function does nothing other than wait.
        # Returns either 0 (not done) or 1 (done)
        return int(Action.normie_time())


if __name__ == "__main__":
    print('Wrong file. Run main.py.')
