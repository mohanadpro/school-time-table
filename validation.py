from datetime import datetime

class Validation:

    def __init(self,data):
        self.data=data

    def validate_the_begin_of_the_day(self):
        timeformat = "%H:%M"
        try:
            validtime = datetime.datetime.strptime(self.time, timeformat)
            #Do your logic with validtime, which is a valid format
        except ValueError:
            #Do your logic for invalid format (maybe print some message?).
            print('error format')