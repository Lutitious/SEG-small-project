# Team *Ladybird* Small Group project

## Team members
The members of the team are:
- *Rahul Imran*
- *Abdulaziz Albanawi*
- *Anirudh George*
- *Mohammed Al Ibrahim*
- *Vishal Kumar*

## Project structure
The project is called `msms` (Music School Management System).  It currently consists of a single app `lessons` where all functionality resides.

## Deployed version of the application
The deployed version of the application can be found [here](https://lutitious.pythonanywhere.com/).

## Installation instructions
To install the software and use it in your local development environment, you must first set up and activate a local development environment.  From the root of the project:

```
$ virtualenv venv
$ source venv/bin/activate
```

Install all required packages:

```
$ pip3 install -r requirements.txt
```

Migrate the database:

```
$ python3 manage.py migrate
```

Seed the development database with:

```
$ python3 manage.py seed
```

Run all tests with:
```
$ python3 manage.py test
```

*The above instructions should work in your version of the application.  If there are deviations, declare those here in bold.  Otherwise, remove this line.*

## Sources
The packages used by this application are specified in `requirements.txt`

*Declare our other sources here.*
All of the tests in test_sign_up_form.py, test_sign_up_view.py and test_user_model.py unit tests are reused from the Clucker application.
