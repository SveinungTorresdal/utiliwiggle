from actions.MoveTo import MoveTo
from actions.Rotate import Rotate
from actions.Wait import Wait

import obspython as obs

class ActionManager():
    # Manages actions

    scene_item = None

    current_action = None
    current_queue = list()
    repeating_queue = list()

    def __init__(self, scene_item, offset):
        self.scene_item = scene_item

        m1 = MoveTo(0, scene_item, 1280, 720-112)
        m2 = MoveTo(2, scene_item, -112, 720-112)

        self.current_queue = [
        ]
        self.repeating_queue = [
            m1, m2
        ]

    def start(self):
        obs.timer_add(self.manage_actions, 20)

    def manage_actions(self):
        # If the queue runs out of actions, but we have repeatable actions ready.
        if len(self.current_queue) == 0:
            self.current_queue.extend(self.repeating_queue)
        
        # If there were no repeatable actions we can quit.
        if len(self.current_queue) == 0:
            obs.remove_current_callback()

        # Get existing action; get and start new action of none exists
        if self.current_action is None:
            print('Set new action')
            self.current_action = self.current_queue.pop(0)
            self.current_action.start()
        
        completed = self.current_action.update()

        if completed:
            # Remove current action after completion
            self.current_action = None