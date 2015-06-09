from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^last_month$', views.last_month),
]
