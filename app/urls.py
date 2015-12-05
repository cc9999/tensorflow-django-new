from django.conf.urls import include
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^create/$',views.VCreateView.as_view(),name='create'),
    url(r'^success/$',views.VSuccessView.as_view(),name='success'),
    url(r'^detail/(?P<pk>[-\w]+)/$',views.VDetailView.as_view(),name='detail'),
    url(r'^list/$',views.VListView.as_view(),name='list'),
    url(r'^test/$',views.test,name='test'),
]
