import webapp2

class ShowRoomsHandler(webapp2.RequestHandler):
	
class CreateRoomHandler(webapp2.RequestHandler):
	

app = webapp2.WSGIApplication([
('/', ShowRoomsHandler),
('/Create', CreateRoomHandler)



], debug=True)


		
