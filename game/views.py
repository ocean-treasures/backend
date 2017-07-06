from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Picture
import random
from random import randint
import json
from django.views.decorators.csrf import csrf_exempt


passed_words = []
pic_ids = []
pic = []
start_game = False
word_index = 0

def get_response(request):
    if start_game == False:
        random_pictures()
        global start_game 
        start_game = True

    print (pic_ids)
    print (pic)

    random_word_index()
    pictures = [
            {
                "url": pic[word_index],
                "id": pic_ids[word_index]
            },
            ]

     #random.shuffle(pic)
#TODO make json object 

    response = {'response': {
        "progress": {
            "current": 5,
            "max": 10
        },
        "word": {
            "id": pic_ids[word_index],
            "word": Picture.objects.get(id=pic_ids[word_index]).word
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
    else:
        is_correct = False

    # import ipdb; ipdb.set_trace()


    response = {'response': {
        "word": Picture.objects.get(id = data['word_id']).word,
        "correct": is_correct
    }}

    return JsonResponse(response, safe=False)

def random_pictures():
    i = 0
    while (i < 5):
        rand = random.randint(0, 6)
        if not rand in pic_ids:
            pic_ids.append(rand)
            pic.append(Picture.objects.all()[rand].pictureUrl)
            i+=1

def random_word_index():
    while 1:
        global word_index
        word_index = random.randint(0, 4)
        if len(passed_words) == 5:
            global passed_words
            passed_words = []
        if not word_index in passed_words:
            passed_words.append(word_index)   
            break 
