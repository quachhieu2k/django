from django.shortcuts import render
from .models import Course, Detail, Item
# Create your views here.
def index(request, *args, **kwargs):
    course = Course.objects.all()
    detail = Detail.objects.all()

    return render(request, 'products/index.html', {'course':course, 'detail':detail})
def detail(request, pr_id, id, **kwargs):
    course = Course.objects.all()
    detail = Detail.objects.get(id= id)
    obj_vid = Item.objects.get(id= id)
    par_id = Detail.objects.filter(parent_id= pr_id)

    return render(request, 'products/detail.html', {'course':course, 'detail':detail,
                                                    'obj_vid': obj_vid, 'details':par_id})