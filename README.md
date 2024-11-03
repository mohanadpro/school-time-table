![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# School timetable 
This is an algorithm to create a school time table 
Every time the user execute this application they get a different result

# live production 
https://school-time-table-e8ecb79978ea.herokuapp.com/

# instruction to use the app
# inputs:
1. The user must enter what time the school starts.
2. How many minutes lasts the session
3. How many minutes are between sessions
4. How many sessions in each day
5. How many sessions for every subject in the week


## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`
 
You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
