from django.urls import path
from .views import TareaListView

urlpatterns = [
    path ('',TareaListView.as_view(),name = 'home' ),
]