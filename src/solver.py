from src.grid_model import GridModel
from typing import List

class Solver:
    def __init__(self, grid_model: GridModel):
        self.grid_model = grid_model
        self.memo = {}

    def solve(self) -> List[List[int]]:
        return self.backtrack(0, 0)

    def backtrack(self, x: int, y: int) -> List[List[int]]:
        if (x, y) in self.memo:
            return self.memo[(x, y)]

        if x >= self.grid_model.width:
            x = 0
            y += 1

        if y >= self.grid_model.height:
            return self.grid_model.cells

        for value in range(2):
            if self.is_valid(x, y, value):
                self.grid_model.set_cell(x, y, value)
                solution = self.backtrack(x + 1, y)
                if solution:
                    return solution
                self.grid_model.set_cell(x, y, 0)

        self.memo[(x, y)] = None
        return None

    def is_valid(self, x: int, y: int, value: int) -> bool:
        # Check if the value is valid in the current cell
        # This is a placeholder for the actual logic
        return True