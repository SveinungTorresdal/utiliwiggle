from typing import Tuple


class Transformation:
    """
    Queuable transformation.
    """
    sceneitem: object
    timestamp: float
    duration: float
    initial: dict
    delta: dict
    transformations: dict

    input: dict

    _normal: float

    def __init__(self, sceneitem: object, timestamp: float, **transformations):
        """
        Initializes transformation.

        @params:
        sceneitem: SceneItem    | Object to transform
        timestamp: float        | When to run
        duration: float         | How long to run
        kwarg: ...              | Remaining arguments
        """
        self.sceneitem = sceneitem
        self.timestamp = timestamp
        self._normal = 0

        self.duration = transformations['duration'] if transformations['duration'] else 0
        
        self.input = transformations
        filtered = {key:value for (key, value) in transformations.items() if key not in ['description', 'duration']}

        self.initial = {key:getattr(sceneitem, key) for (key, value) in filtered.items()}
        self.transformations = {key:value for (key, value) in filtered.items()}

        is_tuple = lambda value: value.__class__ is Tuple.__class__ or type(value) is tuple
        parse_delta = lambda target, initial: (target[0] - initial[0], target[1] - initial[1]) if is_tuple(target) else target - initial
        self.delta = {key:parse_delta(value, self.initial[key]) for (key, value) in filtered.items()}


    @property
    def normal(self) -> float:
        return self._normal

    @normal.setter
    def normal(self, time: float):
        """
        Creates value between 0 and 1 designating progress

        @params
        time: float | current time

        @returns float | normalized value between 0 and 1
        """
        if self.duration is 0:
            # if duration is zero it always completes on call;
            # avoids dividing by zero
            self._normal = 1
        else:
            self._normal = (time - self.timestamp) / self.duration

    def transform(self, time: float):
        """
        Executes current transforms.
        """
        self.normal = time

        for key, transformation in self.delta.items():
            if transformation.__class__ is Tuple.__class__ or type(transformation) is tuple:
                self.delta[key] = (transformation[0] - self.initial[key][0], transformation[1] - self.initial[key][1])
                transform = (self.initial[key][0] + transformation[0] * self.normal, self.initial[key][1] + transformation[1] * self.normal)
                setattr(self.sceneitem, key, transform)
                
            else:
                self.delta[key] = transformation - self.initial[key]
                transform = self.initial[key] + transformation * self.normal
                setattr(self.sceneitem, key, transform)

        return False if self.normal < 1 else True

    def get_endtime(self) -> float:
        return self.timestamp + self.duration

    def get_transforms(self) -> dict:
        return self.input
