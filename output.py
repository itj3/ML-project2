# This module contains functions for printing to console and writing to files
# print_tau(...) Formats and prints the tau and associated room
# plot_model(...) Plots the models calculated temperature values against the actual

from matplotlib import pyplot as p
from matplotlib import patches
from model import get_b_tau


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


def plot_model(room_num, time, calculated, actual):
    """
    plots heat vs time for both the actual data, as well as the calculated heat from our model and saves it to
    file name plot<room_num>.png
    :param time: list of time values
    :param calculated: list of calculated heat values
    :param actual: list of actual heat values
    :return:
    """
    p.cla()
    p.plot(time, calculated, 'b.')
    p.plot(time, actual, 'r.')
    model = patches.Patch(color='blue', label='Model')
    measured = patches.Patch(color='red', label='Measured')
    p.legend([model, measured], ['Model', 'Measured'])
    p.xlabel('Time elapsed (s)')
    p.ylabel('Heat (T(t +dt))')
    p.title('Heat over Time for sensor ' + room_num)
    p.savefig('plot%s.png' % room_num)