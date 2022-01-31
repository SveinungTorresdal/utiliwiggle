import actions.Action as Action
import obspython as obs

from typing import Union


class MoveTo(Action):
    # Move to a given position on the screen

    starting_pos: obs.vec2
    target_pos: obs.vec2
    delta_v: obs.vec2

    def __init__(self, duration: float, scene_item: object, target_pos: obs.vec2):
        super().__init__(duration, scene_item)

        self.target_pos = target_pos

    def start(self):
        super().start()
        obs.obs_sceneitem_get_pos(self.scene_item, self.starting_pos)
        obs.vec2_sub(self.delta_v, self.target_pos, self.starting_pos)

    def update(self, normal: Union[float, None] = None) -> bool:
        normal = normal if normal is not None else super().normie_time()
        normal_v = obs.vec2
        step_v = obs.vec2
        new_pos = obs.vec2
        obs.vec2_set(normal_v, normal, normal)
        obs.vec2_mul(step_v, self.delta_v, normal_v)
        obs.vec2_add(new_pos, self.starting_pos, self.step_v)
        obs.obs_sceneitem_set_pos(self.scene_item, new_pos)

        # Returns either 0 (not done) or 1 (done)
        return bool(int(normal))
