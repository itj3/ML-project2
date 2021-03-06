import csv
import datetime

def read(file_name):
    return_dict = {}
    with open(file_name, 'r') as csv_file:
        count = []
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
            # start of the time we want to look at data
            start = datetime.datetime(2015, 4, 10, 22, 0, 0)
            # end of the time we want to look at data
            end = datetime.datetime(2015, 4, 11, 7, 0, 0)
            if start <= dt <= end:
            #add new value to the dictionary
                if name not in count:
                    return_dict[name] = []
                    count.append(name)
                # remove data without out any associated outside temp since no calculations can be done without it
                if row_list[4] != 'n/a':
                    return_dict[name].append([dt, float(row_list[3]), float(row_list[4])])
    return return_dict