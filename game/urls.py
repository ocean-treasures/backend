from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^next_word/', views.is_active_game, name='get_response'),
    url(r'^check_answer/', views.check_answer, name='check_answer'),
    url(r'^move_up/(?P<time_in_seconds>[0-9]+)', views.move_up, name='move_up'),
    url(r'^move_down/(?P<time_in_seconds>[0-9]+)', views.move_down, name='move_down'),
    url(r'^rope_lenght/', views.rope_lenght, name='rope_lenhgt'),
    url(r'^calibration/(?P<time_in_seconds>[0-9]+)', views.calibration, name='calibration'),
    url(r'^calibration_page/', views.calibration_page, name='calibration_page'),
]
