class Validator:
    @staticmethod
    def if_name_is_empty_or_space_string(string, message):
        if not len(string.strip()) > 0:
            raise ValueError(message)

    @staticmethod
    def if_value_is_zero_or_negative(number, message):
        if number <= 0:
            raise ValueError(message)

    @staticmethod
    def if_value_is_in_range(number, min_val, max_val, message):
        if number < min_val or number > max_val:
            raise ValueError(message)
