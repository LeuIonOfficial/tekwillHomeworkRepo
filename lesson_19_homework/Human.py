from datetime import datetime

DATE_FORMAT = '%Y/%m/%d'


class Human:

    def __init__(self, first_name: str, last_name: str, dob):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob

    def __str__(self):
        pass

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_human_age(self):
        today = datetime.now()
        dob = datetime.strptime(self.dob, DATE_FORMAT)
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        return age


me = Human("Ion", "Leu", "2001/05/09")
print(f"{me.get_full_name()}, age {me.get_human_age()}")

