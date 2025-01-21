from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    pass

    def __str__(self):
        return f"{self.username} has id: {self.email}"

class Program(models.Model):
    title = models.CharField(max_length=64)
    image = models.URLField()
    days = models.CharField(max_length=64)
    timing = models.CharField(max_length=64)
    details = models.TextField()
    subscribers = models.ManyToManyField(User, blank=True, related_name="subscriptions")

    def __str__(self):
        return f"{self.id}: {self.title}"

class Course(models.Model):
    title = models.CharField(max_length=64)
    subtitle = models.CharField(max_length=100)
    image = models.URLField()
    duration = models.IntegerField()
    details = models.TextField()
    enrollers = models.ManyToManyField(User, blank=True, related_name="enrollments")

    def __str__(self):
        return f"{self.id}: {self.title}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="my_comments")
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user.username,
            "comment": self.comment,
            "timestamp": self.comment_date.strftime("%b %d %Y, %I:%M %p")
        }