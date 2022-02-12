from typing import Tuple


class Transformation:
    """
    Queuable transformation.
    """
    sceneitem: object
    timestamp: float
    duration: float
    initial: dict
    transformations: dict

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

        self.initial = {}
        self.transformations = transformations

        for key, transformation in transformations.items():
            if key == 'duration':
                self.duration = transformation
            else:
                self.initial[key] = getattr(sceneitem, key)
                
                if transformation.__class__ is Tuple.__class__:
                    self.delta[key] = Tuple[transformation[0] - self.initial[key][0], transformation[1] - self.initial[key][1]]
                else:
                    self.delta[key] = transformation - self.initial[key]

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
        self._normal = (time - self.timestamp) / self.duration

    def transform(self, time: float):
        """
        Executes current transforms.
        """
        self.normal(time)

        for key, transformation in self.transformations.items():
            transform = None
            
            if transformation.__class__ is Tuple.__class__:
                self.delta[key] = Tuple[transformation[0] - self.initial[key][0], transformation[1] - self.initial[key][1]]
                transform = Tuple[self.initial[key][0] + transformation[0] * self.normal, self.initial[key][1] + transformation[1] * self.normal]
                
            else:
                self.delta[key] = transformation - self.initial[key]
                transform = self.initial[key] + transformation * self.normal

            setattr(self.sceneitem, key, transform)
        
        return False if self.normal < 1 else True
    
    def get_endtime(self) -> float:
        return self.timestamp + self.duration

    def get_transforms(self) -> dict:
        return self.transformations