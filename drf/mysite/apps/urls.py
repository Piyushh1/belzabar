from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from .views import UserViewSet
from . import views

# urlpatterns = [
#     url(r'^users/$', views.user_list),
#     url(r'^users/(?P<pk>[0-9a-z\-]+)$',views.user_detail),
# ]

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
urlpatterns = router.urls

# url (r/users , 'UserViewSet.as_views(
#  "get" : "list"
#  "post" : "create" })

#   url (r/users/<pk> , 'UserViewSet.as_views(
#  "get" : "retrieve" retrieeve return a single object hence in mixins.py the <pk> is passed internally
#  "post" : "update" })
#
#
# urlpatterns = format_suffix_patterns(urlpatterns)