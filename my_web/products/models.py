from django.db import models
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100, db_collation='utf8_general_ci', blank=True, null=True)
    teacher = models.CharField(max_length=50, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    summary = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return f"{self.name}, {self.teacher}, {self.summary}"



class Detail(models.Model):
    title = models.CharField(max_length=100, db_collation='utf8_general_ci', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    duration = models.CharField(max_length=50, blank=True, null=True)
    parent = models.ForeignKey(Course, models.DO_NOTHING)
    thumbnail = models.ImageField(upload_to='images/')
    link_video_ytb = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.title}, {self.description}, {self.duration}, {self.link_video_ytb}"


class CourseComment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course_detail = models.ForeignKey(Detail, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.id} - {self.user.username} - {self.comment[0:15]} ..."


class Item(models.Model):
    video = EmbedVideoField()
