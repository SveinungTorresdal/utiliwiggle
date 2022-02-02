from actions.Action import Action
from actions.MoveTo import MoveTo
from actions.Rotate import Rotate
from actions.Wait import Wait

import obspython as obs

class ActionManager():
    # Manages actions

    def __init__(self, scene_item, offset):
        self.current_action: Action = None
        self.current_queue = list()
        self.repeating_queue = list()

        self.scene_item = scene_item

        center = MoveTo(0, scene_item, (1280-112)/2, (720-112)/2)

        m1 = MoveTo(0, scene_item, 1280, 720-112)
        m2 = MoveTo(8, scene_item, -112, 720-112)

        r1 = Rotate(0, scene_item, 180)

        m3 = MoveTo(0, scene_item, -112, 112)
        m4 = MoveTo(8, scene_item, 1280+112, 112)

        wait = Wait(.25, scene_item)
        wait_start = Wait(0.45*offset, scene_item)

        self.current_queue = [
            m1,
            wait_start
        ]
        self.repeating_queue = [
            m1,
            m2,
            r1,
            wait,
            m3,
            m4,
            r1,
            wait,
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
