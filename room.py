from datetime import datetime as dt

class Room():
	def __init__(self, room_num):
		self.room_num = room_num # room number
		self.window_sa = 0 # surface area of window space

		self.temps = [] # 2D list containing temperatures and time EX: [[datetime object,65], [datetime object,66]]

	def get_room_num(self):
		return self.room_num

	def get_window_sa(self):
		return self.window_sa

	def get_temps(self, date): #date is a datetime object 
		return self.temps

	def add_temp(self, data):
		self.temps.append(data)

	def set_SA(self, SA):
		self.window_SA = SA

