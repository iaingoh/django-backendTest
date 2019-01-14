from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
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

class CardList(APIView):

    def get(self, request):
        with open('cards/resources/response.json') as f:
            collection = json.load(f)

            deck = []
            flag = True
            while flag:
                card = random.choice(collection)
                if not deck:
                    deck.append(card)
                    playerClass = card['playerClass']
                    continue
                elif len(deck) < 30:
                    if card['playerClass'] == playerClass or card['playerClass'] == 'Neutral':
                        deck.append(card)
                else:
                    flag = False
            for card in deck:
                print(card['playerClass'])
            print(len(deck))
        
        return Response(deck)




