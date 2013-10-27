from tastypie.resources import ModelResource
from core.models import Profile, User

class ProfileResource(ModelResource):
	class Meta:
		queryset = Profile.objects.all()
		allowed_methods = ['get']

class UserResource(ModelResource):
	class Meta:
		queryset = User.objects.all()
		resource_name = 'user'