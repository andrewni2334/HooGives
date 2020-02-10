from django.db import models
import uuid
# Create your models here.
class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default = uuid.uuid4, unique = True)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    phone_number = models.CharField(max_length = 14)
    email = models.CharField(max_length = 100)
    # @classmethod
    # def create(cls):
    #     user = cls(user_id=uuid.uuid4().hex)
    #     # do something with the book
    #     return user

class Event(models.Model):
    event_id = models.UUIDField(primary_key=True, default = uuid.uuid4, unique = True)
    event_name = models.CharField(max_length = 100)
    event_date = models.DateTimeField('date of event')
    event_description = models.CharField(max_length = 5000)
    