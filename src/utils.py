from dataclasses import dataclass


@dataclass
class BoundingBox:
    x: int
    y: int
    w: int
    h: int

    """from top left and bottom right corners"""
    @classmethod
    def from_corners(cls, ax, ay, bx, by):
        if ax > bx:
            ax, bx = bx, ax
        if ay > by:
            ay, by = by, ay
        return cls(ax, ay, bx - ax, by - ay)
