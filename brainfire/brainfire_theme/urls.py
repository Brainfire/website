from django.conf.urls.defaults import patterns, include, url
from django.views.generic.base import TemplateView

urlpatterns = patterns('',
    url(r'^robots\.txt$', TextPlainView.as_view(template_name='robots.txt')),
    url(r'^humans\.txt$', TextPlainView.as_view(template_name='humans.txt')),
)