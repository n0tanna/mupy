from src.Mathematics.Calculations.Expand import Expand
from src.Mathematics.Calculations.Simplify import Simplify
from src.Mathematics.Validation.EquationValidation import EquationValidation

variable = [5.0, '*', 'b', '*', 'c', '^', 60.0]
variables = {"b": 2.0, "c": 1.0}
coefficients = [3.0]
response = Simplify.edit_values_dictionary(variable, variables, coefficients)

print("aa")

