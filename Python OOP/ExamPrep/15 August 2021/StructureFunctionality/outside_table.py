from project.table.table import Table
from project.validator import Validator


class OutsideTable(Table):
    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        Validator.if_value_is_in_range(value, 51, 100, "Outside table's number must be between 51 and 100 inclusive!")
        self.__table_number = value
