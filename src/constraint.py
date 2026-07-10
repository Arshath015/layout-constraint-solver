from src.grid_model import GridModel
from typing import List

class Constraint:
    def __init__(self, grid_model: GridModel):
        self.grid_model = grid_model

    def check(self, x: int, y: int, value: int) -> bool:
        # Check if the value satisfies the constraint
        # This is a placeholder for the actual logic
        return True