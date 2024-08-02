from django.urls import path,include
from rest_framework.routers import DefaultRouter

from profiles_api import views

router =DefaultRouter()
router.register('hello-viewset',views.HelloVIewSet,basename='hello-viewset')
router.register('profile',views.UserprofileViewSet)

urlpatterns = [
    path('hello-view/',views.HelloApiView.as_view()),
    path('',include(router.urls))

   
]