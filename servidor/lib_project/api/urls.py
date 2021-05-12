from django.urls import path

from.views import TareaAPIView


urlpatterns = [
    path('',TareaAPIView.as_view()),
]

