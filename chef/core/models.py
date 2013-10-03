from django.db import models

class User(models.Model):
	"""
	Contains teh details of all the users of Chef.
	"""

	# Possible authorization levels of users in Chef
	AUTH_LEVELS = (
	(0, 'ADMIN'),
	(1, 'MOD'),
	(2, 'ATTENDEE')
	)

	user_id = models.CharField(
		max_length=128, 
		blank=False, 
		null=False
		)
	
	first_name = models.CharField(
		max_length=1024, 
		blank=False, 
		null=False
		)

	last_name = models.CharField(
		max_length=1024, 
		blank=True, 
		null=True
		)

	email = models.EmailField()

	user_type = models.CharField(
			choices=AUTH_LEVELS,
			default=2,
			blank=False,
			null=False
			)

	added = models.DateTimeField(
			auto_now_add=True,
			blank=False,
			null=False
			)

	organization = models.CharField(
			max_length=1024,
			null=False,
			blank=False
			)

	campushash_uid = models.CharField(
		max_length=1024,
		null=True,
		blank=True
		)