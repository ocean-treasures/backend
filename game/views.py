from django.http import JsonResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render
from .models import Picture
from .models import Game
import random
import json
from django.views.decorators.csrf import csrf_exempt
import ocean_motion
from constance import config

passed_words = []
pic_ids = []
word_index = 0
question_number = 0
motor_move = 0.0
active_game = -1

current_progress = 1


def is_active_game(request):
    if Game.objects.filter(active=True).count() == 0:
        return HttpResponseNotFound("No active game")
    else:
        game_picturs = Game.objects.get(active=True).pictures.all()
        current_progress = Game.objects.get(active=True)
        print(current_progress.id)
        global question_number
        question_number = Game.objects.get(active=True).number_of_pictures()
        global motor_move
        motor_move = config.ROPE_LENGHT / question_number
        response = get_response(game_picturs)
        return JsonResponse(response, safe=False)


def get_response(game_picturs):
    print("Current")
    print(Game.objects.get(active=True).current)
    print("end")

    if Game.objects.get(active=True).current == 0:
        null()
        for picture in game_picturs:
            pic_ids.append(picture.id)

    print("After")
    print(pic_ids)

    random_word_index(game_picturs)

    correct_id = passed_words[len(passed_words) - 1]
    pictures = [
        {
            "url": game_picturs.get(id=correct_id).pictureUrl,
            "id":  correct_id
        },
    ]

    print("PICDS")
    print(pic_ids)
    random.shuffle(pic_ids)

    i = 0
    for i in range(0, len(pic_ids)):

        if not (pic_ids[i] == correct_id):
            pictures.append({
                "url": game_picturs.get(id=pic_ids[i]).pictureUrl,
                "id":  pic_ids[i]
            })

        if len(pictures) == 4:
            break

    random.shuffle(pictures)
    response = {
        "progress": {
            "current": Game.objects.get(active=True).current,
            "max":     question_number
        },
        "word":     {
            "id":   correct_id,
            "word": game_picturs.get(id=correct_id).word
        },
        "pictures": pictures

    }
    return response


@csrf_exempt
def check_answer(request):
    global current_progress
    current_progress = Game.objects.get(active=True)
    data = json.loads(request.body)
    if data['pic_id'] == data['word_id']:
        is_correct = True
        current_progress.current += 1
        current_progress.save()
        ocean_motion.motor.down(question_number/config.TOTAL_STEPS)
    else:
        is_correct = False
        if not current_progress.current == 0:
            current_progress.current -= 1
            current_progress.save()
            ocean_motion.motor.up(question_number/config.TOTAL_STEPS)

    response = {
        "word":     Picture.objects.get(id=data['pic_id']).word,
        "correct":  is_correct,
        "progress": {
            "current": current_progress.current,
            "max":     question_number
        }
    }

    if current_progress.current == Game.objects.get(active=True).number_of_pictures():
        current_progress.current = 0
        current_progress.save()
        null()

    return JsonResponse(response, safe=False)


def random_word_index(game_picturs):
    global passed_words
    global word_index
    print("Passed words")
    print(passed_words)
    print("PICID")
    print(pic_ids)
    while 1:
        word_index = random.randint(0, len(set(pic_ids)) - 1)
        if len(passed_words) == len(game_picturs):
            passed_words = []
        print("pictures: ", game_picturs)
        if not game_picturs[word_index].id in passed_words:
            passed_words.append(game_picturs[word_index].id)
            break


def null():
    global passed_words
    global pic_ids
    global word_index
    pic_ids = []
    word_index = 0
    passed_words = []


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
