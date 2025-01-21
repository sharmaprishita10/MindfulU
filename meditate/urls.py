from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("programs", views.programs, name="programs"),
    path("program/<int:prog_id>", views.program, name="program"),
    path("courses", views.courses, name="courses"),
    path("course/<int:course_id>", views.course, name="course"),
    path("enrollments", views.enrollments, name="enrollments"),
    path("about", views.about , name="about"),

    # API routes
    path("subscribe/<int:prog_id>", views.subscribe, name="subscribe"),         # GET and PUT requests
    path("enroll/<int:course_id>", views.enroll, name="enroll"),                # GET and PUT requests
    path("comments/<int:prog_id>", views.comments, name="comments")             # GET request and POST requests
]
    