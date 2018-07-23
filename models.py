from google.appengine.ext import ndb

# class HostMessage(ndb.Model):
#     text = ndb.StringProperty()
#     timeStamp = ndb.IntegerProperty()
#     roomName = ndb.StringProperty()
#     hostName = ndb.StringProperty()

class Room(ndb.Model):
    name = ndb.StringProperty()
    host_user = ndb.StringProperty()
    number_of_users = ndb.IntegerProperty()
    #Version 1.1 : Add a Is_Open boolean
