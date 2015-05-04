# from pylab import plot,ylabel, xlabel, yticks, xticks
import matplotlib.pyplot as plt
import csv
import datetime
import matplotlib.cbook as cbook
import file_reader
import room
from model import *

temp_data = file_reader.read('night.csv')
date = []
outTemp = []
inTemp = []

rooms = []
for x in temp_data:
    temp_room = room.Room(x)
    for y in temp_data[x]:
        temp_room.add_temp(y)
    rooms.append(temp_room)


start= datetime.datetime(2015,4,10,22,00)
end = datetime.datetime(2015,4,11,7,0)
timeFrame = end-start
zero = datetime.timedelta(0)
labels = {}
labels['7'] = 'm.'
labels['9'] = 'b.'
labels['10'] = 'r.'
labels['17'] = 'c.'
labels['18'] = 'g.'
labels['19'] = 'k.'
i=10
try:
    for r in rooms:
        if r.room_num == '10':
            temp = r

    for y in temp_data[str(i)]:
        if ( end - y[0]<= timeFrame and  (end - y[0])>=zero):
            date.append(y[0])
            inTemp.append(y[1])
            outTemp.append(y[2])
except KeyError:
    pass
# print infer_vars(temp)
tau = all_tau(temp)
a, =plt.plot(date,inTemp, "b.", label='Sensor 10/Rm #164 Temp')
b, =plt.plot(date, outTemp, "m.", label="Outside Temp")

# plt.legend()

plt.ylabel("Temperature ($^\circ$C)")
plt.xlabel("4/10 to 4/11")
plt.xticks(rotation='45')
plt.gca().add_artist(plt.legend(handles=[a], loc=1))
plt.legend(handles=[b], loc=4)
plt.title("Temperature Vs. Time", fontsize=20)
plt.tight_layout()
plt.savefig('TempVsTime.png')
plt.cla()

b, = plt.plot(tau[1],tau[0], "k.", label="Tau")
plt.ylabel("Tau")
plt.xlabel("4/10 to 4/11")
plt.xticks(rotation='45')

plt.legend(handles=[b], loc=2)
plt.title("Tau Vs. Time", fontsize=20)
plt.tight_layout()
plt.savefig('Temp_Tau.png')

plt.show()