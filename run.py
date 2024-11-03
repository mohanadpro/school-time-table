from subject import Subject
from break_per_day import BreakPerDay
import random


breaks_per_day=[]

# inputs for the project

the_beginning_of_day=int(input("At which hour start the first session \n"))
period_of_session_in_minutes=int(input("Enter the period of the session \n"))
break_between_days=int(input("Enter the break between sessions in minutes, ex: 5 \n"))
how_many_break_per_day=int(input("How many breaks per day for example breakfast break, launch break \n"))

# add breaks between session depending the count of the breaks
for i in range(1,how_many_break_per_day+1):
    end_of_word="" 
    match (i):
        case 1: end_of_word="st"
        case 2: end_of_word="nd"
        case 3: end_of_word="rd"
        case 4: end_of_word="th"
    break_start=input(f"At which time starts the {i}{end_of_word} break, it should be at the end of a session, ex:10:25 \n")
    break_period=int(input(f"How many minutes lasts the {i}{end_of_word} break \n"))
    break_per_day=BreakPerDay(break_start,break_period)
    breaks_per_day.append(break_per_day)


number_of_sessions_on_monday=int(input("Enter the number of sessions on monday \n"))
number_of_sessions_on_tuesday=int(input("Enter the number of sessions on tuesday \n"))

number_of_sessions_on_wednesday=int(input("Enter the number of sessions on wednesday \n"))
number_of_sessions_on_thursday=int(input("Enter the number of sessions on thursday \n"))
number_of_sessions_on_friday=int(input("Enter the number of sessions on friday \n"))


math_session_number=int(input("Enter the number of math sessions \n"))
physic_session_number=int(input("Enter the number of physic sessions \n"))
chemistry_session_number=int(input("Enter the number of chemistry sessions \n"))

science_session_number=int(input("Enter the number of science sessions \n"))
geography_session_number=int(input("Enter the number of geography sessions \n"))
english_session_number=int(input("Enter the number of english sessions \n"))
french_session_number=int(input("Enter the number of french sessions \n"))
informatics_session_number=int(input("Enter the number of informatics sessions \n"))
politics_session_number=int(input("Enter the number of politics sessions \n"))

sport_session_number=int(input("Enter the number of sport sessions \n"))
music_session_number=int(input("Enter the number of music sessions \n"))
art_session_number=int(input("Enter the number of art sessions \n"))




"""
It takes a number of sessions per day and return an initial dictionary that represents sessions for the mentioned day
The keys are right now numbers which will be replaced in the show as a time of the session for example 0 ---> 8:00 - 8:45
"""
def devidDayIntoStudySession(num_of_sessions_in_the_specific_day):
    times={}
    for i in range(num_of_sessions_in_the_specific_day):
        times[i]=''
    return times


"""
    for the show: it takes the begin time of the day and previous session's time and period of session
    so if the previous value is 0 so it will represents the first session in the day and that will presented 8:00 - 8:45
    1: 8:45-9:45

"""
def convert_num_to_time(previous):
    if previous==0 :
        minutes_after_time_period=(the_beginning_of_day)*60+period_of_session_in_minutes
        start_hour=the_beginning_of_day
        start_minutes=0
        end_hour=int(minutes_after_time_period/60)
        end_minutes=minutes_after_time_period%60
        return str(start_hour)+':'+str("00" if start_minutes==0 else start_minutes)+'-'+str(end_hour)+':'+str("00" if end_minutes==0 else end_minutes)
    else:
        previous_in_minutes=0
        for break_per_day in breaks_per_day:
            if(previous==break_per_day.time):                
                previous_in_minutes=int(float(previous.split(':')[0]))*60 + int(float(previous.split(':')[1]))+break_per_day.period
                break
            else:                
                previous_in_minutes=int(float(previous.split(':')[0]))*60 + int(float(previous.split(':')[1]))+break_between_days

        end_session_in_minute=previous_in_minutes+period_of_session_in_minutes
        start_hour=int(previous_in_minutes/60)
        start_minutes=previous_in_minutes%60 
        start_minutes_with_validation=start_minutes if len(str(start_minutes))>1 else "0"+ str(start_minutes)
        end_hour=int(end_session_in_minute/60)
        end_minutes=end_session_in_minute%60
        end_minutes_with_validation=end_minutes if len(str(end_minutes))>1 else "0"+ str(end_minutes)

        return str(start_hour)+':'+str("00" if start_minutes==0 else start_minutes_with_validation)+'-'+str(end_hour)+':'+str("00" if end_minutes==0 else end_minutes_with_validation)


"""
it's just for the show instead of represent the session with 0 : 'Mathematic' it will be represented '8-8:45' ....
hier the sessions will be send in a specific day and an updated result with time will be returned
"""
def update_num_to_specific_time(time_table):
    updated_time_table_for_show={}
    previous=0
    for num,subject in zip(time_table.keys(),time_table.values()):  
         time_now=convert_num_to_time(previous)   
         previous=time_now.split('-')[1]
         updated_time_table_for_show[time_now]=subject    
    return updated_time_table_for_show


"""
it's just for the show instead of represent the session with 0 : 'Mathematic' it will be represented '8-8:45' ....
loop on each day and send its sessions to another function to be update it
"""
def change_of_the_session_to_specific_time(school_time_table):
    updated_school_time_table={}
    for day,time_with_subject in zip(school_time_table.keys(),school_time_table.values()):
        updated_school_time_table[day]=update_num_to_specific_time(time_with_subject)
    return updated_school_time_table


time_table={}



"""
it takes the number of sessions in each day and it will initial a dictionary like 
    {
    'Monday':{'0':'','1','',.....}
    'Tuesday':{'0':'','1','',.....}
    ....
    }
"""
def initial_time_table(number_of_sessions_on_monday,number_of_sessions_on_tuesday,number_of_sessions_on_wednesday,number_of_sessions_on_thursday,number_of_sessions_on_friday):
    time_table['Monday']=devidDayIntoStudySession(number_of_sessions_on_monday)
    time_table['Tuesday']=devidDayIntoStudySession(number_of_sessions_on_tuesday)
    time_table['Wedensday']=devidDayIntoStudySession(number_of_sessions_on_wednesday)
    time_table['Thurday']=devidDayIntoStudySession(number_of_sessions_on_thursday)
    time_table['Firday']=devidDayIntoStudySession(number_of_sessions_on_friday)


"""
initial subject list 
each subject is an object name,number_of_session,priority this is for future

priority the subjects have higher priority it will distributed in the first three sessions, but right now it's ignored
"""
subject_list=[]
def initial_subject_list(math_session_number,physic_session_number,chemistry_session_number,science_session_number,geography_session_number,
                     english_session_number,french_session_number,informatics_session_number,politics_session_number,sport_session_number
                     ,music_session_number,art_session_number):
    math=Subject('Math',math_session_number,2)
    physic=Subject('Physic',physic_session_number,2)
    chemistry=Subject('Chemistry',chemistry_session_number,2)

    science=Subject('Science',science_session_number,1)
    geography=Subject('Geography',geography_session_number,1)
    english=Subject('English',english_session_number,1)
    french=Subject('French',french_session_number,1)
    informatics=Subject('Informatics',informatics_session_number,1)
    politics=Subject('Politics',politics_session_number,1)

    sport=Subject('Sport',sport_session_number,0)
    music=Subject('Music',music_session_number,0)
    art=Subject('Art',art_session_number,1)
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


"""
a specific day will be returned depending on the day's number
ex: 0 -> monady
    1 -> tuesday ....
"""
def get_specific_day(num):
   return list(time_table.keys())[num]



"""
it take 3 params sessions_in_the_day : list of session with the value which will be updated in the future
time : which time is chosed
and the subject 
"""
def assign_subject_to_specific_time(sessions_in_the_day,time,subject):
    sessions_in_the_day[time]=subject.name
    subject.count_of_sessions_per_week-=1
    if(subject.count_of_sessions_per_week==0):
        subject_list.remove(subject)
        

"""
    print the time table a simple loop on the dictionary 
"""
def print_time_table(time_table):
    for day,session in zip(time_table.keys(),time_table.values()):
        print(day,session)


"""
This variable will be increased each time where there is a day has empty session but the subject is repeated 
for example I still have Monday and Thursday and I still have Mathematics subject which has 2 sessions, but after checking it appears that these days have mathematics session
in this way the program will input in infinite loop , so I used this variiable to check after 100 times of trying to exit the loop and initial the program again and execute it again
"""
count_of_tries=0  



"""
    check if the day has an available time to insert subject in 
    if session empty then check if it's the only day that has an empty session so insert it 
    otherwise check if it's repeated and hier if this situation repeat 100 times the program will be initialed againe run from the start
"""
def check_availability_by_specific_day_and_update(day,subject):

    is_infinit_loop=False
    sessions_in_the_day=time_table[day]
    for time,session in zip(sessions_in_the_day.keys(),sessions_in_the_day.values()):       
        if(session==''):
            is_just_one_day_empty=check_if_only_one_day_empty()
            if(is_just_one_day_empty==True):
                 assign_subject_to_specific_time(sessions_in_the_day,time,subject)
                 break
            else:
                result=check_if_in_same_day_subject_repeated(day,subject.name)                
                if(result==True):
                        global count_of_tries
                        count_of_tries+=1
                        if(count_of_tries>100):
                            is_infinit_loop=True
                            break
                else:
                        assign_subject_to_specific_time(sessions_in_the_day,time,subject)
                        break
    if(is_infinit_loop==True):
        count_of_tries=0
        initial_time_table(number_of_sessions_on_monday,number_of_sessions_on_tuesday,number_of_sessions_on_wednesday,number_of_sessions_on_thursday,number_of_sessions_on_friday)

        initial_subject_list(math_session_number,physic_session_number,chemistry_session_number,science_session_number,geography_session_number,
                     english_session_number,french_session_number,informatics_session_number,politics_session_number,sport_session_number
                     ,music_session_number,art_session_number)

        subjectDistribution()
        updated_time_table=change_of_the_session_to_specific_time(time_table)
        print_time_table(updated_time_table)
        exit()



"""
check if the i just still have one day that has an empty session 
if True in that way it's normal to repeat the session if the same subject is found in that day 
if False the program is going to try in another day if the same subject is found in that day
"""
def check_if_only_one_day_empty():
    list_days_has_empty_session=[]
    for i in range(0,5):
        day=get_specific_day(i)
        empty_session_count=0
        for session in time_table[day].values():
            if(session==''):
                empty_session_count+=1
        list_days_has_empty_session.append({'day':day,'empty_session_count':empty_session_count})

    count=0
    for day in list_days_has_empty_session:
        if(day['empty_session_count']>0):
            count+=1   
    if(count==1):
        return True
    else:
        return False


"""
It takes day and the name of the subject and compare if the subject is repeated in this day
If True repeated otherwise not
"""
def check_if_in_same_day_subject_repeated(day,subjet_name):
    sessions_in_the_day=time_table[day]
    is_repeated=False
    for session in sessions_in_the_day.values():
        if(subjet_name==session):
            is_repeated=True
            break
        else:
            is_repeated= False
    return is_repeated
   

"""
distribute subject until no subject found in subject list 
the distribution happens subject by subject 
the subject is taken randomly and will be checked if still has sessions a random day will be chosen automatically to insert subject in it
"""
def subjectDistribution():    
    while(len(subject_list)>0):
        subject=subject_list[random.randint(0,len(subject_list)-1)]
        while(subject.count_of_sessions_per_week>0):
            day=get_specific_day(random.randint(0,len(time_table)-1))
            check_availability_by_specific_day_and_update(day,subject)





"""
I validate hier if the sum of all subject's sessions ia equal to the sum of the session per week
"""
def validate_inputs():
    number_of_sessions_in_week=number_of_sessions_on_monday+number_of_sessions_on_tuesday+number_of_sessions_on_wednesday+number_of_sessions_on_thursday+number_of_sessions_on_friday
    number_of_sessions_in_all_subjects=math_session_number+physic_session_number+chemistry_session_number+science_session_number+geography_session_number+ english_session_number+french_session_number+informatics_session_number+politics_session_number+sport_session_number+ music_session_number+art_session_number
    if(number_of_sessions_in_week==number_of_sessions_in_all_subjects):
        return True
    else:
        return False



"""
This program is going to begin hier after all inputs 
it check if the validation True the program will start distributing the subject otherwise will appear a wrong message
"""
def initial_program():
    if(validate_inputs()==True):
        initial_time_table(number_of_sessions_on_monday,number_of_sessions_on_tuesday,number_of_sessions_on_wednesday,number_of_sessions_on_thursday,number_of_sessions_on_friday)
        initial_subject_list(math_session_number,physic_session_number,chemistry_session_number,science_session_number,geography_session_number,
                            english_session_number,french_session_number,informatics_session_number,politics_session_number,sport_session_number
                            ,music_session_number,art_session_number)
        subjectDistribution()
    else:
        print("Sum of sessions per week doesn't match the sum of all subject sessions")
        


initial_program()
updated_time_table=change_of_the_session_to_specific_time(time_table)
print_time_table(updated_time_table)