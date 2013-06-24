from wimsdemo.views import *
from django.conf.urls import patterns, include, url

urlpatterns = patterns("",
    url(r'^$', DemoView.as_view(), name="demo"),
    #url(R'^result/$', ResultView.as_view(), name="demo_result"),
)