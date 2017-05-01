from django.conf.urls import url
from . import views

app_name = 'storyteller'
urlpatterns = [
    url(r'^ship', views.ship, name='ship'),
    url(r'^$', views.index, name='index'),
    ]