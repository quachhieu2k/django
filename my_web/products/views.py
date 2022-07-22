from django.shortcuts import render, redirect
from .models import Course, Detail, Item, CourseComment
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, logout, login, user_login_failed
from django.http import HttpResponseRedirect
from .forms import UserLoginForm, UserRegisterForm

def index(request, *args, **kwargs):
    course = Course.objects.all()
    detail = Detail.objects.all()

    return render(request, 'products/index.html', {'course':course, 'detail':detail})
def detail(request, pr_id, id, **kwargs):
    course = Course.objects.all()
    detail = Detail.objects.get(id= id)
    obj_vid = Item.objects.get(id= id)
    par_id = Detail.objects.filter(parent_id= pr_id)
    video = Detail.objects.filter(id=id).first()
    course_comment = CourseComment.objects.filter(course_detail= video)

    return render(request, 'products/detail.html', {'course':course, 'detail':detail,
                                                    'obj_vid': obj_vid, 'details':par_id,
                                                    'video': video, 'course_comment': course_comment},)


def login_view(request, *args, **kwargs):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username= username, password= password)

        login(request, user)
        return redirect('/')

    return render(request, 'accounts/login.html', {'form' : form})


def register_view(request, *args, **kwargs):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit= False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()

        user_new = authenticate(username=user.username, password=password)
        login(request, user)
        return redirect('/')

    return render(request, 'accounts/register.html', {'form' : form})

def logout_view(request):
    logout(request)
    return redirect('/')


def videoComment(request):
    if request.user.is_authenticated == True:
        if request.method == 'POST':
            comment = request.POST['comment']
            detail_id = request.POST['detail_id']
            video = Detail.objects.filter(id= detail_id).first()
            new_comment = CourseComment(
                comment=comment,
                user=request.user,
                course_detail=video)
            new_comment.save()

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return redirect('home')


