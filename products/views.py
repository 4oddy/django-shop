from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from common.views import DescriptionMixin, TitleMixin
from products.models import Basket, Product, ProductCategory

# Create your views here.


class IndexView(TitleMixin, DescriptionMixin, TemplateView):
    template_name = 'products/index.html'
    title = 'Шины и Диски в Екатеринбург'
    description = 'Продажа шин и дисков в Екатеринбурге по выгодным ценам в интернет магазине автошин Продажа Шин 96. ' \
                  'Подробная информация о покупке шин и дисков по телефону: +7-961-777-5818'


class ProductsListView(TitleMixin, DescriptionMixin, ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 20
    title = 'Каталог'
    description = 'Продажа шин и дисков в Екатеринбурге по выгодным ценам в интернет магазине автошин Продажа Шин 96. ' \
                  'Подробная информация о покупке шин и дисков по телефону:+7-961-777-5818'

    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data()
        context['categories'] = ProductCategory.objects.all()
        return context


# Функция корзины(Добавляет)
@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user,  product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity +=1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


# Функция корзины(Убирает)
@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

