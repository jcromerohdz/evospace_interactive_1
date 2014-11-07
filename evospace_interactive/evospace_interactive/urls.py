from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'shapes.views.home', name='home'),
    url(r'^facebook/get_login/?$', 'shapes.views.facebook_get_login', name='facebook_get_login'),
    url(r'^facebook/login/?$', 'shapes.views.facebook_login', name='facebook_login'),
    url(r'^logout/?$', 'shapes.views.logout_view', name='logout_view'),
    url(r'^individual/(\d+)/$', 'shapes.views.individual_view', name='individual_view'),
    url(r'^EvoSpace/?$', 'shapes.views.evospace', name='evospace'),
    url(r'^add_collection/(\d+)/$', 'shapes.views.add_collection', name='add_collection'),
    url(r'^get_user_collections/(\d+)/$', 'shapes.views.get_user_collections', name='get_user_collections'),
    url(r'^add_ind_to_col/(\d+)/$', 'shapes.views.add_ind_to_col', name='add_ind_to_col'),
    url(r'^get_collection/(\d+)/$', 'shapes.views.get_collection', name='get_collection'),
    url(r'^get_collection/(\d+)/(\d+)$', 'shapes.views.get_collection', name='get_collection'),
    url(r'^dashboard/$', 'shapes.views.dashboard', name='dashboard'),
    url(r'^home2/$', 'shapes.views.home2', name='home2'),
    # url('', include('social.apps.django_app.urls', namespace='social')),


    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,
						  document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,
						  document_root=settings.MEDIA_ROOT)
