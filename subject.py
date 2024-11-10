class Subject:
    """
    it has three parameters name ex: english , count of sessions ex: 5
    priority : 2 highest important subjects ex: Math , Physic.....
               1 less important ex: science, languages....
               0 the other subjects ex:sport, music ...
    """
    def __init__(self, name, count_of_sessions_per_week):
        self.name = name
        self.count_of_sessions_per_week = count_of_sessions_per_week
