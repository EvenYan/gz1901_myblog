from django.conf.urls import url

from blog import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^detail/(?P<id>\d+)', views.detail, name="detail"),
    url(r'^archive/(\d{4})/(\d+)', views.archive, name="archive"),
    url(r'^category/(\d+)', views.category, name="category"),
]
