class R2Vector:
    """A two-dimensional vector, with methods for vector addition,
    scalar multiplication, and norm calculation.
    """

    def __init__(self, *, x, y):
        """Create a two-dimensional vector with a given x and y
        component.
        """
        self.x = x
        self.y = y

    def norm(self):
        """Calculate the norm of the vector.
        """
        return sum(val ** 2 for val in vars(self).values()) ** 0.5

    def __str__(self):
        """A string representation of the vector.
        """
        return str(tuple(getattr(self, i) for i in vars(self)))

    def __repr__(self):
        """A representation of the vector suitable for use in eval.
        """
        arg_list = [f'{key}={val}' for key, val in vars(self).items()]
        args = ', '.join(arg_list)
        return f'{self.__class__.__name__}({args})'

    def __add__(self, other):
        """Add two vectors elementwise.
        """
        if type(self) is not type(other):
            return NotImplemented
        kwargs = {i: getattr(self, i) + getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)

    def __sub__(self, other):
        """Subtract two vectors elementwise.
        """
        if type(self) is not type(other):
            return NotImplemented
        kwargs = {i: getattr(self, i) - getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)

    def __mul__(self, other):
        """Multiply a vector by a scalar or take the dot product of two
        vectors.
        """
        if type(other) in (int, float):
            kwargs = {i: getattr(self, i) * other for i in vars(self)}
            return self.__class__(**kwargs)
        elif type(self) is type(other):
            args = [getattr(self, i) * getattr(other, i) for i in vars(self)]
            return sum(args)
        return NotImplemented

    def __eq__(self, other):
        """Check if two vectors are equal.
        """
        if type(self) is not type(other):
            return NotImplemented
        return all(getattr(self, i) == getattr(other, i) for i in vars(self))

    def __ne__(self, other):
        """Check if two vectors are unequal.
        """
        return not self == other

    def __lt__(self, other):
        """Check if the norm of the vector is less than that of another
        vector.
        """
        if type(self) is not type(other):
            return NotImplemented
        return self.norm() < other.norm()

    def __gt__(self, other):
        """Check if the norm of the vector is greater than that of another
        vector.
        """
        if type(self) is not type(other):
            return NotImplemented
        return self.norm() > other.norm()

    def __le__(self, other):
        """Check if the norm of the vector is less than or equal to that of
        another vector.
        """
        return not self > other

    def __ge__(self, other):
        """Check if the norm of the vector is greater than or equal to that
        of another vector.
        """
        return not self < other


class R3Vector(R2Vector):
    def __init__(self, *, x, y, z):
        """Create a three-dimensional vector with a given x, y, and z
        component.
        """
        super().__init__(x=x, y=y)
        self.z = z

    def cross(self, other):
        """Calculate the cross product of two vectors in R3.
        """
        if type(self) is not type(other):
            return NotImplemented
        kwargs = {
            'x': self.y * other.z - self.z * other.y,
            'y': self.z * other.x - self.x * other.z,
            'z': self.x * other.y - self.y * other.x
        }

        return self.__class__(**kwargs)
