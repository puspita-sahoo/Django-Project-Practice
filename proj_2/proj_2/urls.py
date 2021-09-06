from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("msg/",views.msg_page, name='msg_page'),
    path("newsfeed/",views.newsfeed_page, name='newsfeed_page'),
    path("profile/",views.profile_page, name='profile_page')
]
