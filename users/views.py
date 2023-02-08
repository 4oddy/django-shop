from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView

from common.views import DescriptionMixin, TitleMixin
from users.forms import UserLoginForm, UserProfileForm, UserRegistrationForm
from users.models import EmailVerification, User


class UserLoginView(TitleMixin, DescriptionMixin, LoginView):
    template_name = 'user/login.html'
    form_class = UserLoginForm
    title = 'Войти на сайт'
    description = 'Продажа шин и дисков в Екатеринбурге по выгодным ценам в интернет магазине автошин Продажа Шин 96. ' \
                  'Подробная информация о покупке шин и дисков по телефону:+7-961-777-5818'


class UserRegistationView(TitleMixin, DescriptionMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'user/registration.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Вы успешно зарегестрированы!'
    title = 'Регистрация на сайте'
    description = 'Продажа шин и дисков в Екатеринбурге по выгодным ценам в интернет магазине автошин Продажа Шин 96. ' \
                  'Подробная информация о покупке шин и дисков по телефону:+7-961-777-5818'


class UserProfileView(TitleMixin, DescriptionMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'user/profile.html'
    title = 'Личный кобинет'
    description = 'Продажа шин и дисков в Екатеринбурге по выгодным ценам в интернет магазине автошин Продажа Шин 96. ' \
                  'Подробная информация о покупке шин и дисков по телефону:+7-961-777-5818'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))


class EmailVerificationView(TitleMixin, DescriptionMixin, TemplateView):
    title = 'Подтверждение эл.почты'
    template_name = 'user/email_verification.html'
    description = 'Продажа шин и дисков в Екатеринбурге по выгодным ценам в интернет магазине автошин Продажа Шин 96.' \
                  'Подробная информация о покупке шин и дисков по телефону:+7-961-777-5818'

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        user = User.objects.get(email=kwargs['email'])
        email_verifications = EmailVerification.objects.filter(user=user, code=code)
        if email_verifications.exists() and not email_verifications.first().is_expired():
            user.is_verified_email = True
            user.save()
            return super(EmailVerificationView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('index'))

