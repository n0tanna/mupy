from Mathematics.Enums.ComparisonOperator import ComparisonIdentifiers


class Comparison:
    @staticmethod
    def compare_values(left_equation: list, right_equation: list, comparison_type: ComparisonIdentifiers):
        left_number = left_equation[0]
        right_number = right_equation[0]

        if comparison_type is ComparisonIdentifiers.EQUAL:
            if left_number == right_number:
                return True

            else:
                return False

        elif comparison_type is ComparisonIdentifiers.GREATER_THAN:
            if left_number > right_number:
                return True

            else:
                return False

        elif comparison_type is ComparisonIdentifiers.LESS_THAN:
            if left_number < right_number:
                return True

            else:
                return False
