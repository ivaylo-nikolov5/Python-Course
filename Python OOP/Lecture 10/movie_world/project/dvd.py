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
        _, month, year = date.split(".")
        months = {'01': 'January',
                  '02': 'February',
                  '03': 'March',
                  '04': 'April',
                  '05': 'May',
                  '06': 'June',
                  '07': 'July',
                  '08': 'August',
                  '09': 'September',
                  '10': 'October',
                  '11': 'November',
                  '12': 'December'}

        month = months[month]
        return cls(name, id, int(year), month, age_restriction)

    def __repr__(self):
        rented = "rented" if self.is_rented else "not rented"
        return f"{self.id}: {self.name} ({self.creation_month} {int(self.creation_year)}) has age restriction {self.age_restriction}. Status: {rented}"
