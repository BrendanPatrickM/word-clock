week = {
    'mo' : 'Monday',
    'tu' : 'Tuesday',
    'we' : 'Wednesday',
    'th': 'Thursday',
    'fr' : 'Friday',
    'sa' : 'Saturday',
    'su': 'Sunday',
}
numbers ={
    13 :'Midnight',
    1 :'One',
    2 :'Two',
    3 :'Three',
    4 :'Four',
    5 :'Five',
    6 :'Six',
    7 :'Seven',
    8 :'Eight',
    9 :'Nine',
    10 :'Ten',
    11 :'Eleven',
    12 :'Twelve',
}

from time import time, ctime
current_time = (ctime(time()))

def get_time(time_str):
    hour = int(time_str[11]+time_str[12])
    if hour == 00:
        hour = 13
    elif hour > 12:
        hour-=12
    i = int(time_str[14]+time_str[15])
    if i > 45:
        hour += 1
    if i < 5 :
        minutes = 'o clock'
    elif i < 10:
        minutes = 'five minutes past'
    elif i < 20:
        minutes = 'quarter past'
    elif i < 25:
        minutes = 'twenty minutes past'
    elif i < 30:
        minutes = 'tewntyfive minutes past'
    elif i < 35:
        minutes = 'half past'
    elif i <40:
        minutes = 'twentyfive minutes to'
    elif i <45:
        minutes ='twenty minutes to'
    elif i <50:
        minutes =  ' quarter to'
    elif i <55:
        minutes = 'ten to'
    elif i <60:
        minutes ='five to'
    return minutes, numbers[hour]

minutes = (get_time(current_time)[0])
hour = (get_time(current_time)[1])

if minutes == 'o clock':
    print(f"It is {hour} {minutes}")
else:
    print(f"It is {minutes} {hour}")
