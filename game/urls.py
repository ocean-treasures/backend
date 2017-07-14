from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^next_word/', views.is_active_game, name='get_response'),
    url(r'^check_answer/', views.check_answer, name='check_answer'),
    #url(r'^calibration/', views.calibration, name='calibration'),
    #url(r'^test/', views.test, name='test'),
]
   