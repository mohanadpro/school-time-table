from subject import Subject
import random
from user_input import UserInputs
from validation import Validation
from presentation import Presentation

time_table = {}
subject_list = []
user_input = UserInputs()

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


def devide_day_into_study_session(num_of_sessions_in_the_specific_day):
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
    time_table['Monday'] = devide_day_into_study_session(
        number_of_sessions_on_monday)
    time_table['Tuesday'] = devide_day_into_study_session(
        number_of_sessions_on_tuesday)
    time_table['Wedensday'] = devide_day_into_study_session(
        number_of_sessions_on_wednesday)
    time_table['Thurday'] = devide_day_into_study_session(
        number_of_sessions_on_thursday)
    time_table['Firday'] = devide_day_into_study_session(
        number_of_sessions_on_friday)


def initial_subject_list(
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
        art_session_number):
    """
    initial subject list
    each subject is an object that has
      name,number_of_session,priority this is for future
    for priority variable:
    the subjects have higher priority it will distributed
      in the first three sessions, but right now it's ignored
    """

    math = Subject('Math', math_session_number)
    physic = Subject('Physic', physic_session_number)
    chemistry = Subject('Chemistry', chemistry_session_number)

    science = Subject('Science', science_session_number)
    geography = Subject('Geography', geography_session_number)
    english = Subject('English', english_session_number)
    french = Subject('French', french_session_number)
    informatics = Subject('Informatics', informatics_session_number)
    politics = Subject('Politics', politics_session_number)

    sport = Subject('Sport', sport_session_number)
    music = Subject('Music', music_session_number)
    art = Subject('Art', art_session_number)
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


def assign_subject_to_specific_time(
        sessions_in_the_day,
        time,
        subject
        ):
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


def check_availability_by_specific_day_and_update(
        day,
        subject,
        number_of_sessions_on_monday,
        number_of_sessions_on_tuesday,
        number_of_sessions_on_wednesday,
        number_of_sessions_on_thursday,
        number_of_sessions_on_friday,
        math_session_number,
        physic_session_number,
        science_session_number,
        chemistry_session_number,
        geography_session_number,
        english_session_number,
        french_session_number,
        informatics_session_number,
        politics_session_number,
        sport_session_number,
        music_session_number,
        art_session_number,
        the_beginning_of_day,
        period_of_session_in_minutes,
        break_between_sessions
        ):
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
                    subject
                    )
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
                        subject
                        )
                    break
    if (is_infinit_loop is True):
        count_of_tries = 0
        (
            the_beginning_of_day,
            period_of_session_in_minutes,
            break_between_sessions,
            breaks_per_day,
            number_of_sessions_on_monday,
            number_of_sessions_on_tuesday,
            number_of_sessions_on_wednesday,
            number_of_sessions_on_thursday,
            number_of_sessions_on_friday,
            math_session_number,
            physic_session_number,
            science_session_number,
            chemistry_session_number,
            geography_session_number,
            english_session_number,
            french_session_number,
            informatics_session_number,
            politics_session_number,
            sport_session_number,
            music_session_number,
            art_session_number) = user_input.get_all_inputs()
        presentation = Presentation()
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

        subjectDistribution(
            number_of_sessions_on_monday,
            number_of_sessions_on_tuesday,
            number_of_sessions_on_wednesday,
            number_of_sessions_on_thursday,
            number_of_sessions_on_friday,
            math_session_number,
            physic_session_number,
            science_session_number,
            chemistry_session_number,
            geography_session_number,
            english_session_number,
            french_session_number,
            informatics_session_number,
            politics_session_number,
            sport_session_number,
            music_session_number,
            art_session_number,
            the_beginning_of_day,
            period_of_session_in_minutes,
            break_between_sessions
        )
        updated_time_table = (
            presentation.change_num_of_the_session_to_specific_time(
                time_table,
                the_beginning_of_day,
                period_of_session_in_minutes,
                break_between_sessions,
                breaks_per_day))
        presentation.print_time_table(updated_time_table)
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
        day = get_specific_day(
            i)
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


def check_if_in_same_day_subject_repeated(
        day,
        subjet_name
        ):
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


def subjectDistribution(
        number_of_sessions_on_monday,
        number_of_sessions_on_tuesday,
        number_of_sessions_on_wednesday,
        number_of_sessions_on_thursday,
        number_of_sessions_on_friday,
        math_session_number,
        physic_session_number,
        science_session_number,
        chemistry_session_number,
        geography_session_number,
        english_session_number,
        french_session_number,
        informatics_session_number,
        politics_session_number,
        sport_session_number,
        music_session_number,
        art_session_number,
        the_beginning_of_day,
        period_of_session_in_minutes,
        break_between_sessions
        ):
    """
    distribute subject until no subject found in subject list
    the distribution happens subject by subject
    the subject is taken randomly and will be checked
    if still has sessions
    a random day will be chosen automatically to insert subject in it
    """
    # print(time_table)
    while (len(subject_list) > 0):
        subject = subject_list[random.randint(0, len(subject_list)-1)]
        while (subject.count_of_sessions_per_week > 0):
            day = get_specific_day(random.randint(0, len(time_table)-1))
            check_availability_by_specific_day_and_update(
                day,
                subject,
                number_of_sessions_on_monday,
                number_of_sessions_on_tuesday,
                number_of_sessions_on_wednesday,
                number_of_sessions_on_thursday,
                number_of_sessions_on_friday,
                math_session_number,
                physic_session_number,
                science_session_number,
                chemistry_session_number,
                geography_session_number,
                english_session_number,
                french_session_number,
                informatics_session_number,
                politics_session_number,
                sport_session_number,
                music_session_number,
                art_session_number,
                the_beginning_of_day,
                period_of_session_in_minutes,
                break_between_sessions)


def initial_program(
        number_of_sessions_on_monday,
        number_of_sessions_on_tuesday,
        number_of_sessions_on_wednesday,
        number_of_sessions_on_thursday,
        number_of_sessions_on_friday,
        math_session_number,
        physic_session_number,
        science_session_number,
        chemistry_session_number,
        geography_session_number,
        english_session_number,
        french_session_number,
        informatics_session_number,
        politics_session_number,
        sport_session_number,
        music_session_number,
        art_session_number,
        the_beginning_of_day,
        period_of_session_in_minutes,
        break_between_sessions
        ):
    """
    This program is going to begin hier after all inputs
    it check if the validation True
    the program will start distributing the subject
    otherwise will appear a wrong message
    """
    validate = Validation()
    (
        validate_match_sum_of_session,
        number_of_sessions_in_week,
        number_of_sessions_in_all_subjects) = (
            validate.validate_sum_of_week_session_match_sum_of_all_sessions(
                number_of_sessions_on_monday,
                number_of_sessions_on_tuesday,
                number_of_sessions_on_wednesday,
                number_of_sessions_on_thursday,
                number_of_sessions_on_friday,
                math_session_number,
                physic_session_number,
                science_session_number,
                chemistry_session_number,
                geography_session_number,
                english_session_number,
                french_session_number,
                informatics_session_number,
                politics_session_number,
                sport_session_number,
                music_session_number,
                art_session_number
            ))
    if (validate_match_sum_of_session is True):
        (
            the_beginning_of_day,
            period_of_session_in_minutes,
            break_between_sessions,
            breaks_per_day,
            number_of_sessions_on_monday,
            number_of_sessions_on_tuesday,
            number_of_sessions_on_wednesday,
            number_of_sessions_on_thursday,
            number_of_sessions_on_friday,
            math_session_number,
            physic_session_number,
            science_session_number,
            chemistry_session_number,
            geography_session_number,
            english_session_number,
            french_session_number,
            informatics_session_number,
            politics_session_number,
            sport_session_number,
            music_session_number,
            art_session_number) = user_input.get_all_inputs()
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
    else:
        print('\033[31m'+"Sum of sessions per week doesn't" +
              " match the sum of all subject sessions \n"
              + " You have provided the sum of per week "
              + str(number_of_sessions_in_week)
              + " but you have provided the sum of all subject sessions "
              + str(number_of_sessions_in_all_subjects) + "\n")
        print('\033[39m')
        main()


def main():
    # inputs for the project
    print(
        "Welcome to school time table system"
        + ", please take into account"
        + " that time system is from 00:00 to 24:00 \n")

    print("Using this system you can generate "
          + "a school timetable "
          + "you have to provide the system with some info "
          + "which is specific for you school\n")

    user_input.handle_inputs()
    presentation = Presentation()
    (
        the_beginning_of_day,
        period_of_session_in_minutes,
        break_between_sessions,
        breaks_per_day,
        number_of_sessions_on_monday,
        number_of_sessions_on_tuesday,
        number_of_sessions_on_wednesday,
        number_of_sessions_on_thursday,
        number_of_sessions_on_friday,
        math_session_number,
        physic_session_number,
        science_session_number,
        chemistry_session_number,
        geography_session_number,
        english_session_number,
        french_session_number,
        informatics_session_number,
        politics_session_number,
        sport_session_number,
        music_session_number,
        art_session_number) = user_input.get_all_inputs()
    initial_program(
        number_of_sessions_on_monday,
        number_of_sessions_on_tuesday,
        number_of_sessions_on_wednesday,
        number_of_sessions_on_thursday,
        number_of_sessions_on_friday,
        math_session_number,
        physic_session_number,
        science_session_number,
        chemistry_session_number,
        geography_session_number,
        english_session_number,
        french_session_number,
        informatics_session_number,
        politics_session_number,
        sport_session_number,
        music_session_number,
        art_session_number,
        the_beginning_of_day,
        period_of_session_in_minutes,
        break_between_sessions
    )
    subjectDistribution(
        number_of_sessions_on_monday,
        number_of_sessions_on_tuesday,
        number_of_sessions_on_wednesday,
        number_of_sessions_on_thursday,
        number_of_sessions_on_friday,
        math_session_number,
        physic_session_number,
        science_session_number,
        chemistry_session_number,
        geography_session_number,
        english_session_number,
        french_session_number,
        informatics_session_number,
        politics_session_number,
        sport_session_number,
        music_session_number,
        art_session_number,
        the_beginning_of_day,
        period_of_session_in_minutes,
        break_between_sessions
    )
    updated_time_table = (
        presentation.change_num_of_the_session_to_specific_time(
            time_table,
            the_beginning_of_day,
            period_of_session_in_minutes,
            break_between_sessions,
            breaks_per_day
            ))
    presentation.print_time_table(updated_time_table)


main()
