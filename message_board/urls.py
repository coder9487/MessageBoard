from django.urls import path
from . import views

urlpatterns = [
    path('message_board/', views.message_board, name='message_board'),
]