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
		('ATT', 'Attendee')
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
	name = models.CharField(max_length=1024)

	def __unicode__(self):
		return self.name