from django.conf.urls import include, url
#from material.frontend import urls as frontend_urls
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'', include(frontend_urls)),
    url(r'^game/', include('game.urls')),
]
