from google.appengine.ext import ndb
from google.appengine.api import users
from google.appengine.api import memcache
import json
import webapp2
import os
import jinja2

JINJA_ENV = jinja2.Environment(
	loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions=['jinja2.ext.autoescape'],
	autoescape=True
)


class Account(ndb.Model):
	username = ndb.StringProperty()
	password = ndb.StringProperty()
	user_type = ndb.StringProperty()

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


class LoginPageHandler(webapp2.RequestHandler):
	def dispatch(self):
		logIn_template = JINJA_ENV.get_template('Templates/login.html')
		self.response.write(logIn_template.render())
	def post(self):
		user = self.request.get("username")
		passw = self.request.get("password")
		type = self.request.get('hostORstudent')
		accounts = Account(user,passw,type)
		self.response.write(user)


result_template = JINJA_ENV.get_template('Templates/rooms.html')

class ShowRoomsHandler(webapp2.RequestHandler):
	def dispatch(self):
			result_template = JINJA_ENV.get_template('Templates/rooms.html')
			rooms = Room.query().fetch()
			result_dictionary = {
			'rooms' : rooms,
			}
			print("Rooms shown successfully.")
			self.response.out.write(result_template.render(result_dictionary))

# class SendToRoom(webapp2.RequestHandler):
# 	def get(self):
# 		content = JINJA_ENV.get_template('Differentiated-Outreach/host.html')
# 		self.response.out.write(content)

class CreateRoomHandler(webapp2.RequestHandler):
	def dispatch(self):
		# for Room in rooms:
		# 	if Room not in rooms:
		# 		rooms.append('Room 4', 'User 4')

		new_room = Room(host = self.request.get("name"))
		new_room.put()
		Create_dictionary = {
		'name' : new_room.host,
		}
		print 'Room added'
		self.response.out.write(result_template.render(Create_dictionary))
		self.redirect('/')
		self.response.out.write('This is working.')


print('done')
app = webapp2.WSGIApplication([
('/login', LoginPageHandler),
('/', ShowRoomsHandler),
('/create', CreateRoomHandler),
# ('/room', SendToRoom),


], debug=True)
