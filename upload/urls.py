from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^files/$', views.dirlist, name='files'),
    url(r'^items/$', views.itemlist, name='items'),
]