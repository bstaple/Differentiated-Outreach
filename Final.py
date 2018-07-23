import webapp2

class Room(object):
	def __init__(self, name, user):
		self.name = name
		self.host_user = user

rooms = [
	Room('Room 1', 'user1'),
	Room('Room 2', 'user2'),
	Room('Room 3', 'user1')
]

class ShowRoomsHandler(webapp2.RequestHandler):
	def dispatch(self):
		for room in rooms:
			self.response.out.write(room.name + ' is owned by ' + room.host_user)
			self.response.out.write('<br>')


class CreateRoomHandler(webapp2.RequestHandler):
	def dispatch(self):
		self.response.out.write('This is working.')


app = webapp2.WSGIApplication([
('/', ShowRoomsHandler),
('/create', CreateRoomHandler)


], debug=True)
