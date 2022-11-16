from src.Mathematics.Enums.ComparisonOperator import ComparisonIdentifiers


class Comparison:
    @staticmethod
    def compare_values(left_number, right_number, comparison_type: ComparisonIdentifiers):

        if comparison_type is ComparisonIdentifiers.EQUAL:
            if left_number == right_number:
                return True

            else:
                return False

        elif comparison_type is ComparisonIdentifiers.NOT_EQUAL:
            if left_number != right_number:
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

        elif comparison_type is ComparisonIdentifiers.GREATER_THAN_OR_EQUAL:
            if left_number >= right_number:
                return True

            else:
                return False

        elif comparison_type is ComparisonIdentifiers.LESS_THAN_OR_EQUAL:
            if left_number <= right_number:
                return True

            else:
                return False
