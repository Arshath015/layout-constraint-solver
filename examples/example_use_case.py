from src.grid_model import GridModel
from src.solver import Solver

# Create a grid model
grid_model = GridModel(width=10, height=10)

# Create a solver
solver = Solver(grid_model)

# Solve the constraints
solution = solver.solve()

# Print the solution
for row in solution:
    print(row)