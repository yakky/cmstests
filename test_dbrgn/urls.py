from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from testx.views import MyFormView

admin.autodiscover()

urlpatterns = i18n_patterns('',
    # Examples:
    # url(r'^$', 'test_dbrgn.views.home', name='home'),
    # url(r'^test_dbrgn/', include('test_dbrgn.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^myform/', MyFormView.as_view()),
    url(r'^', include('cms.urls')),

)
