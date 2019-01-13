# django-backendTest
Create random thirty card deck to expose via endpoint

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
- A sorting algorithm to only allow cards of same playerClass or 'Neutral' to be decked.
    - Or rather, there may be a built in module as itertools that can perform such sorting efficiently. The thing was that 
    each card's attributes may have been different from the next so it was difficult to loop through the differently formatted
    cards.
- Cards may or may not repeat more than twice.
