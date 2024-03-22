class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def diameter(self):
        return 2 * self._radius


# Usage
circle = Circle(5)
print(circle.diameter)  # Output: 10

circle.radius = 7  # Setting new radius
print(circle.diameter)  # Output: 14

circle.radius = -3  # This will raise a ValueError
