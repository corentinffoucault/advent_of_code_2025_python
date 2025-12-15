import math

class JunctionBox:
    __slots__ = ['_x', '_y', '_z', '_root', '_size']

    def __init__(self, x: int, y: int, z: int):
        self._x = x
        self._y = y
        self._z = z
        self._root = self
        self._size = 1

    @property
    def x(self) -> int:
        """X coordinate of Junction Box"""
        return self._x

    @property
    def y(self) -> int:
        """Y coordinate of Junction Box"""
        return self._y

    @property
    def z(self) -> int:
        """Z coordinate of Junction Box"""
        return self._z

    @property
    def root(self) -> "JunctionBox":
        """the root of"""
        return self._root

    @root.setter
    def root(self, new_root: "JunctionBox"):
        self._root = new_root

    @property
    def size(self) -> int:
        """te size of the root"""
        return self._size

    @size.setter
    def size(self, new_size: int):
        self._size = new_size

    def get_straight_line_distance(self, other: "JunctionBox") -> float:
        x_diff = self.x-other.x
        y_diff = self.y-other.y
        z_diff = self.z-other.z
        return math.sqrt(x_diff**2 + y_diff**2 + z_diff**2)

    def get_root(self) -> "JunctionBox":
        if self.root != self:
            self.root = self.root.get_root()
        return self.root

    def join_other_junction_box(self, other: "JunctionBox"):
        root_1 = self.get_root()
        root_2 = other.get_root()
        if root_1 == root_2:
            return

        if root_1.size < root_2.size:
            largest_root, shortest_root = root_2, root_1
        else:
            largest_root, shortest_root = root_1, root_2

        shortest_root.root = largest_root
        largest_root.size += shortest_root.size

    def __repr__(self):
        return f"JunctionBox({self.x}, {self.y}, {self.z})"