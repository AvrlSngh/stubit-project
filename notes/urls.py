from django.conf.urls import url
from . import views

app_name = 'notes'

urlpatterns = [
    url(r'^$', views.notes_list, name = "notes_list"),
    ]
