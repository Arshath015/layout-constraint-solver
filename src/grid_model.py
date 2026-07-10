from pydantic import BaseModel
from typing import List

class GridModel(BaseModel):
    width: int
    height: int
    cells: List[List[int]] = None

    def __init__(self, width: int, height: int, **kwargs):
        super().__init__(width=width, height=height, **kwargs)
        self.cells = [[0 for _ in range(width)] for _ in range(height)]

    def get_cell(self, x: int, y: int) -> int:
        return self.cells[y][x]

    def set_cell(self, x: int, y: int, value: int):
        self.cells[y][x] = value