from django.db import models
import uuid
# Create your models here.
class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable = False, unique = True)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    phone_number = Models.CharField(max_length = 14)
    email = Models.CharField(max_length = 100)

class Event(models.model):
    event_id = models.UUIDField(primary_key=True, default = uuid.uuid4, editable = False, unique = True)
    event_name = models.CharField(max_length = 100)
    event_date = models.DateTimeField('date of event')
    event_description = models.CharField(max_length = 5000)
    