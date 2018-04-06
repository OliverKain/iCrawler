from django.conf import settings
from django.conf.urls import url,static
from main import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', views.stockinfo, name='home'),
    url(r'^api/crawl/', views.crawl, name='crawl'),
]
urlpatterns += staticfiles_urlpatterns()