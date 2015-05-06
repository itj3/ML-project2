import file_reader
import room
from model import infer_tau, update_heat
from output import plot_model, print_tau


def main():
    # load the data slice we want to use for determining tau
    temp_data = file_reader.read('new_temps.csv')
    print 'Data loading complete'
    # build a list of room objects
    rooms = []
    for x in temp_data:
        temp_room = room.Room(x)
        for y in temp_data[x]:
            temp_room.add_temp(y)
        rooms.append(temp_room)

    print 'Room construction complete'
    # for each room, calculate and print tau, and plot the resulting model
    # time step
    dt = 10
    for r in rooms:
        time_steps = []
        calculated_heat_values = []
        actual_heat_values = []
        # any given time value
        t = 0
        tau = infer_tau(r)

        for temp in r.temps:
            t += 10
            time_steps.append(t)
            heat = update_heat(dt, tau, temp[1], temp[2])
            calculated_heat_values.append(heat)
            actual_heat_values.append(temp[1])

        print_tau(r.room_num, tau)
        # IF MATPLOTLIB NOT INSTALLED, COMMENT OUT THIS LINE
        plot_model(r.room_num, time_steps, calculated_heat_values, actual_heat_values)


if __name__ == "__main__":
    main()