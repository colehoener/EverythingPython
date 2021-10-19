class Birthday():
    def __init__(self, day = 00, month = 00, year = 0000):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return(str(self.day) + '/' + str(self.month) + '/' + str(self.year))

    def __hash__(self):
        return (self.day + self.month + self.year) % 12

    def __eq__(self, otherBirthday):
        if(self.day == otherBirthday.day and self.month == otherBirthday.month and self.year == otherBirthday.year):
            return True
        else:
            return False