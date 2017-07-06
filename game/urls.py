from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^next_word/', views.get_response, name='get_response'),
    url(r'^check_answer/', views.check_answer, name='check_answer'),
]
   