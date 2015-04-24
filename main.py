import file_reader
import room

def main():
	temp_data = file_reader.read('temps.csv')
	rooms = []
	for x in temp_data:
		temp_room = room.Room(x)
		for y in temp_data[x]:
			temp_room.add_temp(y)
		rooms.append(temp_room)

	for x in rooms:
		print x.get_room_num()

if __name__ == "__main__":
	main()