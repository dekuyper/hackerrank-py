time = '04:59:59AM'

def time_conversion(time):
	time = time.split(':')
	time[0] = (str(int(time[0]) + 12), time[0])[time[-2:] == 'AM'] 
	time[0] = (time[0], '00')[time[0] == '24']
	print ':'.join(time)[:-2]

time_conversion(time)