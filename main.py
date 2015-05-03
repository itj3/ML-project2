import file_reader
import room
from model import *
from matplotlib import pyplot


def main():
    temp_data = file_reader.read('new_temps.csv')
    print 'Data loading complete'
    rooms = []
    for x in temp_data:
        temp_room = room.Room(x)
        for y in temp_data[x]:
            temp_room.add_temp(y)
        rooms.append(temp_room)

    print 'Room construction complete'

    for r in rooms:
        t = []
        y = []
        x = 0
        for temp in r.temps:
            x += 10
            t.append(x)
            tau, e = infer_vars(r)
            heat = update_heat(10,tau,e,temp[1],temp[2])
            y.append(heat)
        pyplot.plot(t, y,'b.')
        pyplot.savefig('plot%s.png' % r.room_num)
        print 'Finsihed plot %s' % r.room_num
        pyplot.cla()

if __name__ == "__main__":
    main()