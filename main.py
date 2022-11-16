# This is a sample Python script.
from Mathematics.Variables.VariableReplacement import VariableReplacement
from Mathematics.Enums.EquationIdentifers import EquationIdentifiers
from Mathematics.Variables.VariableParentheses import VariableParentheses
from Mathematics.Calculations.ExpandSimplify import ExpandSimplify

equation = [2.0, '*', 'b', '^', 3.0, '*', 3.0, '*', 'b', '+', 2.0]
variables = []
index = 0

while index < len(equation):
    variable = ExpandSimplify.group_values(equation, index)
    variables.append(variable)
    index += len(variable["variable"]) + 1

print(variables)

print("aa")

