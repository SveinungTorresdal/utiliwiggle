from actions.Action import Action
from actions.MoveTo import MoveTo
from actions.MoveToRotate import MoveToRotate
from actions.Rotate import Rotate
from actions.Wait import Wait

import obspython as obs


class ActionManager:
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

        duration = 5

        width = 1280+56
        space = width/14
        time = space/width*duration

        wait_spawn = Wait(1+(time*offset), scene_item)
        spawn_pos = MoveTo(0, scene_item, 1280+56, 720-56)
        bot_left = MoveTo(duration, scene_item, -56, 720-56)

        self.current_queue = [
            spawn_pos,
            wait_spawn,
        ]
        self.repeating_queue = [
            bot_left,
            spawn_pos
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
