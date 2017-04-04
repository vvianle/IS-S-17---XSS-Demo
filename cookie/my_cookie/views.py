from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.permissions import AllowAny

# Create your views here.
# GET /posts/
class CookieListView(generics.ListCreateAPIView):
	serializer_class = CookieSerializer
	permission_classes = (AllowAny, )
	authentication_classes = ([])
	queryset = Cookie.objects.all()