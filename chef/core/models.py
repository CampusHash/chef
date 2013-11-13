from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
	"""
	Contains the profile details of all the users of Chef.
	"""

	# Possible authorization levels of users in Chef
	AUTH_LEVELS = (
		('ADM', 'Administrator'),
		('MOD', 'Moderator'),
		('SPE', 'Speaker'),
		('ATT', 'Attendee'),
	)

	user = models.ForeignKey(User)
	user_type = models.CharField(max_length=3, choices=AUTH_LEVELS, default='ATT')
	organization = models.CharField(max_length=1024)
	campushash_uid = models.CharField(max_length=1024, blank=True)

	def __unicode__(self):
		return self.user.username


class Event(models.Model):
	"""
	Event definitions. An admin can create/update/delete an event.
	A default locally created can be registered with CampusHash Event Central.
	Doing do needs an API key.
	"""

	EVENT_TYPES = (
		('WOR', 'Workshop'),
		('HAC', 'Hackathon'),
		('INT', 'InternHacks'),
		('CUS', 'Custom')
	)

	# Essential details
	name = models.CharField(max_length=1024)	
	date = models.DateField()
	
	# Venue details
	campus_name = models.CharField(max_length=1024)
	address = models.CharField(max_length=1024)
	city = models.CharField(max_length=1024)

	# Session details
	event_type = models.CharField(max_length=3, choices=EVENT_TYPES, default='INT')
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	speaker = models.ForeignKey(Profile)
	
	def __unicode__(self):
		return self.name