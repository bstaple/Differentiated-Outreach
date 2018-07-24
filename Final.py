import webapp2



class Pages(object):
	def __init__(self, Student, Host):
		self.Student= Student
		self.Host = Host


class Host(object):
	def __init__(self, name, notes=''):
		self.name = name
		self.notes = notes

class Student(object):
	def __init__(self, name, Host, notes=''):
		self.name = name
		self.notes = notes
		self.Host = Host

class Room(object):
	def __init__(self, name, host, students):
		self.name = name
		self.host_user = host
		self.student_list = students

rooms = [
	Room('Room 1', 'host1', 'Jimmy'),
	Room('Room 2', 'host2', 'Carl'),
	Room('Room 3', 'host3', 'Jack, Sally and John')
]

class ShowRoomsHandler(webapp2.RequestHandler):
	def dispatch(self):
		for room in rooms:
			self.response.out.write(room.name + ' is owned by ' + room.host_user + ' students are: ' + room.student_list)
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
