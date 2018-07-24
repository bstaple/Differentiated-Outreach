import webapp2
import models

class Profiles(ndb.Model):
	def __init__(self, Student, Hosts):
		self.name = name
		self.notes = ''


class Host(ndb.Model):
	def __init__(self, name, notes='', room_number = '0'):
		host_database = HostDatabase()
		self.name = name
		self.notes = ''
		host_database.name = name
		host_database.room_number = room_number
		host_database.host_message = notes

class Student(ndb.Model):
	def __init__(self, name, Host, notes=''):
		student_database = StudentDatabase()
		self.name = name
		self.notes = notes
		self.Host = Host.name
		student_database.notes = notes
		student_database.name = name
		student_database.corresponding_host = Host.name

class Room(ndb.Model):
	def __init__(self, host, name = 'Marco\'s room', students = [], number_of_students = len(students)):
		room_database = RoomDatabase()
		self.name = name
		self.host_user = host
		self.student_list = students
		room_database.room_name = name
		room_database.host_user = host
		room_database.number_of_users = number_of_students
		room_database.rooms.append(self)

class WaitRoom(ndb.Model):
	def __init__(self, host_owner, list_ofstudents = []):
		self.list_of_students


class ShowRoomsHandler(webapp2.RequestHandler):
	def dispatch(self):
		for room in room_database.rooms.query().fetch():
			self.response.out.write("<input type = 'button' value = 'Go to Room' action = '/room?roomName='" +room.name+
			"' />" + '<p>' +room.name + ' is owned by ' + room.host_user + '</p>')
			self.response.out.write('<br>')
		console.log("Rooms shown successfully.")



class CreateRoomHandler(webapp2.RequestHandler):
	def dispatch(self):
		self.response.out.write('This is working.')


app = webapp2.WSGIApplication([
('/', ShowRoomsHandler),
('/create', CreateRoomHandler),
('/room', SendToRoom),


], debug=True)
