from django.urls import path
from app.views import accueil, detail
urlpatterns = [
    path("", accueil, name="accueil"),
    path("sites/<str:p>", detail, name="detail"),
]