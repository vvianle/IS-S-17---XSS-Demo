from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^cookies$', CookieListView.as_view(), name='cookie_list'),
]