import math
import matplotlib.pyplot as plt


class Vector:
    def __init__(self, x, y=None, z=None):
        if y is None and z is None:
            self.components = x
        else:
            self.components = [x, y, z]

    def __add__(self, other):
        return Vector([a + b for a, b in zip(self.components, other.components)])

    def __sub__(self, other):
        return Vector([a - b for a, b in zip(self.components, other.components)])

    def __mul__(self, scalar):
        return Vector([c * scalar for c in self.components])

    def __truediv__(self, scalar):
        return Vector([c / scalar for c in self.components])

    def dot(self, other):
        return sum(a * b for a, b in zip(self.components, other.components))

    def angle(self, other, degrees=False):
        dot_product = self.dot(other)
        mag_product = self.magnitude() * other.magnitude()
        angle = math.acos(dot_product / mag_product)
        if degrees:
            angle = math.degrees(angle)
        return angle

    def magnitude(self):
        return math.sqrt(sum(c**2 for c in self.components))

    def distance(self, other):
        return (self - other).magnitude()

    def visualize(self):
        if len(self.components) == 2:
            plt.quiver(0, 0, self.components[0], self.components[1],
                       angles='xy', scale_units='xy', scale=1, color='blue')
            plt.xlim(-5, 5)
            plt.ylim(-5, 5)
            plt.show()
        elif len(self.components) == 3:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.quiver(0, 0, 0, self.components[0],
                      self.components[1], self.components[2])
            plt.show()
        else:
            raise ValueError("Vector must have 2 or 3 components")

    def __str__(self):
        return str(self.components)
