# This module contains functions for printing to console and writing to files
# print_tau(...) Formats and prints the tau and associated room
# plot_model(...) Plots the models calculated temperature values against the actual

from matplotlib import pyplot as p
from matplotlib import patches


def print_tau(room_num, tau):
    """
    Formats and prints the tau and associated room
    :param room_num: string - room number
    :param tau: tau value for model
    :return:
    """
    print '-----------------------'
    print 'Node: %s,| Tau: %d' % (room_num, tau)
    print '-----------------------'


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
    p.savefig('plot%s.png' % room_num)