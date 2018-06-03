from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Game
import json
from django.views.decorators.csrf import csrf_exempt
import ocean_motion
from constance import config

from game.utils import choose_words


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


def check_word(request):
    return JsonResponse({})


def move_up(request, steps):
    ocean_motion.motor.up(steps)
    return JsonResponse({"steps": steps})


def move_down(request, steps):
    ocean_motion.motor.down(steps)
    return JsonResponse({"steps": steps})


@csrf_exempt
def calibration(request):
    data = json.loads(request.body)
    config.TOTAL_STEPS = data['total_steps']
    return JsonResponse({})


def calibration_page(request):
    return render(request, 'calibrate.html', {})
