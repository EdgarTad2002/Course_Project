from django.urls import path
from . import views
app_name = 'courses'

urlpatterns = [
    path("", views.show_courses, name="view_courses"),
    path("<int:course_id>", views.in_detail, name='in_detail'),
    path("<int:course_id>/rate", views.rate, name='rate_course'),
    path('register', views.register, name='register'),
    path("login", views.login_into, name="login"),
]