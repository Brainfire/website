from django.conf.urls.defaults import *
from views import ContactView
 
urlpatterns = patterns('', 
    url(r'^$', ContactView.as_view(), name='contact'),
)
