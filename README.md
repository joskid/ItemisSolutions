#  Conference Track Management

## Solutions
Step-1: Read talks input from file (file name configured in 'configuration.py') and create a list of unorganized talks with them.

Step-2: Ordering talks not organized by descending length time.

Step-3: Calculate number of tracks to be created based on talks total duration. Then create them.

Step-4: Assignment of talks in sessions and tracks, validating if there is available time in each session before to be added. Then remove from list of unorganized talks, all talks already added into a session.

Step-5: Finally, add default activities like 'Lunch' or 'Networking Time'.

## Run this solution
There is no need to install external libraries, just consider version of Python in which this was coded: 3.9.2. Then run:
```
python main.py
```

* Test Input
```
Writing Fast Tests Against Enterprise Rails 60min
Overdoing it in Python 45min
Lua for the Masses 30min
Ruby Errors from Mismatched Gem Versions 45min
Common Ruby Errors 45min
Rails for Python Developers lightning
Communicating Over Distance 60min
Accounting-Driven Development 45min
Woah 30min
Sit Down and Write 30min
Pair Programming vs Noise 45min
Rails Magic 60min
Ruby on Rails: Why We Should Move On 60min
Clojure Ate Scala (on my project) 45min
Programming in the Boondocks of Seattle 30min
Ruby vs. Clojure for Back-End Development 30min
Ruby on Rails Legacy App Maintenance 60min
A World Without HackerNews 30min
User Interface CSS in Rails Apps 30min
```

* Test Output
```
Track 1:
09:00AM Writing Fast Tests Against Enterprise Rails 60min
10:00AM Ruby on Rails Legacy App Maintenance 60min
11:00AM Communicating Over Distance 60min
12:00PM Lunch
01:00PM Rails Magic 60min
02:00PM Ruby on Rails: Why We Should Move On 60min
03:00PM Accounting-Driven Development 45min
03:45PM Overdoing it in Python 45min
04:30PM Programming in the Boondocks of Seattle 30min
05:00PM Networking Event
Track 2:
09:00AM Pair Programming vs Noise 45min
09:45AM Ruby Errors from Mismatched Gem Versions 45min
10:30AM Clojure Ate Scala (on my project) 45min
11:15AM Common Ruby Errors 45min
12:00PM Lunch
01:00PM Sit Down and Write 30min
01:30PM Ruby vs. Clojure for Back-End Development 30min
02:00PM A World Without HackerNews 30min
02:30PM Lua for the Masses 30min
03:00PM User Interface CSS in Rails Apps 30min
03:30PM Woah 30min
04:00PM Rails for Python Developers lightning
04:05PM Networking Event
```

