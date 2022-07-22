from django.contrib import admin
from .models import Course, Detail, Item, CourseComment
from embed_video.admin import AdminVideoMixin
# Register your models here.

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Course)
admin.site.register(Detail)
admin.site.register(Item, MyModelAdmin)
admin.site.register(CourseComment)