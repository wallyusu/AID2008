from django.urls import path
from . import views

urlpatterns = [
    path('<int:topic_id>',views.message_view),  # topic_id为url中t_id
]