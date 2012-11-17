from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'brainfire.views.home', name='home'),
    # url(r'^brainfire/', include('brainfire.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

# Root level static files 
urls = [('^%s$' % f, 'redirect_to', {'url': settings.STATIC_URL + f}) for f in settings.ASSETS]
urlpatterns += patterns('django.views.generic.simple', *urls)

urlpatterns += patterns('django.views.generic.simple',
    url(r'^$', 'direct_to_template', {'template': 'index.html'}, name='home'),
    url(r'^terms_and_conditions/$', 'direct_to_template', {'template': 'terms_and_conditions.html'}, name='terms_and_conditions'),
    url(r'^privacy/$', 'direct_to_template', {'template': 'privacy.html'}, name='privacy'),
)

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )

urlpatterns += staticfiles_urlpatterns()

def handler500(request):
    """
    500 error handler which includes ``request`` in the context.

    Templates: `500.html`
    Context: None
    """
    from django.template import Context, loader
    from django.http import HttpResponseServerError

    t = loader.get_template('500.html') # You need to create a 500.html template.
    return HttpResponseServerError(t.render(Context({
        'request': request,
        'STATIC_URL': settings.STATIC_URL,
    })))
