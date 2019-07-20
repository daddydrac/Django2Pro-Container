from django.urls import path
from .views import NavList, NavDetail


urlpatterns = [

    path('navigation/', NavList.as_view()),
    path('navigation/<int:pk>/', NavDetail.as_view()),


]
