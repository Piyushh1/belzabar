from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^users/$', views.user_list),
    url(r'^users/(?P<pk>[0-9a-z\-]+)$',views.user_detail),
]
urlpatterns = format_suffix_patterns(urlpatterns)