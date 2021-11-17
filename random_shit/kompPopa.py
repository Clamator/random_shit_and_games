from dataclasses import dataclass
from enum import Enum


@dataclass
class Popa:
    komp: int
    telek: bool
    channel: int


class Nums(Enum):
    IN_PROGRESS = 1
    FINISHED = 0
