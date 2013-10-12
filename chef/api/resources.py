from tastypie.resources import ModelResource
from core.models import Profile

class ProfileResource(ModelResource):
	class Meta:
		queryset = Profile.objects.all()
		allowed_methods = ['get']