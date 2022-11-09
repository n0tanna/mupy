# This is a sample Python script.
from Mathematics.Eval.Evaluate import Evaluate
from Mathematics.Eval.Classification import Classification
from Mathematics.Validation.ComparisonValidation import ComparisonValidation
from Mathematics.Validation.VariableInputParser import VariableInputParser
from Mathematics.Calculations.ReplaceVariables import ReplaceVariables

equation = list('1+1>2+3')
number = Evaluate.evaluate("10b==100", "b=10")
print(number)

print("aa")

