class Zodiac:
    def __init__(self, name, surname, zodiac, day, month, year):
        self.name = name
        self.surname = surname
        self.zodiac = zodiac
        self.day = day
        self.month = month
        self.year = year
        self.birthday = [day, month, year]

    def getName(self):
        return self.name

    def getSurname(self):
        return self.surname

    def getZodiac(self):
        return self.zodiac

    def getBirthday(self):
        return self.birthday

    def setName(self, name):
        self.name = name

    def setSurname(self, surname):
        self.surname = surname

    def setZodiac(self, zodiac):
        self.zodiac = zodiac

    def setBirthday(self, day, month, year):
        # self.day=day
        # self.month = month
        # self.year =year
        self.birthday = [day, month, year]