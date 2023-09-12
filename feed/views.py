from django.shortcuts import redirect, render

from .forms import PostModelForm
from .models import Post
# from django.views.generic import TemplateView


# class HomePageView(TemplateView):
#     template_name = "home.html"


def Home(request):
    task_list = Post.objects.all()
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PostModelForm()
    return render(request, "home.html", {"form": form, "task_list": task_list})