# TODO настройте здесь urls для заданий сourses, new_courses, find_by_name, who's_author
from django.urls import path
from courses import views


urlpatterns = [
    path('', views.courses),
    path('new/', views.new_courses),
    path('one_obj/<slug:slug>/', views.get_course),
    path('one_obj/', views.get_course_empty),
    path('search/', views.search),
]
