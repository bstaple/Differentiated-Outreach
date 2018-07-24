import webapp2
import models

class Profiles(object):
	def __init__(self, Student, Hosts):
		self.name = name
		self.notes = ''


class Host(object):
	def __init__(self, name, notes='', room_number = '0'):
		host_database = HostDatabase()
		self.name = name
		self.notes = ''
		host_database.name = name
		host_database.room_number = room_number
		host_database.host_message = notes

class Student(object):
	def __init__(self, name, Host, notes=''):
		student_database = StudentDatabase()
		self.name = name
		self.notes = notes
		self.Host = Host.name
		student_database.notes = notes
		student_database.name = name
		student_database.corresponding_host = Host.name

class Room(object):
	def __init__(self, name, host, students, number_of_students = len(students)):
		room_database = RoomDatabase()
		self.name = name
		self.host_user = host.name
		self.student_list = students
		room_database.room_name = name
		room_database.host_user = host.name
		room_database.number_of_users = number_of_students
		room_database.rooms.append(self)

class WaitRoom(Object):
	def __init__(self,list_ofstudents = [], host_owner):



class ShowRoomsHandler(webapp2.RequestHandler):
	def dispatch(self):
		for room in rooms:
			self.response.out.write(room.name + ' is owned by ' + room.host_user + ' ' + room.student_list)
			self.response.out.write('<br>')



class CreateRoomHandler(webapp2.RequestHandler):
	def dispatch(self):
		# for Room in rooms:
		# 	if Room not in rooms:
		# 		rooms.append('Room 4', 'User 4')
		self.response.out.write('This is working.')


app = webapp2.WSGIApplication([
('/', ShowRoomsHandler),
('/create', CreateRoomHandler)


], debug=True)
