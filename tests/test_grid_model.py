import pytest
from src.grid_model import GridModel

def test_grid_model_init):
    grid_model = GridModel(width=10, height=10)
    assert grid_model.width == 10
    assert grid_model.height == 10
    assert grid_model.cells == [[0 for _ in range(10)] for _ in range(10)]

def test_get_cell):
    grid_model = GridModel(width=10, height=10)
    grid_model.set_cell(5, 5, 1)
    assert grid_model.get_cell(5, 5) == 1