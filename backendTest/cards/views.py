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
            print("There are " + str(len(collection)) + " cards in the collection.")

        # Remove cards where key playerClass does not exist.
        faulty_cards = []
        for card in collection:
            if 'playerClass' not in card:
                faulty_cards.append(card)
                index = collection.index(card)
                del collection[index]
        print("The conditional found " + str(len(faulty_cards)) + " faulty cards.")
        print("There are now " + str(len(collection)) + " cards in the collection.")

        deck = []
        while len(deck) < 30:
            card = random.choice(collection)
            if not deck:
                deck.append(card)
                playerClass = card['playerClass']
                continue
            elif card['playerClass'] == playerClass or card['playerClass'] == 'Neutral':
                    deck.append(card)

        for card in deck:
            print(card['playerClass'])

        print(len(deck))
    
        return Response(deck)




