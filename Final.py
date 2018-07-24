from google.appengine.ext import ndb
import webapp2
# import jinja2
# import os
#
# JINJA_ENV = jinja2.Environment(
# 	loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
# 	extensions=['jinja2.ext.autoescape'],
# 	autoescape=True
# )

# class Profiles(ndb.Model):
# 		self.name = name
# 		self.notes = ''

class Host(ndb.Model):
	name = ndb.StringProperty()
	notes = ndb.StringProperty(repeated = True)
	room_number = ndb.IntegerProperty(default = 0)

class Student(ndb.Model):
	name = ndb.StringProperty()
	notes = ndb.BlobProperty(repeated = True)
	Host = ndb.StringProperty()

class Room(ndb.Model):
		host = ndb.StringProperty()
		name = ndb.StringProperty(default = 'Marco')
		student_list = ndb.StringProperty(repeated = True)


class WaitRoom(ndb.Model):
	host_owner = ndb.StringProperty(default = 'Marco')
	list_ofstudents = ndb.StringProperty(repeated = True)


class ShowRoomsHandler(webapp2.RequestHandler):
	def dispatch(self):
		for room in Room.query().fetch():
			print room.name
			self.response.out.write("<input type = 'button' value = 'Go to %s room' action ='/room?roomName=%s />" % (room.host, room.name))
			self.response.out.write('<br>')
		print("Rooms shown successfully.")

# class SendToRoom(webapp2.RequestHandler):
# 	def get(self):
# 		content = JINJA_ENV.get_template('Differentiated-Outreach/host.html')
# 		self.response.out.write(content)

class CreateRoomHandler(webapp2.RequestHandler):
	def dispatch(self):
		# for Room in rooms:
		# 	if Room not in rooms:
		# 		rooms.append('Room 4', 'User 4')

		new_room = Room(host = self.request.get("hostName"))
		new_room.put()
		print 'Room added'
		self.redirect('/')
		self.response.out.write('This is working.')


print('done')
app = webapp2.WSGIApplication([
('/', ShowRoomsHandler),
('/create', CreateRoomHandler),
# ('/room', SendToRoom),


], debug=True)
