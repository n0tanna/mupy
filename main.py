# This is a sample Python script.
from Mathematics.Eval.Evaluate import Evaluate
from Mathematics.Eval.Classification import Classification
from Mathematics.Validation.ComparisonValidation import ComparisonValidation

equation = list('1+1>2+3')
number = ComparisonValidation.split_equation(equation)
print(number)

print("aa")

