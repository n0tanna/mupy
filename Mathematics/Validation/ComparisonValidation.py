from Mathematics.Enums.ComparisonOperator import ComparisonIdentifiers
from Exceptions.OperatorErrors.IncorrectEqualsSignUsageError import IncorrectEqualsSignUsageError


class ComparisonValidation:

    @staticmethod
    def split_comparison(equation: list):
        left_values = []
        right_values = []
        equality_count = equation.count('=')

        if equality_count > 0:
            is_there_equality = equation.index('=')

            if equality_count == 1:
                if ComparisonIdentifiers.has_value(equation[is_there_equality - 1]):
                    if equation[is_there_equality - 1] is ComparisonIdentifiers.NOT.value:
                        comparison_operator = ComparisonIdentifiers.NOT_EQUAL

                    elif equation[is_there_equality - 1] is ComparisonIdentifiers.LESS_THAN.value:
                        comparison_operator = ComparisonIdentifiers.LESS_THAN_OR_EQUAL

                    elif equation[is_there_equality - 1] is ComparisonIdentifiers.GREATER_THAN.value:
                        comparison_operator = ComparisonIdentifiers.GREATER_THAN_OR_EQUAL

                    for index in range(is_there_equality - 1):
                        left_values.append(equation[index])

                    for index in range(is_there_equality + 1, len(equation)):
                        right_values.append(equation[index])

                    return {"left_equation": left_values, "right_equation": right_values,
                            "comparison_type": comparison_operator}

            elif equality_count == 2:
                if equation[is_there_equality + 1] == '=':
                    comparison_operator = ComparisonIdentifiers.EQUAL

                    # MAY USE LATER
                    # if equation[is_there_equality - 1] == ComparisonIdentifiers.NOT.value:
                    #     comparison_operator = ComparisonIdentifiers.NOT_IDENTICAL
                    #
                    #     for index in range(is_there_equality - 1):
                    #         left_values.append(equation[index])
                    #
                    #     for index in range(is_there_equality + 2, len(equation)):
                    #         right_values.append(equation[index])

                    for index in range(is_there_equality):
                        left_values.append(equation[index])

                    for index in range(is_there_equality + 2, len(equation)):
                        right_values.append(equation[index])

                    return {"left_equation": left_values, "right_equation": right_values,
                            "comparison_type": comparison_operator}

                else:
                    raise IncorrectEqualsSignUsageError

            # MAY USE LATER
            # elif equality_count == 3:
            #     if equation[is_there_equality + 1] == '=' and equation[is_there_equality + 2] == '=':
            #         comparison_operator = ComparisonIdentifiers.IDENTICAL
            #         for index in range(is_there_equality):
            #             left_values.append(equation[index])
            #
            #         for index in range(is_there_equality + 3, len(equation)):
            #             right_values.append(equation[index])
            #
            #         return {"left_equation": left_values, "right_equation": right_values,
            #                 "comparison_type": comparison_operator}
            #
            #     else:
            #         raise IncorrectEqualsSignUsageError

            else:
                raise IncorrectEqualsSignUsageError

        else:
            is_there_greater_than = equation.count('>')

            if is_there_greater_than > 0:
                is_there_greater_than = equation.index('>')
                comparison_operator = ComparisonIdentifiers.GREATER_THAN

                for index in range(is_there_greater_than):
                    left_values.append(equation[index])

                for index in range(is_there_greater_than + 1, len(equation)):
                    right_values.append(equation[index])

                return {"left_equation": left_values, "right_equation": right_values,
                        "comparison_type": comparison_operator}

            else:
                is_there_less_than = equation.index('<')
                comparison_operator = ComparisonIdentifiers.LESS_THAN

                for index in range(is_there_less_than):
                    left_values.append(equation[index])

                for index in range(is_there_less_than + 1, len(equation)):
                    right_values.append(equation[index])

                return {"left_equation": left_values, "right_equation": right_values,
                        "comparison_type": comparison_operator}

