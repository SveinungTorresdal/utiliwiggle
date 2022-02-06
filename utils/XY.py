class XY:
    """
    Helper for adding, subtracting, multiplying and dividing an (X,Y).
    """

    x: float
    y: float

    def __init__(self, *items):
        if len(items) == 1:
            self.x, self.y = items[0]
        elif len(items) == 2:
            self.x = items[0]
            self.y = items[1]

    def __add__(self, other):
        if other.__class__ is XY:
            self.x += other.x
            self.y += other.y

        elif other.__class__ in [float, int]:
            self.x += other
            self.y += other
        
        return self
    
    def __sub__(self, other):
        if other.__class__ is XY:
            self.x -= other.x
            self.y -= other.y

        elif other.__class__ in [float, int]:
            self.x -= other
            self.y -= other
        
        return self
    
    def __mul__(self, other):
        if other.__class__ is XY:
            self.x *= other.x
            self.y *= other.y

        elif other.__class__ in [float, int]:
            self.x *= other
            self.y *= other
        
        return self
    
    def __truediv__(self, other):
        if other.__class__ is XY:
            self.x /= other.x
            self.y /= other.y

        elif other.__class__ in [float, int]:
            self.x /= other
            self.y /= other
        
        return self