![School timetable](assets/images/result-image.png)

# School timetable 
---
This is an algorithm to create a school time table 
Every time the user executes the application he/she gets a different result

## instruction to use the app
### Features:
1. The user must enter the start time to the school 
![](assets/images/start-hour-right.png)
    * if user entered a wrong number a wrong message will appear
 ![](assets/images/start-hour-wrong.png)   
2. How many minutes lasts the session
![](assets/images/period-of-session.png)
3. How many minutes are between sessions
![](assets/images/break-between-sessions.png)
4. How many breaks per day, for ex: 2
![](assets/images/number-of-breaks'.png)
    * At which time starts start 1st break 
![](assets/images/1st%20break%20start.png)
    * How many minutes lasts the 1st break                              
![](assets/images/1st-break-period.png)    
    * At which time starts the 2nd break
![](assets/images/2nd-break-start.png)
    * How many minutes lasts the 2nd break                          
![](assets/images/2nd-break-period.png)
5. How many sessions on Monay
![](assets/images/number-of-sessions-on-monday.png)
6. How many sessions on Tuesday
![](assets/images/number-of-sessions-on-tuesday.png)
7. How many sessions on Wedensday
![](assets/images/number-of-sessions-on-wednesday.png)
8. How many sessions on Thursday
![](assets/images/number-of-sessions-on-thursday.png)
9. How many sessions on Friday
![](assets/images/number-of-sessions-on-friday.png)
10. How many mathematics's sessions
![](assets/images/number-of-math-sessions.png)
11. How many pyhisc's sessions
![](assets/images/number-of-physic-sessions.png)
12. How many chemistry's sessions
![](assets/images/number-of-chemistry-sessions.png)
13. How many science's sessions
![](assets/images/number-of-science-sessions.png)
14. How many geography's sessions
![](assets/images/number-of-geography-sessions.png)
15. How many english's sessions
![](assets/images/number-of-english-sessions.png)
16. How many french's sessions
![](assets/images/number-of-french-sessions.png)
17. How many informatics's sessions
![](assets/images/number-of-informatics-sessions.png)
18. How many politics's sessions
![](assets/images/number-of-politics-sessions.png)
19. How many sport's sessions
![](assets/images/number-of-sport-sessions.png)
20. How many music's sessions
![](assets/images/number-of-music-sessions.png)
21. How many art's sessions
![](assets/images/number-of-art-sessions.png)

## Future plan
* Take in account the priority so the subjects that has higher priority would be in the first 3 sessions in the day
* Work on the favorite days for the teachers so Mathematics teacher prefers to work on Monday and Wednesday
* Work on the not suitable days for the teacher so Mathematics teacher coudln't work on Tuesday

## Languages
* Python 3.11.9: used to anchor the project and direct all application behavior
* JavaScript: used to provide the start script needed to run the Code Institute mock terminal in the browser
* HTML used to construct the elements involved in building the mock terminal in the browser


## Tools:
---
* VSCode was used as the main tool to write and edit code.
* Git was used for the version control of the website.
* GitHub was used to host the code of the website.

## Testing
---
* All clear, no errors found except two functions, because they have a long name when passing through [CI Python Linter](https://pep8ci.herokuapp.com/#)
    * run.py
    ![](assets/images/run_py_validation.png)
    * user_input.py
    ![](assets/images/user_input_py_validation.png)
    * validation.py
    ![](assets/images/validation_py_validation.png)
    * presentaion.py
    ![](assets/images/presentaion_py_validation.png)
    * break_per_day.py
    ![](assets/images/break_per_day_py_validation.png)

### Manual Testing 
- Enter an invalid start hour, i got an error message and return to input the same field | PASS
![](assets/images/manual_testing_1.png)
- Enter invalid period for the session, i got an error message and return to input the same field | PASS
![](assets/images/)
- Enter invalid start time for the break, i got an error message and return to input the same field | PASS
![](assets/images/manual_testing_3.png)
- Enter sum of sessions per week not equal to sum of sessions for all subject, i got an error and the project will start from the beginning
![](assets/images/manual_testing_4.png)

### Compatibilty Testing
<details>
<summary>
    Google Chrom
</summary>
![](assets/images/Testing_Google_Chrome.png)
<details>

<details>
<summary>
    Microsoft Edge
</summary>
![](assets/images/Testing_Microsoft_Edge.png)
<details>

<details>
<summary>
    Mozella 
</summary>
![](assets/images/Testing_Firefox.png)
<details>

<details>
<summary>
    Opera
</summary>
![](assets/images/Testing_Opera.png)
<details>

## Deployment
---
* The program was deployed to [Heroku](https://dashboard.heroku.com/).
* The program can be reached by the [link](https://school-time-table-e8ecb79978ea.herokuapp.com/)
### To deploy the project as an application that can be run locally:
Note:

1. This project requires you to have Python installed on your local PC:
* sudo apt install python3
2. You will also need pip installed to allow the installation of modules the application uses.
* sudo apt install python3-pip
Create a local copy of the GitHub repository by following process below:
* Clone the repository:
    1. Open a folder on your computer with the terminal.
    2. Run the following command
    3. git clone https://github.com/IuliiaKonovalova/madlib_with_python.git
### To deploy the project to Heroku so it can be run as a remote web application
1. Create a Heroku account if you don't already have one here [Heroku](https://dashboard.heroku.com/).
2. Create a new Heroku application on the following page here New [Heroku App](https://dashboard.heroku.com/apps):
3. Go to the Deploy tab
4. Link your GitHub account and connect the application to the repository you created.
5. Go to the Settings tab
6. Click "Add buildpack"
7. Add the Python and Node.js buildpacks in the following order
8. Click Reveal Config Vars
9. Add 1 new Config Vars
10. Key: PORT    Value: 8000
    * This Config was provided by [CODE INSTITUTE](https://codeinstitute.net/de/).
11. Click Deploy Branch
12. Click View to launch the application inside a web page.

# Acknowledgements
I am enormously thankful to my mentor [Iuliia Konovalova](https://github.com/IuliiaKonovalova?tab=repositories) for her guidance and valuable feedback!