from actions.Action import Action
import obspython as obs

from typing import Union


class MoveTo(Action):
    # Move to a given position on the screen

    starting_pos: obs.vec2 = obs.vec2()
    target_pos: obs.vec2 = obs.vec2()
    delta_v: obs.vec2 = obs.vec2()

    def __init__(self, duration: float, scene_item: object, target_x: float, target_y: float):
        print(f'Called, target {target_x}, {target_y}')
        super().__init__(duration, scene_item)

        obs.vec2_set(self.target_pos, target_x, target_y)
        
    def start(self):
        print(f'New move! Going to {self.target_pos.x, self.target_pos.y}')
        super().start()
        obs.obs_sceneitem_get_pos(self.scene_item, self.starting_pos)
        obs.vec2_sub(self.delta_v, self.target_pos, self.starting_pos)

    def update(self, normal: Union[float, None] = None) -> bool:
        normal = normal if normal is not None else super().normie_time()

        normal_v = obs.vec2() # time between 0 and 1
        step_v = obs.vec2()   # calculated distance to move
        new_pos = obs.vec2()  # old position + new addition
        obs.vec2_set(normal_v, normal, normal)
        obs.vec2_mul(step_v, self.delta_v, normal_v)
        obs.vec2_add(new_pos, self.starting_pos, step_v)

        # print(f'Normal: {normal_v.x} \nDelta: {self.delta_v.x} \nStep: {step_v.x}')

        obs.obs_sceneitem_set_pos(self.scene_item, new_pos)

        # Returns either 0 (not done) or 1 (done)
        return bool(int(normal))


if __name__ == "__main__":
    print('Wrong file. Run main.py.')
