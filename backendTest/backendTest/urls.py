from django.contrib import admin
from django.urls import path, include
from cards import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cards/', views.CardList.as_view())
]
