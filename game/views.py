from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
from .models import Picture
from .models import Progress
import random
from random import randint
import json
from django.views.decorators.csrf import csrf_exempt	
import sys
sys.path.insert(0, r'/home/pi/ocean_motion/ocean_motion')
from motion import move

#import ipdb; ipdb.set_trace()

passed_words = []
pic_ids = []
word_index = 0
current_progress = 0
question_number = Progress.objects.get(id = 1).max_progress
motor_move = Progress.objects.get(id = 1).rope_lenght/question_number

def get_response(request):
    
    if question_number > Picture.objects.count():
        global question_number
        question_number = Picture.objects.count()

    if question_number < 4:
        question_number = 4

    if len(pic_ids) == 0:
    	random_pictures()
    	move(-Progress.objects.get(id = 1).rope_lenght)

    random_word_index()

    correct_id = passed_words[len(passed_words)-1]   

    pictures = [
            {
                "url": Picture.objects.get(id=correct_id).pictureUrl,
                "id": correct_id
            },
            ]

    random.shuffle(pic_ids)
    i = 0
    for i in range(0, len(pic_ids) - 1):

        if not (pic_ids[i] == correct_id):
            pictures.append({
                    "url": Picture.objects.get(id=pic_ids[i]).pictureUrl,	
                    "id": pic_ids[i]
                })

        if len(pictures) == 4:
            break

    random.shuffle(pictures)
    response = {
        "progress": {
            "current": current_progress,
            "max": question_number
        },
        "word": {
            "id": correct_id,
            "word": Picture.objects.get(id=correct_id).word
        },
        "pictures": pictures
        
}

    return JsonResponse(response)


@csrf_exempt
def check_answer(request):
    data = json.loads(request.body)
    if data['pic_id'] == data['word_id']:
        is_correct = True
        current_progress += 1
        move(motor_move, True)
    else:
        is_correct = False
        if not current_progress == 0:
            current_progress -= 1
            move(-motor_move, True)

    response = {
        "word": Picture.objects.get(id = data['pic_id']).word,
        "correct": is_correct,
        "progress": {
            "current": current_progress,
            "max": question_number
        }
    }

    if current_progress == Progress.objects.get(id =1).max_progress:
    	global passed_words
    	global pic_ids
    	global word_index
        global current_progress
        global active_game
        current_progress = 0
    	passed_words = []
    	pic_ids = []
    	word_index = 0

    return JsonResponse(response, safe=False)


def random_pictures():
    i = 0
    while (i < question_number):
        rand = random.randint(0, Picture.objects.count() - 1)
        if not Picture.objects.all()[rand].id in pic_ids:
            pic_ids.append(Picture.objects.all()[rand].id)
            i+=1

def random_word_index():
    global passed_words
    global word_index
    while 1:
        word_index = random.randint(0, Picture.objects.count() - 1)
        if len(passed_words) == 4: 
            passed_words = []
        if not Picture.objects.all()[word_index].id in passed_words:
            passed_words.append(Picture.objects.all()[word_index].id)   
            break 