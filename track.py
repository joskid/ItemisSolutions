import datetime as dt

# Classes
from session import Session

# Configuration
from configuration import Configuration


class Track:
    """ Track class """

    def __init__(self, id):
        """ Create track with deafult sessions including configuration
        like available time (in minutes) and start time """

        self.__id = id
        self.__sessions = []
        morning_session = Session(
            'Morning Session',
            180,
            dt.datetime.strptime(
                Configuration().MORNING_SESSION_START_TIME,
                '%H'
            )
        )
        afternoon_session = Session(
            'Afternoon Session',
            240,
            dt.datetime.strptime(
                Configuration().AFTERNOON_SESSION_START_TIME,
                '%H'
            )
        )
        self.__sessions.append(morning_session)
        self.__sessions.append(afternoon_session)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    def sessions(self):
        return self.__sessions

    def __str__(self):
        return f"Track {str(self.__id)}"
