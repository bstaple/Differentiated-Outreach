from google.appengine.ext import ndb
import Final

class RoomDatabase(ndb.Model):
    room_name = ndb.StringProperty()
    host_user = ndb.StringProperty()
    number_of_users = ndb.IntegerProperty()
    rooms = ndb.ListProperty(Room)

class StudentDatabase(ndb.model):
    notes = ndb.StringProperty()
    name = ndb.StringProperty()
    corresponding_host = ndb.StringProperty()

class HostDatabase(ndb.model):
    name = ndb.StringProperty()
    room_number = ndb.StringProperty()
    host_message = ndb.StringProperty()

class WaitRoomDatabase(ndb.model):
    list_of_students = ndb.ListProperty(Student)
    host_owner = ndb.StringProperty()






    #Version 1.1 : Add a Is_Open boolean
