import os
from abc import ABC, abstractmethod
from typing import NamedTuple

current_dir = os.path.dirname(__file__)
ASSETS_DIR = os.path.join(current_dir, "..", "..", "assets", "images")


class Direction(NamedTuple):
    UP = -1
    DOWN = 1


class Piece(ABC):
    def __init__(
        self,
        id,
        name,
        color,
        asset,
        direction: Direction,
        value=None,
        texture_rect=None,
    ):
        self.id = id
        self.name = name
        self.color = color
        self.value = value
        self.texture_size = 80
        self.direction = direction
        self.asset = os.path.join(ASSETS_DIR, "80px", asset)
        self.texture_rect = texture_rect
        self.moved = False

    def update_asset_size(self, size):
        asset = self.asset.split(os.sep)[-1]
        self.asset = os.path.join(ASSETS_DIR, f"{size}px", asset)

    @abstractmethod
    def possible_moves(self, row, col):
        pass
