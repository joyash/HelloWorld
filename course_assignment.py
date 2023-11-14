class Hobby:
    def __init__(self, name, ):
        self.name = name
        self.people = []

    def add_hobby(self, name):
        self.people.append(name)


class Event:
    def __init__(self, name, date, location):
        self.name = name
        self.date = date
        self.location = location
        self.participants = []

    def add_event(self, pupil):
        self.participants.append(pupil)


hobby1 = Hobby("trekking")
hobby2 = Hobby("swimming")

event1 = Event("Concert", "2023-01-01", "Helsinki")
event2 = Event("Talent Hunt", "2023-02-02", "Vantaa")

hobby1.add_hobby("rabin")
hobby1.add_hobby("suresh")
hobby2.add_hobby("ritesh")
hobby2.add_hobby("rita")

event1.add_event("chrishtofer")
event1.add_event("nolan")
event2.add_event("maija")
event2.add_event("aamir")

"""for man in [hobby1, hobby2]:
    print(f"{man.people} are interested on these hobby: {man.name}")

for event in [event1, event2]:
    print(f"{event.participants} are goint to: {event.name} on {event.date} in {event.location}")
"""
hobbies = [hobby1, hobby2]  # Store all your Hobby instances in this list
event = [event1, event2]
for hobby in hobbies:
    print(f"{hobby.name} has followings participants {hobby.people}")

for i in event:
    print(f"{i.participants} are going to: {i.name} on {i.date} in {i.location}")
