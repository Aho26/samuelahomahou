from MonCv import views
from django.urls import path



urlpatterns = [
    path('', views.moncv,name="moncv"),
    path('envoyer', views.envoyer_message,name="envoyer")
]
