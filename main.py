# This is a sample Python script.
from Mathematics.Variables.VariableReplacement import VariableReplacement
from Mathematics.Enums.EquationIdentifers import EquationIdentifiers

equation = list('1+1>2+3')
number = VariableReplacement.replace_variables(['2', 'a', 'b', '=', '3', '+', 'b', '+', 'c'], {'a': '2', 'b': ''}, EquationIdentifiers.VARIABLES)
print(number)

print("aa")

