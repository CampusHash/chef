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
		('USR', 'Attendee')
	)

	user = models.ForeignKey(User)
	user_type = models.CharField(max_length=3, choices=AUTH_LEVELS, default='USR')
	organization = models.CharField(max_length=1024)
	campushash_uid = models.CharField(max_length=1024, blank=True)