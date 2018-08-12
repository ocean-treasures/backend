import math
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import Game, Word

import logging
import json
from django.views.decorators.csrf import csrf_exempt
import ocean_motion
from constance import config

from game.utils import choose_words

logger = logging.getLogger('two_fish')


def next_word(request):
    """
    Returns word, four pictures and game progress.
    :param request:
    :return:
    """
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
    """
    Check if the word and the picture match.
    :param request:
    :return:
    """
    json_body = json.loads(request.body)
    pic_id = json_body.get('pic_id')
    word_id = json_body.get('word_id')
    game = get_object_or_404(Game, is_active=True)
    steps_per_word = math.ceil(config.TOTAL_STEPS / game.number_of_pictures())

    if pic_id and word_id and pic_id == word_id and game.words.filter(id=word_id).exists():
        if not game.guessed_words.filter(id=word_id).exists():
            game.guessed_words.add(word_id)
            move_down(request, steps_per_word)
        is_correct = True
    else:
        game.guessed_words.remove(game.guessed_words.first())
        move_up(steps_per_word, steps_per_word)
        is_correct = False

    current = game.guessed_words.count()
    all_pics = game.number_of_pictures()

    response = {
        "word":     Word.objects.get(id=word_id).text,
        "correct":  is_correct,
        "progress": {
            "current": current,
            "max":     all_pics
        }
    }
    if current == all_pics:
        game.reset()
    return JsonResponse(response)


def move_up(request, steps):
    response = JsonResponse({"steps": steps})
    try:
        ocean_motion.motor.up(steps)
    except Exception as ex:
        if settings.DEBUG:
            logger.debug('up {}'.format(steps))
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
            logger.debug('down {}'.format(steps))
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
