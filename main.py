from mupy.Calculations.Expand import Expand
from mupy.Calculations.Simplify import Simplify

equation = [2.0, '*', 'b', '^', 3.0, '*', 3.0, '*', 'b', '*', 'c', '*', 2.0, 'b', '^', 5.0]
variables = []
index = 0

while index < len(equation):
    variable = Expand.group_variables(equation, index)
    variables.append(variable)
    index += len(variable["variable"]) + 1

holder = Simplify.simplify_multiplication(variables)

print(variables)
print(holder)

print("aa")

