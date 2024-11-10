class Presentation:
    """
    This class is responsible to display the time table
    """

    def convert_num_to_time(
            self,
            previous,
            the_beginning_of_day,
            period_of_session_in_minutes,
            break_between_sessions,
            breaks_per_day
            ):
        """
        for the show: it takes previous session's time
        if the previous value is 0 so it will represent the first session
        in the day
        ex: 0: begin time of the day
        1: 8:45-9:45
        """
        if previous == 0:
            minutes_after_time_period = (
                (the_beginning_of_day) * 60
                + period_of_session_in_minutes)
            start_hour = the_beginning_of_day
            start_minutes = 0
            end_hour = int(minutes_after_time_period / 60)
            end_minutes = minutes_after_time_period % 60
            result = (
                str(start_hour) + ':'
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
            result = (
                str(start_hour) + ':'
                + str("00" if start_minutes == 0
                      else start_minutes_with_validation)
                + '-' + str(end_hour)
                + ':'
                + str("00" if end_minutes == 0
                      else end_minutes_with_validation))
            return result

    def update_num_to_specific_time(
            self,
            time_table,
            the_beginning_of_day,
            period_of_session_in_minutes,
            break_between_sessions,
            breaks_per_day):
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
            time_now = self.convert_num_to_time(
                previous,
                the_beginning_of_day,
                period_of_session_in_minutes,
                break_between_sessions,
                breaks_per_day)
            previous = time_now.split('-')[1]
            updated_time_table_for_show[time_now] = subject
        return updated_time_table_for_show

    def change_num_of_the_session_to_specific_time(
            self,
            school_time_table,
            the_beginning_of_day,
            period_of_session_in_minutes,
            break_between_sessions,
            breaks_per_day):
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
            updated_school_time_table[day] = self.update_num_to_specific_time(
                time_with_subject,
                the_beginning_of_day,
                period_of_session_in_minutes,
                break_between_sessions,
                breaks_per_day
                )
        return updated_school_time_table

    def print_time_table(self, time_table):
        """
        print the time table a simple loop on the dictionary
        """
        for day, session in zip(time_table.keys(), time_table.values()):
            print(day, session)
