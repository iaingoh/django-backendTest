# django-backendTest
Create random thirty card deck to expose via endpoint. The development process has been commited, logged and pushed regularly, to extensively document the development process. The project started off without Django but as a standlone python script loading the json response and randomly cutting the deck. You may find the repo here: https://github.com/iaingoh/lomotif-technicaltest1 . When i realized that the sorting algorithm i tried to implement was full of holes, i scraped it and decided to structure the entire project first and then look into it after. The project now exposes a random deck via the endpoint.
**Update:** The deck is returned with the same playerClass or 'Neutral' cards.

---

Project URL: https://lomotif-backendtest.herokuapp.com/cards/

---

### Author

Iain Goh

---

### How to access endpoint and view deck
Simply visit *https://lomotif-backendtest.herokuapp.com/cards/* to view the random thirty card deck. It has been deployed on Heroku.
The project may also be cloned but be sure to install dependencies as *django and djangorestframework*. Pipenv was used in the development of this project.

---

## URL Routes

```
/admin
/dev
/cards
```

---

## Planned Improvements
Two project requirements:
- A sorting algorithm to only allow cards of same playerClass or 'Neutral' to be decked(Partial completion).
    - Or rather, there may be a built in module as itertools that can perform such sorting efficiently. The thing was that 
    each card's attributes may have been different from the next so it was difficult to loop through the differently formatted
    cards.
    - Storing a dictionary object in Django's model class isn't straightforward and so the loaded json file was exposed to the endpoint directly, bypassing Django's model class entirely.
- Cards may or may not repeat more than twice.
