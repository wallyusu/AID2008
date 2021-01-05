from django.urls import path
from . import views
urlpatterns = [
    # http://127.0.0.1:8000/payment/jump/
    path('jump/',views.JumpView.as_view()),
    path('result/',views.ResultView.as_view()),

]