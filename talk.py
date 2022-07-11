class Talk:
    """ Talk class """

    __start_time = ''

    def __init__(self, name, length):
        self.__name = name
        self.__length = length

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        self.__length = length

    @property
    def start_time(self):
        return self.__start_time

    @start_time.setter
    def start_time(self, start_time):
        self.__start_time = start_time

    def __str__(self):
        return f"{self.__start_time.strftime('%I:%M%p')} {self.__name}"
