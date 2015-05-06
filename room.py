from datetime import datetime as dt

class Room():
	def __init__(self, room_num):
		self.room_num = room_num # acctually is the node number
		self.temps = [] # 2D list containing temperatures and time EX: [[datetime object, inside temp, outside temp], [datetime object,66,34]]

	def get_temps(self, date): #date is a datetime object 
		return self.temps

	def add_temp(self, data):
		self.temps.append(data)

