# This is a sample Python script.
from mupy.Eval.Evaluate import Evaluate
from mupy.Eval.Classification import Classification
from mupy.Validation.ComparisonValidation import ComparisonValidation
from mupy.Validation.VariableInputParser import VariableInputParser
from mupy.Calculations.ReplaceVariables import ReplaceVariables

equation = list('1+1>2+3')
number = Evaluate.evaluate("10b==100", "b=10")
print(number)

print("aa")

