# Thesis Project Andrew Amazeen

Users are people looking to create a stock portfolio but
want the process to be automated. The project runs once
per day around noon and cycles through all the instructions
for the day. CSV files will store a list of current stock
positions as well as a list of all transactions.

## Install required libraries
Ensure that you are in the main directory and
run the following:

_This must be done before you can run the application
if you are not using the included venv._

```shell
$ pip install -r requirements.txt
```
or
```shell
$ pip install PILLOW
$ pip install pytest
```
Note: You need to import those packages in your
Python file.

## To run the program
Click the green triangle run icon in the
top-right corner of the PyCharm window.

or
```shell
$ python aamazeen_project.py
```

## Functionality
### Create Schedule
After entering your desired major(s), a sample course schedule
for your 4 years in college will be created, even combining
courses for double majors.

This output is a sample and can still be edited by selecting
different majors or editing your name and again selecting the
'Create Schedule' button.

On the back end, the code will automatically register the inputs
and determine which schedule to present to the user. These are
not yet recorded in the .csv file until the user decides to
finalize their schedule with the Submit button.

### Submit
Once a schedule is created, the user may choose to finalize
their schedule by clicking the Submit button. This takes record
of their name, majors, course schedule, and a timestamp of
their request. This also clears the entries so that a new user
may create a schedule with their own majors. Users may not use
the Submit button until they have created a schedule.

### Exit
The application will be closed when the Exit
button is clicked.

## Data files
### students.csv
The file contains the transaction data in the
following format:

| Time                     | Name   | Majors         | Schedule           |
|--------------------------|--------|----------------|--------------------|
| Wed Apr 26 12:51:20 2023 | Andrew | ['BDA', 'CIS'] | {'Fall 2022': ...} |
| Wed Apr 26 12:51:26 2023 | Lucas  | ['CIS']        | {'Fall 2022': ...} |
| Wed Apr 26 12:51:34 2023 | Ethan  | ['BDA']        | {'Fall 2022': ...} |

## Class

### Major Class

#### Variables
Each Major Class instance has the following
instance variables:
1. major: public, string data type
2. year: public, integer data type
3. credit_hours: public, float data type

Each Major Class instance has the following
properties:
- major getter
- major setter
- year getter
- year setter
- credit_hours getter
- credit_hours setter

#### Methods
The Account Class has the following methods:
* The dunder__init__(self, major, year, credit_hours) method
* The dunder__str__(self) method
* The update_hours(self, hours_earned) instance method