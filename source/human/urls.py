from django.conf.urls import url, patterns
from human import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from human.views import index, orgAction, mapData, economics, social, form, organizations, health


urlpatterns = patterns('',
    # ex: /polls/,
    url(r'^$', index, name = 'index'),
    url(r'^org-action/',orgAction.as_view(), name = 'org-action'),
    url(r'^map_data/', mapData, name = 'mapData'),
    url(r'^economics/', economics, name = 'economics'),
    url(r'^social/', social, name = 'social'),
    url(r'^form/', form.as_view(), name = 'form'),
    url(r'^org/', organizations, name = 'org'),
    url(r'^health/', health, name = 'health')
    
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()
