import actions.Action as Action

class Wait(Action):
    # Just... waits some time.

    def update(self) -> bool:
        # This function does nothing other than wait.
        # Returns either 0 (not done) or 1 (done)
        return int(Action.update())