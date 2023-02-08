from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic.base import View
from django.views.generic.list import ListView
from blog.models import Blog
from common.views import DescriptionMixin, TitleMixin
from .form import CommentsForm


class BlogView(TitleMixin, DescriptionMixin, View):
    """"Вывод записи"""
    title = 'Блог'
    description = 'Продажа шин и дисков в Екатеринбурге по выгодным ценам в интернет магазине автошин Продажа Шин 96. ' \
                  'Подробная информация о покупке шин и дисков по телефону: +7-961-777-5818'

    def get(self, request):
        blogs = Blog.objects.all()     # Указываем что передаем шаблону
        return render(request, 'blog/blog.html', {'blog_list': blogs})


class BlogDetail(TitleMixin, DescriptionMixin, View):
    """"Отдельная страница записи"""
    title = 'Блог'
    description = 'Продажа шин и дисков в Екатеринбурге по выгодным ценам в интернет магазине автошин Продажа Шин 96. ' \
                  'Подробная информация о покупке шин и дисков по телефону: +7-961-777-5818'

    def get(self, request, pk):
        blog = Blog.objects.get(id=pk)
        return render(request, 'blog/blog_detail.html', {'blog': blog})


class AddComments(LoginRequiredMixin, View):
    """Добавление комментария после регистрации"""
    @method_decorator(login_required)
    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.blog_id = pk
            form.save()
        return redirect(f'/blog/{pk}')





