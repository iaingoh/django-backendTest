from django.shortcuts import render
from django.http import HttpResponse
import json

def load_json(request):
    with open('cards/resources/response.json') as f:
        collection = json.load(f)

        for card in collection:
            print(card['name'])

        print(len(collection))
        print(type(collection))

        card1 = collection[0]
        print(type(card1))
        print(len(card1))

        card2 = collection[1]
        print(len(card2))


    return HttpResponse('<h3>The view is loaded</h3>')

