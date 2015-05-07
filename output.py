# This module contains functions for printing to console and writing to files
# print_tau(...) Formats and prints the tau and associated room
# plot_model(...) Plots the models calculated temperature values against the actual

from matplotlib import pyplot as p
from matplotlib import patches
from model import get_b_tau
import datetime
rooms ={}
rooms['1'] = '211'
rooms['2'] = '222'
rooms['12'] = '216'
rooms['15'] = '222'
rooms['18'] = '203'
rooms['6'] = '212'
rooms['4']  = '162'
rooms['8'] = '162'
rooms['13'] = '146'
rooms['16'] = '176'
rooms['10'] = '164'
rooms['19'] = '170'
rooms['9'] = '141'
rooms['3'] = '137A'
rooms['14'] = '137'
rooms['5'] = '132'
rooms['11'] = '121'
rooms['7'] = '125'
rooms['17'] = '123'


def print_tau(room_num, tau):
    """
    Formats and prints the tau and associated room
    :param room_num: string - room number
    :param tau: tau value for model
    :return:
    """
    print '-----------------------'
    if int(room_num) < 10:
        print 'Node: 0%s, | Tau: %d' % (room_num, tau)
    else:
        print 'Node: %s, | Tau: %d' % (room_num, tau)
    print '-----------------------'

def print_b_tau(rooms):
    """
    Formats and prints the tau of the building
    :param rooms: list of room objects
    :return:
    """
    print '-----------------------'
    print 'Building  | Tau: %d' % (get_b_tau(rooms))


def plot_model(room_num, time, calculated, actual, start, end):
    """
    plots heat vs time for both the actual data, as well as the calculated heat from our model and saves it to
    file name plot<room_num>.png
    :param time: list of time values
    :param calculated: list of calculated heat values
    :param actual: list of actual heat values
    :return:
    """
    sens_num = rooms[str(room_num)]
    p.cla()
    p.plot(time, calculated, 'b.')
    p.plot(time, actual, 'r.')
    model = patches.Patch(color='blue', label='Model')
    measured = patches.Patch(color='red', label='Measured')
    p.legend([model, measured], ['Model', 'Measured'])
    p.xticks(rotation=45)
    p.xlabel('%s/%s to %s/%s' % (start.month,start.day,end.month,end.day))
    p.ylabel('Heat (T(t +dt))')
    p.title("Data and Model Comparison Room %s Sensor %s" %(sens_num, room_num))
    p.tight_layout()
    p.savefig('plot%s.png' % room_num)