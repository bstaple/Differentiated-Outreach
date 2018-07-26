from google.appengine.ext import ndb
from google.appengine.api import users
from google.appengine.api import memcache
import json
import webapp2
import json
import jinja2
import os
import datetime
import random

jinja_env = jinja2.Environment(
	loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions=['jinja2.ext.autoescape'],
	autoescape=True
)

class UserInfo(ndb.Model):
	name = ndb.StringProperty()

class HostPageHandler(webapp2.RequestHandler):
  def get(self):
    template = jinja_env.get_template('Templates/host.html')
    self.response.write(template.render())



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

		chat_messages = ndb.StringProperty(repeated = True)
		host = ndb.StringProperty()
		name = ndb.StringProperty(default = 'Marco')
		student_list = ndb.StringProperty(repeated = True)
		host_notes = ndb.StringProperty(repeated = True)
		def to_summary_dict(self):
			return{
	      # "key" is a property we get from ndb.Model - we can use this for easy retrieval of 1 specfic Model
	        'key': self.key.urlsafe(),
	        'title': self.title,
	        'author': self.author
	    }
		chat_messages = ndb.StringProperty(repeated = True)
		host = ndb.StringProperty()
		name = ndb.StringProperty(default = 'Marco')
		student_list = ndb.StringProperty(repeated = True)
		host_notes = ndb.StringProperty(repeated = True)
		def to_summary_dict(self):
			return {
	# "key" is a property we get from ndb.Model - we can use this for easy retrieval of 1 specfic Model
			'key': self.key.urlsafe(),
			'title': self.title,
			'author': self.author
		}


class WaitRoom(ndb.Model):
	host_owner = ndb.StringProperty(default = 'Marco')
	list_ofstudents = ndb.StringProperty(repeated = True)


class LoginPageHandler(webapp2.RequestHandler):
	def get(self):
		logIn_template = jinja_env.get_template('Templates/login.html')
		self.response.write(logIn_template.render())

	def post(self):
		username = self.request.get("username")
		password = self.request.get("password")
		user_type = self.request.get('hostORstudent')
		accounts = Account(username = username,password = password,user_type = user_type)
		accounts.put()
		self.redirect('/?name=' + self.request.get("username") + '&hostORstudent=' + self.request.get("hostORstudent"))


result_template = jinja_env.get_template('Templates/rooms.html')

class ShowRoomsHandler(webapp2.RequestHandler):
	def dispatch(self):

		# for room in Room.query().fetch():
		# 	print room.name
		# 	self.response.out.write("<input type = 'button' value = 'Go to %s room' action ='/room?roomName=%s />" % (room.host, room.name))
		# 	self.response.out.write('<br>')
		print("Rooms shown successfully.")

		result_template = jinja_env.get_template('Templates/rooms.html')
		rooms = Room.query().fetch()
		result_dictionary = {
		'rooms' : rooms,
		}
		self.reponse.out.write(result_template.render(result_dictionary))

class MainHandler(webapp2.RequestHandler):
	def get(self):
		result_template = jinja_env.get_template('Templates/rooms.html')
		rooms = Room.query().fetch()
		result_dictionary = {
		'rooms' : rooms,
		'name' : self.request.get('name'),
		'hostORstudent' : self.request.get('hostORstudent')
		}
		print("Rooms shown successfully.")
		self.response.out.write(result_template.render(result_dictionary))

class SendToRoom(webapp2.RequestHandler):
	def get(self):
		type = self.request.get("hostORstudent")
		host_content = jinja_env.get_template('Templates/host.html')

		messages = Room.query().filter(name= self.request.get("Room_name"))

		messages = Room.query().filter(name=self.request.get("Room_name"))


		output_variables = {
		'messages': messages,
		'name' : self.request.get("name")
		}
		self.response.out.write(host_content.render(output_variables))
		print messages

		# for message in messages:
		# 	self.response.out.write(''' %s : %s ''' % (self.request.get("name"),message.chat_messages))

	def post(self):
		rkey = self.request.get('key')

      # construct an ndb.Key object

	  	key = ndb.Key(urlsafe=rkey)
	  	if key:
    # use the ndb.Key object's get() method to retrieve the Model associated with that particular key
			m = key.get()
			room_query_object.put()

			key = ndb.Key(urlsafe=rkey)
		if key:
        # use the ndb.Key object's get() method to retrieve the Model associated with that particular key
			m = key.get()
			room_query_object.put()

			if self.request.get("hostORstudent") == 'host':
				content = jinja_env.get_template('Templates/host.html')
				self.response.out.write(content.render())
				self.redirect('/room')

class CreateRoomHandler(webapp2.RequestHandler):
	def post(self):
		if self.request.get('hostORstudent') == 'host':
			new_room = Room(host = self.request.get("name"), name = self.request.get("Room_name"))
			new_room.put()
			self.response.out.write(new_room)
			self.redirect('/?name=' + self.request.get("name") + '&hostORstudent=' + self.request.get('hostORstudent') + "&roomName=" + self.request.get("Room_name"))
		else:
			self.redirect('/?name=' + self.request.get("name") + '&hostORstudent=' + self.request.get('hostORstudent'))
class GetRoomsHandler(webapp2.RequestHandler):
	def get(self):
		self.refresh()

		# self.redirect('/create?name=' + self.request.get("name"))
		# print 'Room added'
		# self.response.out.write(result_template.render(Create_dictionary))
		# print 'hey whats up'
		# self.redirect('/')
	# def post(self):
	# 	new_room = Room(host = self.request.get("name"))
	# 	new_room.put()


print('done')
app = webapp2.WSGIApplication([
('/login', LoginPageHandler),
('/', MainHandler),
('/create', CreateRoomHandler),
('/room', SendToRoom),
('/hostpage', HostPageHandler),
('/getRoom', GetRoomsHandler),



], debug=True)
