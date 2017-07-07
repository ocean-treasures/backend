from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Picture
from .models import Progress
import random
from random import randint
import json
from django.views.decorators.csrf import csrf_exempt


passed_words = []
pic_ids = []
start_game = False
word_index = 0
current_progress = Progress.objects.get()


def get_response(request):
    if start_game == False:
        random_pictures()
        global start_game 
        start_game = True

    random_word_index()
    correct_id = passed_words[len(passed_words)-1]
    pictures = [
            {
                "url": Picture.objects.get(id=pic_ids[word_index]).pictureUrl,
                "id": correct_id
            },
            ]

    random.shuffle(pic_ids)
    #TODO make json object 
    
    i = 0
    for i in range(0, len(pic_ids) - 1):
        #import ipdb; ipdb.set_trace()
        if not (pic_ids[i] == correct_id):
            pictures.append({
                    "url": Picture.objects.get(id=pic_ids[i]).pictureUrl,
                    "id": pic_ids[i]
                })

        if len(pictures) == 4:
            break

    
    random.shuffle(pictures)
    response = {'response': {
        "progress": {
            "current": current_progress.curr,
            "max": current_progress.max_progress
        },
        "word": {
            "id": correct_id,
            "word": Picture.objects.get(id=correct_id).word
        },
        "pictures": pictures
        
    }}


    return JsonResponse(response)


@csrf_exempt
def check_answer(request):
    # import ipdb; ipdb.set_trace()
    data = json.loads(request.POST.get('body'))

    if data['pic_id'] == data['word_id']:
        is_correct = True
        current_progress.curr += 1
    else:
        is_correct = False
        if not current_progress.curr == 0:
            current_progress.curr -= 1

    # import ipdb; ipdb.set_trace()
    current_progress.save()

    response = {'response': {
        "word": Picture.objects.get(id = data['word_id']).word,
        "correct": is_correct
    }}

    return JsonResponse(response, safe=False)




def random_pictures():
    i = 0
    while (i < 5):
        rand = random.randint(0, 6)
        if not Picture.objects.all()[rand].id in pic_ids:
            pic_ids.append(Picture.objects.all()[rand].id)
            i+=1

def random_word_index():
    while 1:
        global word_index
        word_index = random.randint(0, 4)
        if len(passed_words) == 5:
            global passed_words
            passed_words = []
        if not Picture.objects.all()[word_index].id in passed_words:
            passed_words.append(Picture.objects.all()[word_index].id)   
            break 


