import copy
from quiz1 import Person
from quiz2 import Quest


class Adventurer(Person):
    def __init__(self, name: str, born: int = 500, job: str = "Unemployed",
                 level: int = 1, money: int = 0):
        super().__init__(name, born, job, level, money)
        self.__current_quest = None

    @property
    def current_quest(self):
        return self.__current_quest

    def take(self, val):
        if not isinstance(val, Quest):
            raise ValueError("Value can only be Quest")
        if self.level < val.level:
            raise ValueError
        if val.job != "*":
            if self.job != val.job:
                raise ValueError

        self.__current_quest = copy.deepcopy(val)

    def complete(self):
        super().__init__(self.name, self.born, self.job, self.level,
                         self.money + self.__current_quest.reward)
        self.__current_quest = None

    def __repr__(self):
        return [self.name, self.born, self.job, self.level, self.money]

a= Quest('jo',10,200,'hunter')
b= Adventurer('B',2004,'hunter',11,200)
c= Adventurer('C',2004,'hunter',10,100)

for i in [b,c]:
    i.take(a)
    print(i.current_quest)
    i.complete()
    print(i.current_quest)
    print(i)





############################# 1st edition ####################################

# from quiz1 import Person
# from quiz2 import Quest
#
# class Adventure(Person):
#     def __init__(self,name,born,job,level,money,current_quest):
#         super().__init__(name,born,job,level,money)
#         if not isinstance(current_quest,Quest):
#             raise TypeError
#
#         self.__current_quest = current_quest
#
#     def take(self,):
#         if self.level >= current_quest.level and self.job == current_quest.job:
#             self.__current_quest = current_quest
#         pass
#
#     def complete(self):
#         self.__current_quest = None
