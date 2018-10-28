import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Which city would you like to pick, Chicago, New York or Washington? \n').lower()
    while city not in CITY_DATA.keys():
        city = input('Your input is not valid. Please pick either Chicago, New York or Washington: \n ').lower()
    print('Cool! you picked: {}.'.format(city.title()))

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('\nWould you like to pick a month? If yes, type one of the first 6 months otherwise write All:\n').lower()
    while month not in months and month != 'all':
        month = input('Your input is not valid. Please pick either january, february, march, april, may or june. Otherwise type All:\n ').lower()
    print('Cool! you picked: {}.'.format(month.title()))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day= input('\nWould you like to pick a day of the week? If yes please type which one otherwise write all: \n').lower()
    while day not in days and day != 'all':
        day = input('Your input is not valid. Please pick either Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday. Otherwise type All:\n ').lower()
    print('Cool! you picked: {}.'.format(day.title()))

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1

        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.title()]

    return df

def show_data(df):
    """Asks the user if (s)he wants to see raw data."""

    answer = input('\nWould you like to see how the data looks like? Please type yes or no: ').lower()
    while answer not in ['yes','no']:
        answer = input('Please state whether you would like to see raw data. Type yes or no: ').lower()

    if answer == 'yes':
        print(df.head(5))
        further = input('\nWould you like to see more? Please type yes or no: ')
        while further not in ['yes','no']:
            further = input('Please state whether you would like to see raw data. Type yes or no: ').lower()
        i=5
        while further != 'no':
              print(df.iloc[i:i+5])
              i+=5
              further = input('Please state whether you would like to see raw data. Type yes or no: ').lower()
    else:
        print('\nLet\'s then go to the stats!\n')

def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if month == 'all':
        common_month = df['month'].mode()[0]
        common_month = months[common_month-1].title()
        print('The most common month is: {}'.format(common_month))

    # TO DO: display the most common day of week
    if day == 'all':
        common_day = df['day_of_week'].mode()[0]
        print('The most common day is: {}'.format(common_day))

    # TO DO: display the most common start hour
    common_hour = df['Start Time'].dt.hour.mode()[0]
    if common_hour<12:
        common_hour=str(common_hour)+'am'
    else:
        common_hour=str(common_hour-12)+'pm'
    print('The most common hour is: {}'.format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('The most common start station is: {}'.format(common_start.title()))

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('The most common end station is: {}'.format(common_end.title()))

    # TO DO: display most frequent combination of start station and end station trip
    common_combination = df.groupby(['Start Station','End Station']).size().sort_values(ascending=False).head(1).reset_index()
    print('The most common combination is from {} to {}, with a count of {} occurrences.'.format(
    common_combination.iloc[0]['Start Station'], common_combination.iloc[0]['End Station'],common_combination.iloc[0,2]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    total_hours = int(total_time/3600)
    total_minutes = int((total_time - total_hours*3600)/60)
    total_seconds = (total_time - total_hours*3600 - total_minutes*60).round(2)
    print('The total travel time is: {:,} second(s), ie {:,} hour(s), {} minute(s) and {} second(s).'.format(total_time, total_hours, total_minutes, total_seconds))

    # TO DO: display mean travel time
    avg_time = df['Trip Duration'].mean().round(2)
    avg_minutes = int(avg_time/60)
    avg_seconds = (avg_time - avg_minutes*60).round(2)
    print('The average travel time is: {} second(s), ie {} minute(s) and {} second(s). '.format(avg_time, avg_minutes, avg_seconds))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    if user_types.size==2:
        print('There are in total {:,} {}(s) and {:,} {}(s).'.format(user_types.iloc[0], user_types.index[0],user_types.iloc[1], user_types.index[1]))
    else:
        print('There are in total {:,} {}(s), {:,} {}(s) and {} {}(s).'.format(user_types.iloc[0], user_types.index[0],user_types.iloc[1], user_types.index[1], user_types.iloc[2], user_types.index[2]))

    # TO DO: Display counts of gender
    if city!='washington':
        gender = df['Gender'].value_counts()
        print('There are in total {:,} {}(s) and {:,} {}(s).'.format(gender.iloc[0], gender.index[0],gender.iloc[1], gender.index[1]))
    # TO DO: Display earliest, most recent, and most common year of birth
    if city != 'washington':
        earliest_year = int(df['Birth Year'].min())
        most_recent = int(df['Birth Year'].max())
        most_common = int(df['Birth Year'].mode()[0])
        print('The earliest year of birth is {}, the most recent is {} and the most common is {}.'.format(earliest_year, most_recent, most_common))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    print('Hello! Let\'s explore some US bikeshare data!')

    while True:
        city, month, day = get_filters()

        #CHECK input is what user wanted
        print('\nOk, you would like to see data for {}, related to month: {} and day: {}.'.format(city.title(),month.title(),day.title()))
        check = input('Is that correct? Please write Yes or No: ').lower()
        while check not in ['yes','no']:
            check=input('Is that correct? Please write either Yes or No: ').lower()
        while check == 'no':
            print('\nOk, let\'s try again!\n\n')
            print('-'*40)
            city, month, day = get_filters()
            check = input('Is that correct? Please write Yes or No: ').lower()

        df = load_data(city, month, day)

        show_data(df)

        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        while restart not in ['yes','no']:
            restart = input('\nWould you like to restart? Please enter either yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
