from project.month_mapper import month_mapper


class DVD:
    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        _, month, year = [int(x) for x in date.split('.')]
        month_name = month_mapper[month]
        return cls(name, id, year, month_name, age_restriction)

    def __repr__(self):
        if self.is_rented:
            state = "rented"
        else:
            state = "not rented"
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {state}"

