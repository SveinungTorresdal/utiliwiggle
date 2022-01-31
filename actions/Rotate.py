import actions.Action as Action
import obspython as obs

from typing import Union

class MoveTo(Action):
    # Move to a given position on the screen

    starting_rot: float
    target_rot: float
    delta_rot: float

    def __init__(self, duration: float, scene_item: object, target_rot: float):

        Action.__init__(duration, scene_item)

        self.target_rot = target_rot
        
    def start(self):
        Action.start()
        obs.obs_sceneitem_get_rot(self.scene_item, self.starting_rot)
        self.delta_rot = self.target_rot - self.starting_rot

    def update(self, normal: Union[float, None] = None) -> bool:
        normal = normal if normal is not None else Action.normie_time()
        step_rot: float = self.delta_rot * normal
        obs.obs_sceneitem_set_rot(self.scene_item, step_rot)

        # Returns either 0 (not done) or 1 (done)
        return bool(int(normal))
