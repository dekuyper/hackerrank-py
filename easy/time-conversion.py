time = '04:45:54PM'


def time_conversion(time):
    time = time.split(':')

    if time[-1][-2:] == 'AM' and time[0] == '12':
    	time[0] = '00'
    if time[-1][-2:] == 'PM' and time[0] != '12':
    	time[0] = str(int(time[0]) + 12)

    return ':'.join(time)[:-2]


print(time_conversion(time))

