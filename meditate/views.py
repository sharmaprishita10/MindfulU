from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
import json

from .models import *

# Create your views here.
def index(request):
    return render(request, "meditate/index.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "meditate/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "meditate/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "meditate/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "meditate/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "meditate/register.html")


@csrf_exempt
def subscribe(request, prog_id):
    # Query for requested program
    try:
        program = Program.objects.get(pk=prog_id)
    except Program.DoesNotExist:
        return JsonResponse({"error": "Program not found."}, status=404)

    # GET follower and following count
    if request.method == "GET":
        return JsonResponse({
            "subscribers" : program.subscribers.count()
        })
    # Subscribe/Unsubscribe request
    elif request.method == "PUT":

        if request.user.is_authenticated:
            subscriber_row = Program.objects.filter(pk=prog_id, subscribers=request.user).first()
            if subscriber_row is None:      # Currently the user is not subscribed
                program.subscribers.add(request.user)
                title = "Unsubscribe"
            else:
                program.subscribers.remove(request.user)        # The user is subscribed
                title = "Subscribe"
                    
            return JsonResponse({
                "title" : title
            })

    else:
        return JsonResponse({
            "error": "GET or PUT request required."
        }, status=400)

@csrf_exempt
def enroll(request, course_id):
    # Query for requested course
    try:
        course = Course.objects.get(pk=course_id)
    except Course.DoesNotExist:
        return JsonResponse({"error": "Course not found."}, status=404)

    # GET follower and following count
    if request.method == "GET":
        return JsonResponse({
            "enrollers" : course.enrollers.count()
        })
    # Enroll/Unenroll request
    elif request.method == "PUT": 
        if request.user.is_authenticated:
            enroller_row = Course.objects.filter(pk=course_id, enrollers=request.user).first()
            if enroller_row is None:      # Currently the user is not enrolled 
                course.enrollers.add(request.user)
                title = "Unenroll"
            else:
                course.enrollers.remove(request.user)        # The user is enrolled
                title = "Enroll"
                    
            return JsonResponse({
                "title" : title
            })

    else:
        return JsonResponse({
            "error": "GET or PUT request required."
        }, status=400)

@csrf_exempt
def comments(request, prog_id):

    # Query for requested program
    try:
        program = Program.objects.get(pk=prog_id)
    except Program.DoesNotExist:
        return JsonResponse({"error": "Program not found."}, status=404)

    # GET all the comments of the given program
    if request.method == "GET":
        comments = program.comments.all()

        # Return comments in reverse chronologial order
        comments = comments.order_by("-comment_date").all()

        return JsonResponse([comment.serialize() for comment in comments], safe=False)
    # POST the new comment on the given program
    elif request.method == "POST":
        if request.user.is_authenticated:
            # Get contents of the comment
            data = json.loads(request.body)
            comment = data.get("comment", "")

            # Create the new comment object
            new_comment = Comment(user = request.user, program = program, comment=comment)
            new_comment.save()

            return JsonResponse({"message": "Your comment is published successfully."}, status=201)
        else:
            return HttpResponseRedirect(reverse("login"))
    else:
        return JsonResponse({
            "error": "GET or POST request required."
        }, status=400)

def programs(request):

    return render(request, "meditate/programs.html", {
        "programs" : Program.objects.all()
    })

def program(request, prog_id):
    # Query for requested program
    try:
        program = Program.objects.get(pk=prog_id)
    except Program.DoesNotExist:
        return JsonResponse({"error": "Program not found."}, status=404)

    if request.user.is_authenticated:
        subscriber_row = Program.objects.filter(pk=prog_id, subscribers=request.user).first()
        if subscriber_row is None:      # Currently the user is not subscribed
            title = "Subscribe"
        else:                           # The user is subscribed
            title = "Unsubscribe"
    else:
        title = "Subscribe"

    return render(request, "meditate/program.html", {
        "program" : program,
        "title" : title
    })

def courses(request):

    return render(request, "meditate/courses.html", {
        "courses" : Course.objects.all()
    })

def course(request, course_id):
    # Query for requested course
    try:
        course = Course.objects.get(pk=course_id)
    except Course.DoesNotExist:
        return JsonResponse({"error": "Course not found."}, status=404)

    if request.user.is_authenticated:
        enroller_row = Course.objects.filter(pk=course_id, enrollers=request.user).first()
        if enroller_row is None:      # Currently the user is not enrolled
            title = "Enroll"
        else:                           # The user is enrolled
            title = "Unenroll"
    else:
        title = "Enroll"

    return render(request, "meditate/course.html", {
        "course" : course,
        "title" : title
    })

@login_required
def enrollments(request):
    return render(request, "meditate/enrollments.html", {
        "programs" : request.user.subscriptions.all(),
        "courses" : request.user.enrollments.all()
    })

def about(request):
    return render(request, "meditate/about.html")