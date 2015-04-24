import csv
import datetime

def read(file_name):
	return_list = []
	with open(file_name, 'rb') as csv_file:
		spamreader = csv.reader(csv_file, delimiter=' ', quotechar='|')
		for row in spamreader:
			#put row into a list
			row_list = [x for x in row[0].split(',')]
			#bunch of BS to get the node number from the stupidly long name
			name_list = row_list[0].split('/')     
			name = name_list[1].split('_')[1]
			#put date and time into a datetime object
			date_list = row_list[1].split('/')
			time_list = row_list[2].split(':')
			month  = int(date_list[0])
			day    = int(date_list[1])
			year   = int(date_list[2])
			hour   = int(time_list[0])
			minute = int(time_list[1])
			second = int(time_list[2])
			dt     = datetime.datetime(year, month, day, hour, minute, second)
			return_list.append([name, dt, row_list[3]])
	return return_list