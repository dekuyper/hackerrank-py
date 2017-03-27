time = '12:45:54PM'

def time_conversion(time):
	time = time.split(':')
	time[0] = (str(int(time[0]) + 12), time[0])[time[-1][-2:] == 'AM']
	print(time)
	time[0] = (time[0], '00')[time[0] == '24' or (time[0] == '12' and time[-1][-2:] == 'AM')]
	print ':'.join(time)[:-2]


time_conversion(time)
