from django.conf.urls import url

from game import views

urlpatterns = [
    url(r'^next_word/', views.next_word, name='next_word'),
    url(r'^check_answer/', views.check_word, name='check_word'),

    url(r'^move_up/(?P<steps>[0-9]+)', views.move_up, name='move_up'),
    url(r'^move_down/(?P<steps>[0-9]+)', views.move_down, name='move_down'),
    url(r'^calibrate/', views.calibration, name='calibration'),
    url(r'^calibration_page/', views.calibration_page)
]
