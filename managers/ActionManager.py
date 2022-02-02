from actions.Action import Action
from actions.MoveTo import MoveTo
from actions.Rotate import Rotate
from actions.Wait import Wait

import obspython as obs

class ActionManager():
    """
    Manages actions; it first executes any actions in the current queue,
    after which it executes any actions in the repeating queue whenever the queue empties.
    """

    current_action: Action
    current_queue: list
    repeating_queue: list

    def __init__(self, scene_item, offset):
        """
        Initializes ActionManager.

        @params:
        scene_item: 'obs_sceneitem_t'   | The object to animate.
        offset: int                     | Position in the SceneManager's list of scene items.
        """

        self.current_action: Action = None
        self.current_queue = list()
        self.repeating_queue = list()

        self.scene_item = scene_item

        center = MoveTo(0, scene_item, (1280+112)/2, (720+112)/2)

        offscreen_bot_right = MoveTo(0, scene_item, 1280, 720-112)
        offscreen_bot_left = MoveTo(8, scene_item, -112, 720-112)

        r1 = Rotate(0, scene_item, 180)

        offscreen_top_left = MoveTo(0, scene_item, -112, 112)
        offscreen_top_right = MoveTo(8, scene_item, 1280+112, 112)

        wait = Wait(.25, scene_item)
        wait_start = Wait(0.45*offset, scene_item)

        self.current_queue = [
            offscreen_bot_right,
            wait_start
        ]
        self.repeating_queue = [
            offscreen_bot_right,
            offscreen_bot_left,
            r1,
            wait,
            offscreen_top_left,
            offscreen_top_right,
            r1,
            wait,
        ]

    def start(self):
        """
        Sets up a callback to be rung at set interval.
        """

        obs.timer_add(self.tick, 20)

    def tick(self):
        """
        If an action is ongoing we update its progress.
        When no action is set we fetch a new one from the queue.
        If the queue is empty we refresh it with repeating actions.
        On the offchance there are no actions after that we conclude we're done and remove the callback.
        """

        # If the queue runs out of actions, but we have repeatable actions ready.
        if len(self.current_queue) == 0:
            self.current_queue.extend(self.repeating_queue)
        
        # If there were no repeatable actions we can quit.
        if len(self.current_queue) == 0:
            obs.remove_current_callback()

        # Get existing action; get and start new action of none exists
        if self.current_action is None:
            self.current_action = self.current_queue.pop(0)
            self.current_action.start()
        
        completed = self.current_action.update()

        if completed:
            # Remove current action after completion
            self.current_action = None
