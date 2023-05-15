from django.urls import path
from profiles_api import views


urlpatterns = [
    path('name-views/', views.NameApiView.as_view()),

]
