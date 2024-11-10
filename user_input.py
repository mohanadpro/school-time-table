from validation import Validation
from break_per_day import BreakPerDay


class UserInputs():
    """
    To handle user's inputs
    """
    breaks_per_day = []

    def __init(self):
        self.number_of_sessions_on_monday,
        self.number_of_sessions_on_tuesday,
        self.number_of_sessions_on_wednesday,
        self.number_of_sessions_on_thursday,
        self.number_of_sessions_on_friday,
        self.math_session_number,
        self.physic_session_number,
        self.science_session_number,
        self.chemistry_session_number,
        self.geography_session_number,
        self.english_session_number,
        self.french_session_number,
        self.informatics_session_number,
        self.politics_session_number,
        self.sport_session_number,
        self.music_session_number,
        self.art_session_number,
        self.the_beginning_of_day,
        self.period_of_session_in_minutes,
        self.break_between_sessions = 0

    def handle_inputs(self):
        validate = Validation()
        self.the_beginning_of_day = (
            validate.validate_number_between_two_numbers(
                "At which hour start the first session,"
                + " enter number from 8 to 10 \n",
                8,
                10,
                "Please enter number from 8 to 10"
            ))

        self.period_of_session_in_minutes = (
            validate.validate_number_between_two_numbers(
                "Enter the period of the session"
                + " enter number from 30 to 60 \n",
                30,
                60,
                "Please enter number from 30 to 60"))

        self.break_between_sessions = (
            validate.validate_number_between_two_numbers(
                "Enter the free time between sessions in minutes \n"
                + " enter number from 0 to 5 \n",
                0,
                5,
                "Please enter number from 0 to 5"))

        self.how_many_break_per_day = (
            validate.validate_number_between_two_numbers(
                "How many breaks per day"
                + "for example breakfast break, launch break,"
                + " value 1 or 2\n",
                1,
                2,
                "Please enter value 1 or 2"))

        # add breaks between session depending the count of the breaks
        for i in range(1, self.how_many_break_per_day + 1):
            end_of_word = ""
            match (i):
                case 1: end_of_word = "st"
                case 2: end_of_word = "nd"
            break_start = validate.validate_breaks_per_day(
                f"At which time starts the {i}{end_of_word} break,"
                + " it should be at the end of a session,\n ex:10:25 \n",
                self.breaks_per_day,
                self.period_of_session_in_minutes
            )
            break_period = validate.validate_number_between_two_numbers(
                f"How many minutes lasts the {i}{end_of_word} break \n",
                10,
                60,
                "Please enter number from 10 to 60 "
                )
            break_per_day = BreakPerDay(break_start, break_period)
            self.breaks_per_day.append(break_per_day)

        self.number_of_sessions_on_monday = (
            validate.validate_number_between_two_numbers(
                "Enter the number of sessions on monday,"
                + " enter number from 4 to 10 \n",
                4,
                10,
                'Please enter number from 4 to 10 \n'))

        self.number_of_sessions_on_tuesday = (
            validate.validate_number_between_two_numbers(
                "Enter the number of sessions on tuesday,"
                + " enter number from 4 to 10  \n",
                4,
                10,
                'Please enter number from 4 to 10 \n'))

        self.number_of_sessions_on_wednesday = (
            validate.validate_number_between_two_numbers(
                "Enter the number of sessions on wednesday,"
                + " enter number from 4 to 10  \n",
                4,
                10,
                'Please enter number from 4 to 10 \n'))

        self.number_of_sessions_on_thursday = (
            validate.validate_number_between_two_numbers(
                "Enter the number of sessions on thursday,"
                + " enter number from 4 to 10  \n",
                4,
                10,
                'Please enter number from 4 to 10 \n'))

        self.number_of_sessions_on_friday = (
            validate.validate_number_between_two_numbers(
                "Enter the number of sessions on friday,"
                + " enter number from 4 to 10  \n",
                4,
                10,
                'Please enter number from 4 to 10 \n'))

        self.math_session_number = (
            validate.validate_number_between_two_numbers(
                "Enter the number of math sessions,"
                + " enter number from 1 to 5  \n",
                1,
                5,
                'Please enter number from 1 to 5 \n'))

        self.physic_session_number = (
            validate.validate_number_between_two_numbers(
                "Enter the number of physic sessions,"
                + " enter number from 1 to 5  \n",
                1,
                5,
                'Please enter number from 1 to 5 \n'))

        self.chemistry_session_number = (
            validate.validate_number_between_two_numbers(
                "Enter the number of chemistry sessions,"
                + " enter number from 1 to 5  \n",
                1,
                5,
                'Please enter number from 1 to 5 \n'))

        self.science_session_number = (
            validate.validate_number_between_two_numbers(
                "Enter the number of science sessions,"
                + " enter number from 1 to 5  \n",
                1,
                5,
                'Please enter number from 1 to 5 \n'))

        self.geography_session_number = (
            validate.validate_number_between_two_numbers(
                "Enter the number of geography sessions,"
                + " enter number from 1 to 5  \n",
                1,
                5,
                'Please enter number from 1 to 5 \n'))

        self.english_session_number = (
            validate.validate_number_between_two_numbers(
                "Enter the number of english sessions,"
                + " enter number from 1 to 5  \n",
                1,
                5,
                'Please enter number from 1 to 5 \n'))

        self.french_session_number = (
            validate.validate_number_between_two_numbers(
                "Enter the number of french sessions,"
                + " enter number from 1 to 5  \n",
                1,
                5,
                'Please enter number from 1 to 5\n'))

        self.informatics_session_number = (
            validate.validate_number_between_two_numbers(
                "Enter the number of informatics sessions,"
                + " enter number from 1 to 5  \n",
                1,
                5,
                'Please enter number from 1 to 5 \n'))

        self.politics_session_number = (
            validate.validate_number_between_two_numbers(
                "Enter the number of politics sessions,"
                + " enter number from 1 to 5  \n",
                1,
                5,
                'Please enter number from 1 to 5 \n'))

        self.sport_session_number = (
            validate.validate_number_between_two_numbers(
                "Enter the number of sport sessions,"
                + " enter number from 1 to 5  \n",
                1,
                5,
                'Please enter number from 1 to 5 \n'))

        self.music_session_number = (
            validate.validate_number_between_two_numbers(
                "Enter the number of music sessions,"
                + " enter number from 1 to 5  \n",
                1,
                5,
                'Please enter number from 1 to 5 \n'))

        self.art_session_number = (
            validate.validate_number_between_two_numbers(
                "Enter the number of art sessions,"
                + " enter number from 1 to 5  \n",
                1,
                5,
                'Please enter number from 1 to 5 \n'))

        return (
            self.the_beginning_of_day,
            self.period_of_session_in_minutes,
            self.break_between_sessions,
            self.how_many_break_per_day,
            self.breaks_per_day,
            self.number_of_sessions_on_monday,
            self.number_of_sessions_on_tuesday,
            self.number_of_sessions_on_wednesday,
            self.number_of_sessions_on_thursday,
            self.number_of_sessions_on_friday,
            self.math_session_number,
            self.physic_session_number,
            self.science_session_number,
            self.chemistry_session_number,
            self.geography_session_number,
            self.english_session_number,
            self.french_session_number,
            self.informatics_session_number,
            self.politics_session_number,
            self.sport_session_number,
            self.music_session_number,
            self.art_session_number)

    def get_all_inputs(self):
        return (self.the_beginning_of_day,
                self.period_of_session_in_minutes,
                self.break_between_sessions,
                self.breaks_per_day,
                self.number_of_sessions_on_monday,
                self.number_of_sessions_on_tuesday,
                self.number_of_sessions_on_wednesday,
                self.number_of_sessions_on_thursday,
                self.number_of_sessions_on_friday,
                self.math_session_number,
                self.physic_session_number,
                self.science_session_number,
                self.chemistry_session_number,
                self.geography_session_number,
                self.english_session_number,
                self.french_session_number,
                self.informatics_session_number,
                self.politics_session_number,
                self.sport_session_number,
                self.music_session_number,
                self.art_session_number)
