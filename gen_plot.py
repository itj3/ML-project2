# from pylab import plot,ylabel, xlabel, yticks, xticks
import matplotlib.pyplot as plt
import csv
import datetime
import matplotlib.cbook as cbook
import file_reader
import room
from model import *

temp_data = file_reader.read('night.csv')
rooms = []

for x in temp_data:
    temp_room = room.Room(x)
    for y in temp_data[x]:
        temp_room.add_temp(y)
    rooms.append(temp_room)

start= datetime.datetime(2015,4,10,22,00)
end = datetime.datetime(2015,4,11,7,30)
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

datetime.datetime(2015,4,11,1,13)
try:
    for r in rooms:
        date =[]
        inTemp = []
        outTemp =[]
        line = labels[str(r.room_num)]
        for y in r.temps:
            if ( end - y[0]<= timeFrame and  (end - y[0])>=zero):
                date.append(y[0])
                inTemp.append(y[1])
                outTemp.append(y[2])
        plt.plot(date,inTemp, "%s"%(line), label="Sensor #%s" %(r.room_num))
except KeyError:
    pass
plt.ylabel("Temperature ($^\circ$C)")
plt.xlabel("4/10 to 4/11")
plt.xticks(rotation='45')
plt.title("Temperature Vs. Time", fontsize=20)

plt.xlabel("4/10 to 4/11")
plt.legend(loc=8, handletextpad=0,handlelength=0.5,columnspacing=0.5,numpoints=1,fancybox=True, ncol=6,fontsize=10)
plt.tight_layout()
plt.savefig('All_Sens.png')

plt.show()
