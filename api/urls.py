from django.db import router
from django.urls import include, path
#from rest_framework import DefaultRouter
from . import views

#router = DefaultRouter()
#router.register("student", views.StudentView, basename="student")
urlpatterns = [
    path("teachers/", views.teachers_api_view),
    path("teacher/<int:pk>/", views.teacher_detail),
    path("student/", views.StudentView.as_view()),  #class based view
    path("student", views.StudentView.as_view()),
    #path("", include(router.urls)),
    path("student/<int:pk>/", views.StudentDetail.as_view()),
]