from django.urls import path
from .views import taskList, taskDetail


urlpatterns = [
    path('', taskList.as_view(), name='taskList'),
    path('<int:pk>/', taskDetail.as_view(), name='taskDetail'),
]