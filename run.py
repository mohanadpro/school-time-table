from subject import Subject
from break_per_day import BreakPerDay
import random
import datetime
breaks_per_day = []
# inputs for the project
print("Welcome to school time table system"
      + ", please take into account"
      + " that time system is from 00:00 to 24:00 \n")


def validate_number_between_two_numbers(
        input_message,
        first_value,
        second_value,
        error_message):
    while True:
        try:
            result = int(input(input_message))
            if (first_value <= result <= second_value):
                return result
            else:
                raise ValueError()
        except ValueError:
            print('\033[31m' + error_message)
            print('\033[39m')


the_beginning_of_day = validate_number_between_two_numbers(
    "At which hour start the first session"
    + " value between 8 and 10 \n",
    8,
    10,
    "Please enter value between 8 and 10")


period_of_session_in_minutes = validate_number_between_two_numbers(
    "Enter the period of the session"
    + " value between 30 and 60 \n",
    30,
    60,
    "Please enter value between 30 and 60")


break_between_sessions = validate_number_between_two_numbers(
    "Enter the break between sessions in minutes"
    + " value between 0 and 5, ex: 5 \n",
    0,
    5,
    "Please enter value between 0 and 5")


def convert_time_to_minute(time):
    return (
        int(time.split(':')[0]) * 60 + int(int(time.split(':')[1])))


def validate_breaks_per_day(input_message):
    timeformat = "%H:%M"
    while True:
        try:
            the_input = input(input_message)
            datetime.datetime.strptime(the_input, timeformat)
            if (len(breaks_per_day) > 0):
                for break_value in breaks_per_day:
                    if (
                        convert_time_to_minute(the_input)
                        < (
                            convert_time_to_minute(break_value.time)
                            + break_value.period
                            + period_of_session_in_minutes)):
                        raise ValueError
            return the_input
        except ValueError:
            print('\033[31m' + 'Please input a valid time')
            print('\033[39m')


how_many_break_per_day = validate_number_between_two_numbers(
    "How many breaks per day for example breakfast break, launch break"
    + "value between 1 and 2\n",
    1,
    2,
    "Please enter value between 1 and 2")


# add breaks between session depending the count of the breaks
for i in range(1, how_many_break_per_day + 1):
    end_of_word = ""
    match (i):
        case 1: end_of_word = "st"
        case 2: end_of_word = "nd"
    break_start = validate_breaks_per_day(
        f"At which time starts the {i}{end_of_word} break,"
        + " it should be at the end of a session, ex:10:25 \n"
    )
    break_period = validate_number_between_two_numbers(
        f"How many minutes lasts the {i}{end_of_word} break \n",
        10,
        60,
        "Please enter value between 10 and 60 "
        )
    break_per_day = BreakPerDay(break_start, break_period)
    breaks_per_day.append(break_per_day)


number_of_sessions_on_monday = validate_number_between_two_numbers(
    "Enter the number of sessions on monday,"
    + " value between 4 and 10 \n",
    4,
    10,
    'Please enter value between 4 and 10 \n')

number_of_sessions_on_tuesday = validate_number_between_two_numbers(
    "Enter the number of sessions on tuesday,"
    + " value between 4 and 10  \n",
    4,
    10,
    'Please enter value between 4 and 10 \n')

number_of_sessions_on_wednesday = validate_number_between_two_numbers(
    "Enter the number of sessions on wednesday,"
    + " value between 4 and 10  \n",
    4,
    10,
    'Please enter value between 4 and 10 \n')

number_of_sessions_on_thursday = validate_number_between_two_numbers(
    "Enter the number of sessions on thursday,"
    + " value between 4 and 10  \n",
    4,
    10,
    'Please enter value between 4 and 10 \n')

number_of_sessions_on_friday = validate_number_between_two_numbers(
    "Enter the number of sessions on friday,"
    + " value between 4 and 10  \n",
    4,
    10,
    'Please enter value between 4 and 10 \n')

math_session_number = validate_number_between_two_numbers(
    "Enter the number of math sessions,"
    + " value between 1 and 5  \n",
    1,
    5,
    'Please enter value between 1 and 5 \n')

physic_session_number = validate_number_between_two_numbers(
    "Enter the number of physic sessions,"
    + " value between 1 and 5  \n",
    1,
    5,
    'Please enter value between 1 and 5 \n')

chemistry_session_number = validate_number_between_two_numbers(
    "Enter the number of chemistry sessions,"
    + " value between 1 and 5  \n",
    1,
    5,
    'Please enter value between 1 and 5 \n')

science_session_number = validate_number_between_two_numbers(
    "Enter the number of science sessions,"
    + " value between 1 and 5  \n",
    1,
    5,
    'Please enter value between 1 and 5 \n')

geography_session_number = validate_number_between_two_numbers(
    "Enter the number of geography sessions,"
    + " value between 1 and 5  \n",
    1,
    5,
    'Please enter value between 1 and 5 \n')

english_session_number = validate_number_between_two_numbers(
    "Enter the number of english sessions,"
    + " value between 1 and 5  \n",
    1,
    5,
    'Please enter value between 1 and 5 \n')

french_session_number = validate_number_between_two_numbers(
    "Enter the number of french sessions,"
    + " value between 1 and 5  \n",
    1,
    5,
    'Please enter value between 1 and 5 \n')

informatics_session_number = validate_number_between_two_numbers(
    "Enter the number of informatics sessions,"
    + " value between 1 and 5  \n",
    1,
    5,
    'Please enter value between 1 and 5 \n')

politics_session_number = validate_number_between_two_numbers(
    "Enter the number of politics sessions,"
    + " value between 1 and 5  \n",
    1,
    5,
    'Please enter value between 1 and 5 \n')

sport_session_number = validate_number_between_two_numbers(
    "Enter the number of sport sessions,"
    + " value between 1 and 5  \n",
    1,
    5,
    'Please enter value between 1 and 5 \n')

music_session_number = validate_number_between_two_numbers(
    "Enter the number of music sessions,"
    + " value between 1 and 5  \n",
    1,
    5,
    'Please enter value between 1 and 5 \n')

art_session_number = validate_number_between_two_numbers(
    "Enter the number of art sessions,"
    + " value between 1 and 5  \n",
    1,
    5,
    'Please enter value between 1 and 5 \n')


def devidDayIntoStudySession(num_of_sessions_in_the_specific_day):
    """
    It takes a number of the sessions per day
    and return an initial dictionary
    that represents sessions for the mentioned day
    The keys are in the first numbers
    which will be replaced in the show to a time of the session
    for example 0 ---> 8:00 - 8:45
    """
    times = {}
    for i in range(num_of_sessions_in_the_specific_day):
        times[i] = ''
    return times


def convert_num_to_time(previous):
    """
    for the show: it takes previous session's time
    if the previous value is 0 so it will represent the first session
      in the day
      ex: 0: begin time of the day
    1: 8:45-9:45
    """
    if previous == 0:
        minutes_after_time_period = ((the_beginning_of_day) * 60
                                     + period_of_session_in_minutes)
        start_hour = the_beginning_of_day
        start_minutes = 0
        end_hour = int(minutes_after_time_period / 60)
        end_minutes = minutes_after_time_period % 60
        result = (str(start_hour) + ':'
                  + str("00" if start_minutes == 0 else start_minutes)
                  + '-'+str(end_hour) + ':'
                  + str("00" if end_minutes == 0 else end_minutes))
        return result
    else:
        previous_in_minutes = 0
        for break_per_day in breaks_per_day:
            if (previous == break_per_day.time):
                previous_in_minutes = (
                    int(float(previous.split(':')[0])) * 60
                    + int(float(previous.split(':')[1]))
                    + break_per_day.period)
                break
            else:
                previous_in_minutes = (
                    int(float(previous.split(':')[0])) * 60
                    + int(float(previous.split(':')[1]))
                    + break_between_sessions)

        end_session_in_minute = (
            previous_in_minutes
            + period_of_session_in_minutes)
        start_hour = int(previous_in_minutes / 60)
        start_minutes = previous_in_minutes % 60
        start_minutes_with_validation = (
            start_minutes if len(str(start_minutes))
            > 1 else "0" + str(start_minutes))
        end_hour = int(end_session_in_minute / 60)
        end_minutes = end_session_in_minute % 60
        end_minutes_with_validation = (
            end_minutes if len(str(end_minutes))
            > 1 else "0" + str(end_minutes))
        result = (str(start_hour) + ':'
                  + str("00" if start_minutes == 0
                        else start_minutes_with_validation)
                  + '-' + str(end_hour)
                  + ':'
                  + str("00" if end_minutes == 0
                        else end_minutes_with_validation))
        return result


def update_num_to_specific_time(time_table):
    """
    it's just for the show
    instead of present the session with 0 : 'Mathematic'
    it will be presented '8-8:45' ....
    hier the sessions will be send in a specific day
      and an updated result with time will be returned
    """
    updated_time_table_for_show = {}
    previous = 0
    for subject in time_table.values():
        time_now = convert_num_to_time(previous)
        previous = time_now.split('-')[1]
        updated_time_table_for_show[time_now] = subject
    return updated_time_table_for_show


def change_of_the_session_to_specific_time(school_time_table):
    """
    it's just for the show,
    instead of present the session with 0 : 'Mathematic'
      it will be presented '8-8:45' ....
    loop on each day and
    send its sessions to another function to be update it
    """
    updated_school_time_table = {}
    for day, time_with_subject in (
            zip(school_time_table.keys(), school_time_table.values())):
        updated_school_time_table[day] = update_num_to_specific_time(
            time_with_subject)
    return updated_school_time_table


time_table = {}


def initial_time_table(
        number_of_sessions_on_monday,
        number_of_sessions_on_tuesday,
        number_of_sessions_on_wednesday,
        number_of_sessions_on_thursday,
        number_of_sessions_on_friday):
    """
    it takes the number of sessions in each day
    and it will initial a dictionary like
        {
        'Monday':{'0':'','1','',.....}
        'Tuesday':{'0':'','1','',.....}
        ....
        }
    """
    time_table['Monday'] = devidDayIntoStudySession(
        number_of_sessions_on_monday)
    time_table['Tuesday'] = devidDayIntoStudySession(
        number_of_sessions_on_tuesday)
    time_table['Wedensday'] = devidDayIntoStudySession(
        number_of_sessions_on_wednesday)
    time_table['Thurday'] = devidDayIntoStudySession(
        number_of_sessions_on_thursday)
    time_table['Firday'] = devidDayIntoStudySession(
        number_of_sessions_on_friday)


subject_list = []


def initial_subject_list(math_session_number,
                         physic_session_number,
                         chemistry_session_number,
                         science_session_number,
                         geography_session_number,
                         english_session_number,
                         french_session_number,
                         informatics_session_number,
                         politics_session_number,
                         sport_session_number,
                         music_session_number,
                         art_session_number):
    """
    initial subject list
    each subject is an object that has
      name,number_of_session,priority this is for future
    for priority variable:
    the subjects have higher priority it will distributed
      in the first three sessions, but right now it's ignored
    """
    math = Subject('Math', math_session_number, 2)
    physic = Subject('Physic', physic_session_number, 2)
    chemistry = Subject('Chemistry', chemistry_session_number, 2)

    science = Subject('Science', science_session_number, 1)
    geography = Subject('Geography', geography_session_number, 1)
    english = Subject('English', english_session_number, 1)
    french = Subject('French', french_session_number, 1)
    informatics = Subject('Informatics', informatics_session_number, 1)
    politics = Subject('Politics', politics_session_number, 1)

    sport = Subject('Sport', sport_session_number, 0)
    music = Subject('Music', music_session_number, 0)
    art = Subject('Art', art_session_number, 1)
    subject_list.clear()
    subject_list.append(math)
    subject_list.append(physic)
    subject_list.append(chemistry)
    subject_list.append(science)
    subject_list.append(geography)
    subject_list.append(english)
    subject_list.append(french)
    subject_list.append(informatics)
    subject_list.append(politics)
    subject_list.append(sport)
    subject_list.append(music)
    subject_list.append(art)


def get_specific_day(num):
    """
    a specific day will be returned depending on the day's number
    ex: 0 -> monady
        1 -> tuesday ....
    """
    return list(time_table.keys())[num]


def assign_subject_to_specific_time(sessions_in_the_day, time, subject):
    """
    it take 3 params sessions_in_the_day
    : list of session with the value which will be updated in the future
    time : which time is chosed
    and the subject
    """
    sessions_in_the_day[time] = subject.name
    subject.count_of_sessions_per_week -= 1
    if (subject.count_of_sessions_per_week == 0):
        subject_list.remove(subject)


def print_time_table(time_table):
    """
    print the time table a simple loop on the dictionary
    """
    for day, session in zip(time_table.keys(), time_table.values()):
        print(day, session)


"""
This variable will be increased each time where
there is a day has empty session but the subject is repeated
for example I still have on Monday and Thursday empty sessions
and Mathematics subject has 2 sessions, but after checking it appears
 that these days have mathematics session
In this case the application will enter an infinite loop,
 so I used this variiable to check and  after 100 times of trying,
   exit the loop and initial the program again and execute it again
"""
count_of_tries = 0


def check_availability_by_specific_day_and_update(day, subject):
    """
        check if the day has an available time to insert subject in
        if session empty then check if it's the only day
        that has an empty session so insert it
        otherwise check if it's repeated and hier if this situation repeat
        100 times the program will be initialed againe run from the start
    """
    is_infinit_loop = False
    sessions_in_the_day = time_table[day]
    for time, session in (
            zip(sessions_in_the_day.keys(), sessions_in_the_day.values())):
        if (session == ''):
            is_just_one_day_empty = check_if_only_one_day_empty()
            if (is_just_one_day_empty is True):
                assign_subject_to_specific_time(
                    sessions_in_the_day,
                    time,
                    subject)
                break
            else:
                result = check_if_in_same_day_subject_repeated(
                    day,
                    subject.name)
                if (result is True):
                    global count_of_tries
                    count_of_tries += 1
                    if (count_of_tries > 100):
                        is_infinit_loop = True
                        break
                else:
                    assign_subject_to_specific_time(
                        sessions_in_the_day,
                        time,
                        subject)
                    break
    if (is_infinit_loop is True):
        count_of_tries = 0
        initial_time_table(number_of_sessions_on_monday,
                           number_of_sessions_on_tuesday,
                           number_of_sessions_on_wednesday,
                           number_of_sessions_on_thursday,
                           number_of_sessions_on_friday)

        initial_subject_list(math_session_number,
                             physic_session_number,
                             chemistry_session_number,
                             science_session_number,
                             geography_session_number,
                             english_session_number,
                             french_session_number,
                             informatics_session_number,
                             politics_session_number,
                             sport_session_number,
                             music_session_number,
                             art_session_number)

        subjectDistribution()
        updated_time_table = change_of_the_session_to_specific_time(time_table)
        print_time_table(updated_time_table)
        exit()


def check_if_only_one_day_empty():
    """
    check if the table just still have one day that has an empty session
    if True in that way it's normal to
    repeat the session if the same subject is found in that day
    if False the program is going to try in another day
    if the same subject is found in that day
    """
    list_days_has_empty_session = []
    for i in range(0, 5):
        day = get_specific_day(i)
        empty_session_count = 0
        for session in time_table[day].values():
            if (session == ''):
                empty_session_count += 1
        list_days_has_empty_session.append
        ({'day': day, 'empty_session_count': empty_session_count})

    count = 0
    for day in list_days_has_empty_session:
        if (day['empty_session_count'] > 0):
            count += 1
    if (count == 1):
        return True
    else:
        return False


def check_if_in_same_day_subject_repeated(day, subjet_name):
    """
    It takes day and the name of the subject
    and compare if the subject is repeated in this day
    If True repeated otherwise not
    """
    sessions_in_the_day = time_table[day]
    is_repeated = False
    for session in sessions_in_the_day.values():
        if (subjet_name == session):
            is_repeated = True
            break
        else:
            is_repeated = False
    return is_repeated


def subjectDistribution():
    """
    distribute subject until no subject found in subject list
    the distribution happens subject by subject
    the subject is taken randomly and will be checked
    if still has sessions
    a random day will be chosen automatically to insert subject in it
    """
    while (len(subject_list) > 0):
        subject = subject_list[random.randint(0, len(subject_list)-1)]
        while (subject.count_of_sessions_per_week > 0):
            day = get_specific_day(random.randint(0, len(time_table)-1))
            check_availability_by_specific_day_and_update(day, subject)


def validate_inputs():
    """
    I validate hier if the sum of all subject's sessions
    is equal to the sum of the session per week
    """
    number_of_sessions_in_week = (
        number_of_sessions_on_monday
        + number_of_sessions_on_tuesday + number_of_sessions_on_wednesday
        + number_of_sessions_on_thursday + number_of_sessions_on_friday)
    number_of_sessions_in_all_subjects = (
        math_session_number
        + physic_session_number + chemistry_session_number
        + science_session_number + geography_session_number
        + english_session_number + french_session_number
        + informatics_session_number + politics_session_number
        + sport_session_number + music_session_number + art_session_number)
    if number_of_sessions_in_week == number_of_sessions_in_all_subjects:
        return True
    else:
        return False


def initial_program():
    """
    This program is going to begin hier after all inputs
    it check if the validation True
    the program will start distributing the subject
    otherwise will appear a wrong message
    """
    if (validate_inputs() is True):
        initial_time_table(
            number_of_sessions_on_monday,
            number_of_sessions_on_tuesday,
            number_of_sessions_on_wednesday,
            number_of_sessions_on_thursday,
            number_of_sessions_on_friday)
        initial_subject_list(
            math_session_number,
            physic_session_number,
            chemistry_session_number,
            science_session_number,
            geography_session_number,
            english_session_number,
            french_session_number,
            informatics_session_number,
            politics_session_number,
            sport_session_number,
            music_session_number,
            art_session_number)
        subjectDistribution()
    else:
        print("Sum of sessions per week doesn't" +
              " match the sum of all subject sessions")


initial_program()
updated_time_table = change_of_the_session_to_specific_time(time_table)
print_time_table(updated_time_table)
