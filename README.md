### Date created
* **bikeshare.py** was written on 21/10/2018.
* This **README** file was written on 28/10/2018.

### US Bikeshare
This is an interactive project written in Python that allows the user to get some insights and stats on the bike share systems in Chicago, New York City, and Washington.

### Requirements
To run this program you need:
* Python 3
* Numpy and Pandas libraries (installed using Anaconda)
* Terminal application
* Text editor (I used *Atom*)

### Files used
The three csv files provided for the projects, namely:
1. *chicago.csv*
2. *washington.csv*
3. *new_york_city.csv*

Moreover, the *bikeshare.py* template provided by the course has been used as a starting point for the main structure of the project.

### Description
In the **main** function, different functions are called following the order and structure included in the template provided by the course.

Throughout the interactive experience, the code checks for typos or inappropriate input and displays calculation times.

The functions in the project are the following:
1.  *get_filters*: asks the user's input to select one of the three cities and, if desired, filter on a month or day of the week
2. *load_data*: loads data according to user's input
3. *show_data*: function I added to original template in order to ask the user whether s(he) wants to see the data loaded
4. *time_stats*: outputs the most common month, hour and day of travel (given the data selected earlier)
5. *station_stats*: outputs the most common start, end and combination of stations
6. *trip_duration_stats*: displays statistics on total and average trip duration
7. *user_stats*: provides details on the population of users such as gender and birth year

### Credits
The *Programming for Data Science* tutors and the Udacity community :sparkles:
