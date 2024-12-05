class Quest:
    def __init__(self, title:str, level:int = 1, reward:int = 0, job:str = "*"):
        if not isinstance(title, str):
            raise TypeError("Can only be string.")
        if len(title) == 0:
            raise ValueError("Cannot be empty string.")

        if not isinstance(level, int):
            raise TypeError("level need to be integer only.")
        if level <= 0:
            raise ValueError("level cannot be less than or equal to 0.")

        if not isinstance(reward, int):
            raise TypeError("reward need to be integer only.")
        if reward < 0:
            raise ValueError("reward cannot be less than 0.")

        if not isinstance(job, str):
            raise TypeError("Can only be string.")
        if len(job) == 0:
            raise ValueError("Cannot be empty string.")
        self.__title = title
        self.__level = level
        self.__reward = reward
        self.__job = job
    def __str__(self):
        return f'''[Quest "{self.__title}" for Level {self.__level} {self.__job}, $ {self.__reward}]'''
    @property
    def title(self):
        return self.__title
    @property
    def level(self):
        return self.__level
    @property
    def reward(self):
        return self.__reward
    @property
    def job(self):
        return self.__job