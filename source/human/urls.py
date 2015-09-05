from django.conf.urls import url, patterns
from human import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from human.views import index, orgAction, mapData


urlpatterns = patterns('',
    # ex: /polls/,
    url(r'^$', index.as_view(), name = 'index'),
    url(r'^org-action/',orgAction.as_view(), name = 'org-action'),
    url(r'^map_data/', mapData, name = 'mapData'),
    

     
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()
