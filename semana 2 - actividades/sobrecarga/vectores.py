class Vector:
    def __init__(self, x1, y1):
        self.x1 = x1
        self.y1 = y1
    def __add__(self, otro):
        x = self.x1 + otro.x1
        y = self.y1 + otro.y1
        return x, y

v1 = Vector(2,2)
v2 = Vector(3,3)
print(v1+v2)