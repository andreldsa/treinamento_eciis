from google.appengine.ext import ndb

class User(ndb.Model):

    # The id of the institutions to which the user belongs
    # minimum = 1
    institution = ndb.KeyStringProperty(repeated=True)

    # The id of the institutions followed by the user
    # minimum = 0
    follows = ndb.KeyStringProperty(repeated=True)

    # The id of the posts authored by the user
    posts = ndb.KeyStringProperty(repeated=True)

    # The ids of the institutions administered by the user
    institutions_admin = ndb.KeyStringProperty(repeated=True)

    # Notofications received by the user
    notifications = ndb.JsonProperty()


class Timeline(ndb.Model):

    owner = ndb.KeyStringProperty
    posts = ndb.JsonProperty



class Institution(ndb.Model):

    # The admin user of this institution
    admin = ndb.KeyStringProperty(required=True)

    # The parent institution
    # Value is None for institutions without parent
    parent_institution = ndb.KeyStringProperty()

    # The ids of users who are members of this institution
    members = ndb.KeyStringProperty(repeated=True)

    # Users subscribed to this institution's posts
    # All these followers receive copies of the posts
    # of this institution in their timeline.
    followers = ndb.KeyStringProperty(repeated=True)

    # 
    posts = ndb.KeyStringProperty(repeated=True)

    
class Post(ndb.Model)

    # user who is the author
    author = ndb.KeyStringProperty

    # institution to which this post belongs
    institution = ndb.KeyStringProperty



class Channel(ndb.Model)
