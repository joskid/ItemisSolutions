import datetime as dt


class Session:
    """ Session class """

    def __init__(self, name, available_time, next_hour):
        self.__name = name
        self.__available_time = available_time
        self.__next_hour = next_hour
        self.__talks = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def available_time(self):
        return self.__available_time

    @available_time.setter
    def available_time(self, available_time):
        self.__available_time = available_time

    @property
    def next_hour(self):
        return self.__next_hour

    @next_hour.setter
    def next_hour(self, next_hour):
        self.__next_hour = next_hour

    def talks(self):
        return self.__talks

    def add_talk(self, talk):
        """ Add talk to a session """

        talk.start_time = self.__next_hour
        self.__talks.append(talk)

        self.__available_time = self.__available_time - talk.length
        talk_time = dt.datetime.strptime(
            str(dt.timedelta(minutes=talk.length)),
            '%H:%M:%S'
        )
        time_zero = dt.datetime.strptime('0', '%H')
        self.__next_hour = self.__next_hour - time_zero + talk_time

    def add_default_activity(self, talk, start_time):
        """ Allows to add activities like Lunch and Networking Event """

        talk.start_time = start_time
        self.__talks.append(talk)

    def __str__(self):
        return self.__name
