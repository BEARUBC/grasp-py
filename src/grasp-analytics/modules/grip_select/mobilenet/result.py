from dataclasses import dataclass
from typing import List

from src.utils import BoundingBox


@dataclass
class MobileNetResult:
    boxes: List[BoundingBox]