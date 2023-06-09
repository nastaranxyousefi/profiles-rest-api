from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('name-viewset', views.NameViewSet, basename='name-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.ProfileFeedItemViewSet)

urlpatterns = [
    path('name-views/', views.NameApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),

]
 