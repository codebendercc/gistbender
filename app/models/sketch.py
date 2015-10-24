import datetime
from app import db
from mongokit import Document

@db.register
class Sketch(Document):

    __collection__ = 'sketches'
    __database__ = 'gistbender'

    structure = {
        'url': unicode,
        'filename': unicode,
        'description': unicode,
        'code': unicode
       # 'sketch': ObjectId
    } 

    required_fields = ['url','filename','code']
    default_values = {
        'description': u''
    }
    use_dot_notation = True
