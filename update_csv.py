import csv
import datetime

def read(file_name):
	return_list = []
	with open(file_name, 'rb') as csv_file:
		spamreader = csv.reader(csv_file, delimiter=' ', quotechar='|')
		for row in spamreader:
			#put row into a list
			row_list = [x for x in row[0].split(',')]   
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
			#add new value to the dictionary
			return_list.append([dt, row_list[3]])
	return return_list


def update(file_name):
	count = 0
	outside_temps = read('ArbTempDataset.csv')
	csvfile = file_name
	output = []
	with open(csvfile, 'r') as fin, open('new_'+csvfile, 'wb') as fout:
		reader = csv.reader(fin, delimiter=' ', quotechar='|')
		writer = csv.writer(fout, delimiter=' ', quotechar='|')
		for row in reader:
			row_list = [x for x in row[0].split(',')]
			date_list = row_list[1].split('/')
			time_list = row_list[2].split(':')
			month  = int(date_list[0])
			day    = int(date_list[1])
			hour   = int(time_list[0])
			minute = int(time_list[1])
			data   = ',n/a'
			for x in outside_temps:
				dt = x[0]
				if dt.month == month and dt.day == day and dt.hour == hour and dt.minute == minute:
					data = ','+ x[1]
					break
			temp = row[0] + data
			output.append([temp])
			print count
			count+=1
		writer.writerows(output)