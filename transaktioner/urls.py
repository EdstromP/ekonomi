from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^last_month$', views.last_month, name="last_month"),
    url(r'^last_month/mat$', views.only_mat, name="bara_mat"),
    url(r'^mat$', views.only_mat, name="bara_mat"),
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^statistik$', views.StatistikView.as_view(), name="statistik"),
    url(r'^kategori/(?P<kategori>[\w-]+)/$', views.KategoriView.as_view(), name="kategori"),
    #url(r'^kategori/([\w-]+)/$', views.KategoriView.as_view(), name="kategori"),
    #url(r'^/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),
    url(r'^(?P<pk>[0-9]+)/$', views.TransaktionUpdate.as_view(), name="uppdatera"),
]
