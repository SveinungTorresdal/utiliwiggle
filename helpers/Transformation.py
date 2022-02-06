from helpers.SceneItem import SceneItem

class Transformation:
    """
    Queuable transformation.
    """
    sceneitem: SceneItem
    timestamp: float
    duration: float
    initial: dict
    transformations: dict

    _normal: float

    def __init__(self, sceneitem: SceneItem, timestamp: float, duration: float, **transformations):
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
        self.duration = duration
        self._normal = 0

        for key, transformation in transformations.items():
            self.initial[key] = getattr(sceneitem, key)
            self.transformations[key] = transformation

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
        self.normal(time)

