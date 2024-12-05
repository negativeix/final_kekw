class Person:
    def __init__(self, name:str, born:int = 500, job:str = "Unemployed", level:int = 1, money:int = 0):
        if not isinstance(name, str):
            raise TypeError("Can only be string.")
        if len(name) == 0:
            raise ValueError("Cannot be empty string.")
        if not isinstance(born, int):
            raise TypeError("born year need to be integer only.")
        if born < 0:
            raise ValueError("Born year cannot be under 0.")
        if not isinstance(job, str):
            raise TypeError("Can only be string.")
        if len(job) == 0:
            raise ValueError("Cannot be empty string.")
        if not isinstance(level, int):
            raise TypeError("level need to be integer only.")
        if level <= 0:
            raise ValueError("level cannot be less than or equal to 0.")
        if not isinstance(money, int):
            raise TypeError("money need to be integer only.")
        if money < 0:
            raise ValueError("money cannot be less than 0.")
        self.__name = name
        self.__born = born
        self.__job = job
        self.__level = level
        self.__money = money

    def __str__(self):
        return f"[{self.__job} {self.__name}, Level {self.__level}, born Year {self.__born}, $ {self.__money}]"

    @property
    def name(self):
        return self.__name

    @property
    def born(self):
        return self.__born

    @property
    def level(self):
        return self.__level

    @property
    def money(self):
        return self.__money

    @property
    def job(self):
        return self.__job

    @job.setter
    def job(self, value):
        if not isinstance(value, str):
            raise TypeError("self.job can only be string")
        if len(value) == 0:
            raise ValueError("Cannot be empty string")
        self.__job = value


'''
p = Person('Bob', 500, 'Unemployed', 1, 100)
p = Person('Bob', 400, 'Carpenter', 2)
p = Person('Bob', level=2, job='Something')
p = Person('Joe', born=100.0)
p = Person('Bob', money=-1)
'''