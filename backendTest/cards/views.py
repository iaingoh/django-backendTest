from django.shortcuts import render
from django.http import HttpResponse
import json
import random

def load_json(request):
    with open('cards/resources/response.json') as f:
        collection = json.load(f)

        deck = []
        for i in range(30):
            deck.append(random.choice(collection))

        for card in deck:
            print(card['name'])

    print(len(deck))
    return HttpResponse('<h3>The view is loaded</h3>')



