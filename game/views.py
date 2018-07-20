from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import Game

import logging
import json
from django.views.decorators.csrf import csrf_exempt
import ocean_motion
from constance import config

from game.utils import choose_words

logger = logging.getLogger('two_fish')

def next_word(request):
    game = get_object_or_404(Game, is_active=True)
    correct_word, pictures = choose_words(game)

    response = {
        "progress": {
            "current": game.guessed_words.count(),
            "max": game.words.count()
        },
        "word": correct_word,
        "pictures": pictures
    }
    return JsonResponse(response)

@csrf_exempt
def check_word(request):
    print(json.loads(request.body))
    game = get_object_or_404(Game, is_active=True)
    print(game.words.all())
    return JsonResponse({})


def move_up(request, steps):
    response = JsonResponse({"steps": steps})
    try:
        ocean_motion.motor.up(steps)
    except Exception as ex:
        if settings.DEBUG:
            logger.debug(ex)
        else:
            response = JsonResponse({"error": str(ex)})
            response.status_code = 500
    return response


def move_down(request, steps):
    response = JsonResponse({"steps": steps})
    try:
        ocean_motion.motor.down(steps)
    except Exception as ex:
        if settings.DEBUG:
            logger.debug(ex)
        else:
            response = JsonResponse({"error": str(ex)})
            response.status_code = 500
    return response

@csrf_exempt
def calibration(request):
    data = json.loads(request.body)
    config.TOTAL_STEPS = data['total_steps']
    return JsonResponse({})


def calibration_page(request):
    return render(request, 'calibrate.html', {})
