import datetime


class Validation:
    """
    This is to validate all inputs if they match the required criteria
    """

    def validate_number_between_two_numbers(
            self,
            input_message,
            first_value,
            second_value,
            error_message):
        """
        To validate if number is between two numbers
        it takes the input message
        first value : ex 8
        second value : ex 15
        the number should be in the range between 8 and 15
        if not it return the error message
        """
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

    def validate_sum_of_sessions_per_week_match_sum_of_all_sessions_for_all_subjects(
            self,
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
            art_session_number):
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
            # first boolean value if they match or not
            # number_of_sessions_in_week and
            # number_of_sessions_in_all_subjects are
            # to show to the user with an input message
            # that he/she input how many
            # session per week he input
            # and how many number of all sessions
            return [True,
                    number_of_sessions_in_week,
                    number_of_sessions_in_all_subjects]
        else:
            return [False,
                    number_of_sessions_in_week,
                    number_of_sessions_in_all_subjects]

    def convert_time_to_minute(self, time):
        # it takes the time ex : 11:35
        #  and return 11 * 60 + 35 = 635
        return (
            int(time.split(':')[0]) * 60 + int(int(time.split(':')[1])))

    def validate_breaks_per_day(
            self,
            input_message,
            breaks_per_day,
            period_of_session_in_minutes):
        # validate if the provided break time is true
        # 10:25 is True , 11 is False
        timeformat = "%H:%M"
        while True:
            try:
                the_input = input(input_message)
                datetime.datetime.strptime(the_input, timeformat)
                if (len(breaks_per_day) > 0):
                    for break_value in breaks_per_day:
                        if (
                            self.convert_time_to_minute(the_input)
                            < (
                                self.convert_time_to_minute(break_value.time)
                                + break_value.period
                                + period_of_session_in_minutes)):
                            raise ValueError
                return the_input
            except ValueError:
                print('\033[31m' + 'Please input a valid time')
                print('\033[39m')
