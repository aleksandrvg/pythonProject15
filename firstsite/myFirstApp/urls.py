from django.urls import path
from .views import two, test
urlpatterns = [
    path('<int:one>/<int:two>/', two),
    path('another/', test),
]