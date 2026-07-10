import pytest
from src.solver import Solver
from src.grid_model import GridModel

def test_solver_init):
    grid_model = GridModel(width=10, height=10)
    solver = Solver(grid_model)
    assert solver.grid_model == grid_model

def test_solve):
    grid_model = GridModel(width=2, height=2)
    solver = Solver(grid_model)
    solution = solver.solve()
    assert solution == [[0, 0], [0, 0]]