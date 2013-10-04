from django.db import models

class User(models.Model):
	"""
	Contains teh details of all the users of Chef.
	"""

	# Possible authorization levels of users in Chef
	AUTH_LEVELS = (
	('ADMIN', 'Administrator'),
	('MOD', 'Moderator'),
	('USR', 'Attendee')
	)

	user_id = models.CharField(
		max_length=128, 
		)
	
	first_name = models.CharField(
		max_length=1024, 
		)

	last_name = models.CharField(
		max_length=1024, 
		)

	email = models.EmailField(

		)

	user_type = models.CharField(
			choices=AUTH_LEVELS,
			default=2,
			)

	added = models.DateTimeField(
			auto_now_add=True,
			)

	organization = models.CharField(
			max_length=1024,
			)

	campushash_uid = models.CharField(
		max_length=1024,
		blank=True
		)