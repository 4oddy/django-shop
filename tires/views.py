from django.shortcuts import render
from common.views import DescriptionMixin, TitleMixin
from django.views.generic.base import TemplateView


class TiresView(TitleMixin, DescriptionMixin, TemplateView):
    template_name = 'tires/payment.html'
    title = 'Шины'
    description = 'Продажа шин и дисков в Екатеринбурге по выгодным ценам в интернет магазине автошин Продажа Шин 96. ' \
                  'Подробная информация о покупке шин и дисков по телефону: +7-961-777-5818'

