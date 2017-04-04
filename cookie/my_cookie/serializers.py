from rest_framework import serializers
from .models import *

class CookieSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cookie
		fields = ('cookie', 'timestamp')