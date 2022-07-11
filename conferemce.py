class Conference:
    """ Conference class """

    __tracks_number = 0

    def __init__(self):
        self.__tracks = []

    @property
    def tracks_number(self):
        return self.__tracks_number

    @tracks_number.setter
    def tracks_number(self, tracks_number):
        self.__tracks_number = tracks_number

    def tracks(self):
        return self.__tracks

    def add_track(self, track):
        self.__tracks.append(track)

    def show_tracks(self):
        """ Print all talks fitted into sessions
        and tracks """

        for track in self.__tracks:
            print(f"Track {track.id}:")
            for session in track.sessions():
                for talk in session.talks():
                    print(talk)
