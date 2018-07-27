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
	questions = ndb.StringProperty(repeated = True)
	note_pad = ndb.StringProperty(repeated = True)

class Room(ndb.Model):

		chat_messages = ndb.StringProperty(repeated = True)
		host = ndb.StringProperty()
		name = ndb.StringProperty(default = 'Marco')
		question_list = ndb.StringProperty(repeated = True)
		host_notes = ndb.StringProperty(repeated = True)


class WaitRoom(ndb.Model):
	host_owner = ndb.StringProperty(default = 'Marco')
	list_ofstudents = ndb.StringProperty(repeated = True)


class LoginPageHandler(webapp2.RequestHandler):
	def get(self):
		logIn_template = jinja_env.get_template('Templates/loginFancy.html')
		self.response.write(logIn_template.render())

	def post(self):
		username = self.request.get("username")
		password = self.request.get("password")
		user_type = self.request.get('hostORstudent')

		if user_type == 'students':
			new_Student = Student(name = username)
			accounts = Account(username = username,password = password,user_type = user_type)
			accounts.put()
			new_Student.put()
			print "Student Key" + str(new_Student.key.id())
			self.redirect('/?name=' + self.request.get("username") + '&hostORstudent=' + self.request.get("hostORstudent")+"&studentKey="+str(new_Student.key.id()))
		else:
			accounts = Account(username = username,password = password,user_type = user_type)
			accounts.put()
			self.redirect('/?name=' + self.request.get("username") + '&hostORstudent=' + self.request.get("hostORstudent"))




class MainHandler(webapp2.RequestHandler):
	def get(self):
		print("Rooms shown successfully.")
		print "This is the key" + self.request.get("studentKey")
		result_template = jinja_env.get_template('Templates/rooms.html')
		rooms = Room.query().fetch()
		if self.request.get('hostORstudent') == 'students':
			student_id = self.request.get("studentKey")
			student_key = ndb.Key('Student', int(student_id))
			q = student_key.get()
		result_dictionary = {
		'rooms' : rooms,
		'student' :  self.request.get('studentKey'),
		'hostORstudent' : self.request.get("hostORstudent"),
		'name' : self.request.get("name"),
		}
		self.response.out.write(result_template.render(result_dictionary))

class SendToRoom(webapp2.RequestHandler):
	def get(self):
		if self.request.get('hostORstudent') == 'host':
			type = self.request.get("hostORstudent")
			host_content = jinja_env.get_template('Templates/host.html')
			id = self.request.get('key')
			key = ndb.Key('Room', int(id))
			m = key.get()
			messages = m.chat_messages
			questions = m.question_list
			print messages
			# messages.append(str(message))
			print ["Messages : "] + messages

			# message = self.request.get('chat_messages')
			# messages.append(message)


			output_variables = {
			'messages': messages,
			'name' : self.request.get("name"),
			'question_list' : questions,
			}
			print ["This is what should come out"] + messages
			self.response.out.write(host_content.render(output_variables))
		else:
			student_content = jinja_env.get_template('Templates/student.html')
			id = self.request.get('key')
			key = ndb.Key('Room', int(id))
			m = key.get()
			messages = m.chat_messages
			student_id = self.request.get("studentKey")
			print "Student ID" + student_id
			student_key = ndb.Key('Student', int(student_id))
			q = student_key.get()
			student_questions = q.questions
			print messages
			# messages.append(str(message))
			print ["Messages : "] + messages
			student_notes = q.note_pad

			output_variables = {
			'messages': messages,
			'name' : self.request.get("name"),
			'questions' : student_questions,
			'notes' : student_notes
			}
			print ["This is what should come out"] + messages
			self.response.out.write(student_content.render(output_variables))

	def post(self):
		  print "I'm in the post"
		  id = self.request.get('key')
		  question = self.request.get('student_question')
		  note = self.request.get("note_input")
		  print "Everything under this is what we want"
		  print id
		  print self.request
		  key = ndb.Key('Room', int(id))
		   #ndb.Key(urlsafe=rkey)
		  m = key.get()
		  print m
		  input = m.chat_messages
		  questions = m.question_list
		  print input
		  input.append(self.request.get('chat_message'))

		  print "After append: "
		  print input
		  # if self.request.get("hostORstudent") == 'host':
			#   questions.append(self.request.get("name") + " asked : " + question)
		  #
			#   m.put()
		  if self.request.get("hostORstudent") == 'students':

			  questions.append(self.request.get("name") + " asked : " + question)
			  m.put()
			  student_id = self.request.get("studentKey")
			  student_key = ndb.Key('Student', int(student_id))
			  q = student_key.get()
			  student_questions = q.questions
			  student_notes = q.note_pad
			  student_questions.append(question)
			  student_notes.append(note)
			  q.put()
		  m.put()
		  self.get()






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
