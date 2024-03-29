from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^create_user$', views.create_user),
    url(r'^login', views.login),
    url(r'^logout$', views.logout),
    url(r'^wall$', views.success),
    url(r'add_msg', views.add_msg),
    url(r'add_cm/(?P<msg_id>\d+)$', views.add_cm),
    url(r'delete/(?P<cm_id>\d+)$', views.delete),    
]