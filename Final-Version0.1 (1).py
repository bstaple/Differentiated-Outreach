import json
import webapp2

from google.appengine.api import memcache

def send_json(request_handler, props):
	request_handler.response.content_type = 'application/json'
	request_handler.response.write(json.dumps(props))

class HostHandler(webapp2.RequestHandler):
	def __init__(self, text):
		self.text = text
	def to_dict(self):
		result = {
			'text': self.text
		}
		return result
		
class HostMessages(webapp2.RequestHandler):
	def dispatch(self):
		result = {}


app = webapp2.WSGIApplication([
('/', HostHandler),
('/Host', HostMessages)



], debug=True)


		