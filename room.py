from datetime import datetime as dt

class room():
	def __init__(self, room_num, window_sa, temps):
		self.room_num = room_num    # room number
		self.window_sa = window_sa     # surface area of window space

		#kind of need the data to set this...
		self.temps = [] # 2D list containing temperatures and time EX: [[datetime object,65], [datetime object,66]]

	def get_room_num(self):
		return self.room_num

	def get_window_sa(self):
		return self.window_sa

	def get_temp(self, date): #date is a datetime object 
		for temp in self.temps:
			d = temp[0]
			if d == date:
				return temp[1]
		return -1

