# This is a sample Python script.
from Mathematics.Eval.Evaluate import Evaluate
from Mathematics.Eval.Classification import Classification
from Mathematics.Validation.ComparisonValidation import ComparisonValidation
from Mathematics.Validation.VariableInputParser import VariableInputParser

equation = list('1+1>2+3')
number = VariableInputParser.variable_input_parser("a=2,b=5+3")
print(number)

print("aa")

