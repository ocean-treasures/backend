from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Picture
import json
from django.views.decorators.csrf import csrf_exempt


def get_response(request):

    response = {'response': {
        "progress": {
            "current": 5,
            "max": 10
        },
        "word": {
            "id": 6261,
            "word": "banana"
        },
        "pictures": [
            {
                "url": "/media/6216.png",
                "id": 4
            },
            {
                "url": "/media/6414.png",
                "id": 16
            },
            {
                "url": "/media/1615.png",
                "id": 75
            },
            {
                "url": "/media/6215.png",
                "id": 215
            }]
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


#TODO find word by id in Picture
    response = {'response': {
        "word": "banana",
        "correct": is_correct
    }}

    return JsonResponse(response, safe=False)



def all(request):
    #import ipdb; ipdb.set_trace()
    pictures = Picture.objects.all()

    response = {'response': {
            "pictures": [
                {
                    "url": Picture.objects.all()[0].pictureUrl,
                    "id": Picture.objects.all()[0].id
                },
                {
                    "url": Picture.objects.all()[1].pictureUrl,
                    "id": Picture.objects.all()[1].id
                }
            ] 
    }}
    #result = ['picture id: {}, picture word: {}\n '.format(p.id, p.word) for p in pictures]
    return JsonResponse(response)