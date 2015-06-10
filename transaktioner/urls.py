from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^last_month$', views.last_month, name="last_month"),
    url(r'^last_month/mat$', views.only_mat, name="bara_mat"),
    url(r'^mat$', views.only_mat, name="bara_mat"),
]
