# This is a sample Python script.
from Mathematics.Variables.VariableReplacement import VariableReplacement
from Mathematics.Enums.EquationIdentifers import EquationIdentifiers
from Mathematics.Variables.VariableParentheses import VariableParentheses
from Mathematics.Calculations.Expand import Expand
from Mathematics.Calculations.Simplify import Simplify

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

