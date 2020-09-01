# Us to You app {Backend}
## Step 1: Make sure you have PYTHON 3 installed
To check, use ```python3 -v```
If installed, proceed to step 2.
If not, look up [the docs](https://www.python.org/). lol.

## Step 2 Make sure Pip is installed
(It's like npm/yarn except for python.)

Run this code in your CLI of choice:
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```
...and after, run this:
```
python get-pip.py
```
It should automatically upgrade you to  ```pip3```


## Step 3 Create a Python Virtual env
```
python3 -m venv venv
```
Then activate it:
```
source venv/bin/activate
```

## Step 4 Get Django
```python
python3 -m pip3 install Django
pip3 install djangorestframework
```


## If this is your first time running this app:
Run this:
```
python3 manage.py migrate
```
This will init the SQLite Database.

## Step 5 Paste this into your CLI:
```python
python3 manage.py runserver
```
# Finally, check localhost:8000/admin
You should be able to login. Credentials are in the Discord dev chat.

## If any errors pop up
Post a screenshot or code snippet of the entire error into the Slack or Discord channel and tag Cat.

## Looking for the Frontend?
[Go here lol.](https://github.com/RoblesAarik/hackathon_frontend/)

## TODO:
- Create CRUD functionality
- Connect to frontend (look up axios for React)
- Create test users via frontend
