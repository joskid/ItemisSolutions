
import datetime as dt

# Classes
from configuration import Configuration
from talk import Talk
from track import Track
from conference import Conference


def run():

    conference = Conference()
    unorganized_talks = []  # talks not organized into sessions yet
    tracks_number = 0  # tracks to be created
    talks_total_duration = 0  # total amount of talks length

    """ Read of input (Tracks) """
    try:
        with open(Configuration().INPUT_FILE_NAME) as f:
            for line in f:
                words = line.split(' ')
                length_in_text = words[-1].rstrip('\r\n')
                length_in_minutes = length_in_text.replace('min', '')

                # If track length is 'lightning' then asign 5 min
                if length_in_minutes == 'lightning':
                    length_in_minutes = 5

                length = int(length_in_minutes)
                name = line.rstrip('\r\n')
                talk = Talk(name, length)
                unorganized_talks.append(talk)
    except FileNotFoundError:
        print('No existe el archivo \'input.txt\'')

    # Ordering talks not organized by descending length time
    unorganized_talks = sorted(
        unorganized_talks,
        key=lambda talk: talk.length,
        reverse=True
    )

    for talk in unorganized_talks:
        talks_total_duration += talk.length

    # Number of tracks to be created
    tracks_number = round(
        talks_total_duration/Configuration().TRACK_TIME + 0.5
    )
    conference.tracks_number = tracks_number

    # Tracks creation
    for t in range(tracks_number):
        track = Track(t + 1)
        conference.add_track(track)

    """ Assignment of talks in seassions and tracks """
    tracks = conference.tracks()
    organized_talks = []
    for t in tracks:

        for s in t.sessions():

            # Remove talks already organized and order
            unorganized_talks = set(
                unorganized_talks
            ).difference(organized_talks)

            unorganized_talks = sorted(
                unorganized_talks,
                key=lambda talk: talk.length,
                reverse=True
            )

            # Iterating through talks not organized yet
            for u in unorganized_talks:

                # Add talk to session if time is still available
                if s.available_time - u.length >= 0:
                    s.add_talk(u)
                    organized_talks.append(u)

                # Exit iteration is there is no time available in session
                if s.available_time == 0:
                    break

            # Adding default activities (Lunch and Networking Event)
            if s.name == 'Morning Session':
                s.add_default_activity(
                    Talk('Lunch', 60),
                    dt.datetime.strptime(
                        Configuration().LUNCH_TIME,
                        '%H'
                    )
                )
            else:
                """ Validation if hour that correspond to Networking Event
                is lower to the minimum time for this event (4PM) """

                networking_next_hour = dt.datetime.strptime(
                    Configuration().MINIMUM_NETWORKING_TIME,
                    '%H'
                )

                if s.next_hour < networking_next_hour:
                    s.add_default_activity(
                        Talk('Networking Event', 60),
                        dt.datetime.strptime(
                            Configuration().MINIMUM_NETWORKING_TIME,
                            '%H'
                        )
                    )
                else:
                    s.add_talk(Talk('Networking Event', 60))

    # Show all talks fitted into sessions and tracks
    conference.show_tracks()


if __name__ == '__main__':
    run()
