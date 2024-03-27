1)To work with the project you must perform the following steps:
Clone the repository.
Activate virtual environment env/bin/activate.bat
Install dependencies pip install -r requirements.txt
Create a .env file, fill it with data from the env.sample file
Create a database in PostreSQL CREATE DATABASE qw7;
Create python manage.py makemigrate and apply migrations python manage.py migrate
Create a user with python manage.py csu command
Install and run Docker Desktop locally (on Windows)
Build the image using docker-compose build
Start containers with docker-compose up command
Open your browser and go to http://127.0.0.1:8000 to access the application.


2)The following tasks have been solved:
CORS configured
Integration with Telegram has been configured
Pagination implemented
Environment variables used
All necessary models are described or redefined
All necessary endpoints have been implemented
All necessary validators are configured
The described access rights are reserved
Configured a deferred task via Celery
The project is at least 80% covered by tests
The code is designed in accordance with best practices
There is a list of dependencies
Flake8 check result is 100%, excluding migrations
The solution is posted on GitHub


3)Description of tasks
Added necessary habit models
Implemented endpoints for working with the frontend
An application has been created for working with Telegram and sending reminders


4)Model Habit:
The user is the creator of the habit.
Location - the location where the habit needs to be performed.
Time is the time when you need to perform the habit.
Action is an action that is a habit.
A sign of a pleasant habit is a habit that can be tied to the performance of a useful habit.
A linked habit is a habit that is linked to another habit, important to indicate for good habits, but not for pleasant ones.
Frequency (daily by default) – frequency of habit execution for the reminder in days.
Reward - how the user should reward himself after completion.
Time to complete is the time the user is expected to spend completing the habit.
A sign of publicity - habits can be published publicly so that other users can follow other people’s habits as an example.


5)Model User:
mail,
chat_id


6)Validators
Eliminate the simultaneous selection of a related habit and indication of a reward.
The execution time should be no more than 120 seconds.
Linked habits can only include habits with the sign of a pleasant habit.
An enjoyable habit cannot have a reward or an associated habit.
You cannot perform the habit less than once every 7 days.


7)Pagination
To display a list of habits, implement pagination with output of 5 habits per page.


8)Access rights
Each user has access only to their habits using the CRUD mechanism.
The user can see a list of public habits without the ability to somehow edit or delete them.


9)Endpoints
Registration
Authorization
List of habits of the current user with pagination
List of public habits
Creating a Habit
Editing a Habit
Deleting a habit


10)Integration
For the service to function fully, it is necessary to implement work with deferred tasks to remind you at what time which habits need to be performed. To do this, you will need to integrate the service with the Telegram messenger, which will send out notifications.


11)Safety
The project needs to configure CORS so that the frontend can connect to the project on the deployed server.


12)Documentation
To implement screens using front-end developers, you need to configure the output of documentation. If necessary, describe endpoints for which documentation will not be generated automatically.

The documentation for the API is implemented using drf-yasg and is located at the following endpoints:

http://127.0.0.1:8000/docs/
http://127.0.0.1:8000/redoc/


13)project testing
To test the project, run the command: python manage.py test
