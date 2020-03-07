from django.conf.urls import url, include
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.mainPage),
    url(r'^about_us/$', views.aboutPage),
    url(r'^blog/$', views.blogPage),
    url(r'^prices/$', views.pricesPage),
    url(r'^contacts/$', views.contactsPage),
]