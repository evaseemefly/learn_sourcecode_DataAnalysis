import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

months = ['january', 'february', 'march', 'april', 'may', 'june','all']

day_of_week = ['monday', 'tuesday', 'wednesday',
                   'thursday', 'friday', 'saturday', 'sunday','all']

def input_mod(input_print,error_print,enterable_list):
    
    # 将输入的input内容最小化
    ret=input(input_print).lower()
    # 判断输入的内容是否在可选范围内
    while ret not in enterable_list:
        # 若不在则需要重新输入
        ret=input(error_print).lower()
    return ret

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    让用户输入符合条件的城市、月份、以及星期
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # 为城市（芝加哥，纽约，华盛顿）获取用户输入。提示：使用while循环来处理无效输入

    city = ''

    
    # 方式1：
    # 现由方式2替代：
    # while True:
    #     print('请输入你要选择的城市：“chicago, new york city, washington”')
    #     input_city = input()
    #     city = input_city
    #     # 加入对城市的判断，若不在CITY_DATA中则重新输入
    #     if city in CITY_DATA.keys():
    #         print('你输入的城市信息有误，请重新输入')
    #     if input_city.lower() == 'chicago':
    #         break
    #     if input_city.lower() == 'new york city':
    #         break
    #     if input_city.lower() == 'washington':
    #         break
    
    # 方式2：
    city=input_mod('请输入你要选择的城市：“chicago, new york city, washington”','你输入的城市信息有误，请重新输入',CITY_DATA.keys())

    print('-'*40)

    # TO DO: get user input for month (all, january, february, ... , june)
    # 处理用户输入的月份
    month = ''
    
    # 方式1：由方式2替代
    # while True:
    #     print('请输入你要选择的月份：“all, january, february, ... , june”')
    #     month = input()
    #     if month in months:
    #         month = months.index(month)+1
    #         print('你输入的月份为：%s'%str(month))
    #         break
    #     else:
    #         print('您输入的有误，请重新输入')
            # break
    month=input_mod('请输入你要选择的月份：“all, january, february, ... , june”','您输入的有误，请重新输入',months)
    print('-'*40)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    # 处理用户输入的日
    dayOfWeek = ''
    
    # 方式1：由方式2替代
    # while True:
    #     print('你要选择星期几：“monday,tuesday,wednesday,thursday,friday,saturday,sunday”')
    #     input_day = input()
    #     dayOfWeek = input_day
    #     if input_day in day_of_week:
    #         dayOfWeek = day_of_week.index(input_day)+1
    #         print('你输入的为星期：%s' % str(dayOfWeek))
    #         break
    #     else:
    #         print('您输入的有误，请重新输入')
    dayOfWeek=input_mod('你要选择星期几：“monday,tuesday,wednesday,thursday,friday,saturday,sunday”','您输入的有误，请重新输入',day_of_week)
    print('-'*40)
    return city, month, dayOfWeek


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
    # 取出指定城市对应的文件名称
    # CITY_DATA = {'chicago': 'chicago.csv',
    #              'new york city': 'new_york_city.csv',
    #              'washington': 'washington.csv'}
    city_data_filename = CITY_DATA[city]
    # 读取指定路径的文件
    df = pd.read_csv(city_data_filename)
    # 对数据进行筛选
    # 需要删选的条件有：
    #   月份
    #   一周中的某天

    # 修改Start Time为时间戳格式
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    ts = df['Start Time'].dt
    # 月份的计数是从1开始
    df['month'] = ts.month
    # weekday的计数是从0开始（即0代表星期1）
    df['day_of_week'] = ts.weekday+1
    # 注意还需要为df添加一个hours列，hour的计数是从1开始
    df['hours'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'all':
            # use the index of the months list to get the corresponding int
        # 使用月份列表的索引来获得相应的整数
        # months = ['january', 'february', 'march', 'april', 'may', 'june']
        # index_month = months.index(month)+1
        index_month = months.index(month)+1
#         month = months[ts.month]

        # filter by month to create the new dataframe
#         df =
        df = df[df['month'] == index_month]
    # elif month=='all':

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        # dayofweek = ['monday', 'tuesday', 'wednesday',
        #              'thursday', 'friday', 'saturday', 'sunday']
        # index_weekday = dayofweek.index(day)+1
        index_weekday = day_of_week.index(day)+1
        df = df[df['day_of_week'] == index_weekday]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel.
        显示最频繁的旅行时间的统计数据
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # 使用df.mode()的方式获取众数（出现频率最高的）
    # TO DO: display the most common month
    popular_month = df['month'].mode()
    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()

    # TO DO: display the most common start hour
    popular_hour = df['hours'].mode()

    print('month的众数为:%s' % popular_month)
    print('day_of_week的众数为:%s' % popular_day_of_week)
    print('hour的众数为:%s' % popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """
        Displays statistics on the most popular stations and trip.
        显示最热门的站点及旅程的统计
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()


    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()
    print('起始站的众数为:%s' % popular_start)
    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()
    print('结束站的众数为:%s' % popular_end)
    # TO DO: display most frequent combination of start station and end station trip
    # 显示最频繁的起始站和结束站的组合
    # popular_group_startEnd=df[['Start Station','End Station']].mode()
    popular_group_startEnd = df['Start Station'] + ' to ' + df['End Station']
    print('起始结束站的众数为:%s' % popular_group_startEnd.mode())
    
    # popular_start = df['Start Station'].mode()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """
        Displays statistics on the total and average trip duration.
        显示总体和平均旅行持续时间的统计数据（Trip Duration）
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    # 计算总的旅行时长
    travel_totals=df['Trip Duration'].sum()
    print('总的旅行时长%s'%str(travel_totals))
    # TO DO: display mean travel time
    # 计算旅行的平均值
    travel_mean = df['Trip Duration'].mean()
    print('旅行时长平均值%s' % str(travel_mean))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())
    # TO DO: Display counts of gender
    try:
        print(df['Gender'].value_counts())
    except:
        print("没有gender数据")

    # TO DO: Display earliest, most recent, and most common year of birth
    # 最早的，最近的，出现最多的
    # 1 最早的
    try:
        early=df.sort_values(by=['Birth Year'])[:1]
        print('出现最早的出生年份为：%s'%str(early['Birth Year']))

        # 2 最近的
        last=df.sort_values(by=['Birth Year'],ascending=False)[:1]
        print('距离现在最近的出生年份为：%s' % str(last['Birth Year']))
        # 3 出现次数最多的
        counts = df['Birth Year'].value_counts()
        most=counts.index[0]
        print('出现次数最多的出生年份为：%s' % str(most))
    except:
        print('并没有生日这一列数据')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
