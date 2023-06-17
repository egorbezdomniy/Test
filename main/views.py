from django.shortcuts import render,redirect, get_object_or_404
from . import models
from .forms import LiquidForm, SaleForm, SingleForm, PodForm, EvaporatorForm
from django.contrib.contenttypes.models import ContentType
from . import forms
from . import serializers
from datetime import timedelta, datetime
from django.utils import timezone
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import messages
from rest_framework import viewsets, permissions


# Create your views here.
@login_required(login_url='login')
def index(request):
    current_time = timezone.now()
    sales = models.Sale.objects.all()
    week_profit = 0
    month_profit = 0
    day_profit = 0 
    week_turnover = 0
    month_turnover = 0
    day_turnover = 0 
    for sale in sales:
        sold_date = timezone.make_aware(datetime(sale.date.year, sale.date.month, sale.date.day))
        time_difference = current_time - sold_date
        if time_difference <= timedelta(days=30):
            month_profit += (int(sale.sold_for) - int(sale.item.price)) * int(sale.amount_of_sold)
            month_turnover += int(sale.sold_for) * int(sale.amount_of_sold)
        if time_difference <= timedelta(days=7):
            week_profit += (int(sale.sold_for) - int(sale.item.price)) * int(sale.amount_of_sold)
            week_turnover += int(sale.sold_for) * int(sale.amount_of_sold)
        if time_difference <= timedelta(days=1):
            day_profit += (int(sale.sold_for) - int(sale.item.price)) * int(sale.amount_of_sold)
            day_turnover += int(sale.sold_for) * int(sale.amount_of_sold)

    return render(request, 'main/index.html', {
        'sales': sales,
        'week_profit': week_profit,
        'month_profit': month_profit,
        'day_profit': day_profit,
        'week_turnover': week_turnover,
        'month_turnover': month_turnover,
        'day_turnover': day_turnover,
    })


# Вьюхи страницы входа

def logoutView(request):
    logout(request)
    return redirect('index')


def loginView(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Wrong credentials')
            return render(request, 'main/log_reg.html')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Wrong credentials')
            return redirect('login')
    return render(request, 'main/log_reg.html', {
        'page': page
    })


# Изменение предметов

@login_required(login_url='login')
def changeLiquid(request, pk):
    liquid = models.Liquid.objects.get(id=pk)
    form = LiquidForm(instance=liquid)
    if request.method == 'POST':
        form = LiquidForm(request.POST, instance=liquid)
        if form.is_valid():
            form.save()
            return redirect('availability')
    return render(request, 'main/form.html', {
        'form': form,
    })


@login_required(login_url='login')
def changePod(request, pk):
    pod = models.Pod.objects.get(id=pk)
    form = PodForm(instance=pod)
    if request.method == 'POST':
        form = PodForm(request.POST, instance=pod)
        if form.is_valid():
            form.save()
            return redirect('availability')
    return render(request, 'main/form.html', {
        'form': form,
    })



@login_required(login_url='login')
def changeSingle(request, pk):
    single = models.Single.objects.get(id=pk)
    form = SingleForm(instance=single)
    if request.method == 'POST':
        form = SingleForm(request.POST, instance=single)
        if form.is_valid():
            form.save()
            return redirect('availability')
    return render(request, 'main/form.html', {
        'form': form,
    })



@login_required(login_url='login')
def changeEvaporator(request, pk):
    evaporator = models.Evaporator.objects.get(id=pk)
    form = EvaporatorForm(instance=evaporator)
    if request.method == 'POST':
        form = EvaporatorForm(request.POST, instance=evaporator)
        if form.is_valid():
            form.save()
            return redirect('availability')
    return render(request, 'main/form.html', {
        'form': form,
    })




@login_required(login_url='login')
def sales(request):
    sales = models.Sale.objects.all()
    profit = 0
    for sale in sales:
        profit += (int(sale.sold_for) - int(sale.item.price)) * int(sale.amount_of_sold)

    return render(request, 'main/sales.html', {
        'sales': sales,
        'profit': profit
    })


@login_required(login_url='login')
def availability(request):
    liquidBrands = models.LiquidBrand.objects.all()
    singleBrands = models.SingleBrand.objects.all()
    podBrands = models.PodBrand.objects.all()
    evaporatorBrands = models.EvaporatorBrand.objects.all()
    return render(request, 'main/availability.html', {
        'liquidBrands': liquidBrands,
        'singleBrands': singleBrands,
        'podBrands': podBrands,
        'evaporatorBrands': evaporatorBrands

    })

@login_required(login_url='login')
def create_sale(request, type, item_id):
    if type == 'Liquid':
        item = models.Liquid.objects.get(id=item_id)
    elif type == 'Pod':
        item = models.Pod.objects.get(id=item_id)
    elif type == 'Single':
        item = models.Single.objects.get(id=item_id)
    elif type == 'Evaporator':
        item = models.Evaporator.objects.get(id=item_id)
    else:
        # Обработка ошибки дописать
        return redirect('index')  

    if request.method == 'POST':
        form = forms.SaleForm(request.POST)
        if form.is_valid():
            sale = form.save(commit=False)
            sale.item = item
            sale.content_type = models.ContentType.objects.get_for_model(item)
            
            item.amount -= sale.amount_of_sold
            item.save()
            sale.save()
            if type == 'Liquid':
                return redirect('liquidBrand', pk=item.brand.name)
            elif type == 'Pod':
                return redirect('podBrand', pk=item.brand.name)
            elif type == 'Single':
                return redirect('singleBrand', pk=item.brand.name)
            elif type == 'Evaporator':
                return redirect('evaporatorBrand', pk=item.brand.name)
    else:
        form = forms.SaleForm(initial={'content_type': models.ContentType.objects.get_for_model(item),
                                       'object_id': item.id,
                                       'item': item,
                                       'sold_for': int(item.price)+int(item.margin)})
    return render(request, 'main/create_sale.html', {'form': form})



# Бренды

@login_required(login_url='login')
def liquidBrand(request, pk):
    brand = models.LiquidBrand.objects.get(name=pk)
    goods = brand.liquid_set.all()
    type = 'Liquid'
    return render(request, 'main/brand.html', {
        'brand': brand,
        'goods': goods,
        'type': type,
    })

@login_required(login_url='login')
def singleBrand(request, pk):
    brand = models.SingleBrand.objects.get(name=pk)
    goods = brand.single_set.all()
    type = 'Single'
    return render(request, 'main/brand.html', {
        'brand': brand,
        'goods': goods,
        'type' : type
        })

@login_required(login_url='login')
def podBrand(request, pk):
    brand = models.PodBrand.objects.get(name=pk)
    goods = brand.pod_set.all()
    type = 'Pod'
    return render(request, 'main/brand.html', {
        'brand': brand,
        'goods': goods,
        'type' : type
        })

@login_required(login_url='login')
def evaporatorBrand(request, pk):
    brand = models.EvaporatorBrand.objects.get(name=pk)
    goods = brand.evaporator_set.all()
    type = 'Evaporator'
    return render(request, 'main/brand.html', {
        'brand': brand,
        'goods': goods,
        'type' : type
        })



# Экземпляры товара

@login_required(login_url='login')
def liquid(request, pk):
    liquid = models.Liquid.objects.get(id=pk)
    rozn = int(liquid.price) + int(liquid.margin)
    type = 'Liquid'
    return render(request, 'main/good.html', {
        'good': liquid,
        'rozn': rozn,
        'type': type
    })

@login_required(login_url='login')
def pod(request, pk):
    pod = models.Pod.objects.get(id=pk)
    rozn = int(pod.price) + int(pod.margin)
    type = 'Pod'
    return render(request, 'main/good.html', {
        'good': pod,
        'rozn': rozn,
        'pod': True,
        'type': type
    })

@login_required(login_url='login')
def single(request, pk):
    single = models.Single.objects.get(id=pk)
    rozn = int(single.price) + int(single.margin)
    type = 'Single'
    return render(request, 'main/good.html', {
        'good': single,
        'rozn': rozn,
        'type': type
    })

@login_required(login_url='login')
def evaporator(request, pk):
    evaporator = models.Evaporator.objects.get(id=pk)
    rozn = int(evaporator.price) + int(evaporator.margin)
    type = 'Evaporator'
    return render(request, 'main/good.html', {
        'good': evaporator,
        'rozn': rozn,
        'type': type
    })



# Типы товара

@login_required(login_url='login')
def liquids(request):
    name = 'Жидкости'
    liquid_list = models.Liquid.objects.all()
    return render(request, 'main/goods.html', {
        'goods': liquid_list,
        'name': name
    })

@login_required(login_url='login')
def pods(request):
    name = 'Поды'
    pod_list = models.Pod.objects.all()
    return render(request, 'main/goods.html', {
        'goods': pod_list,
        'name': name
    })

@login_required(login_url='login')
def singles(request):
    name = 'Одноразки'
    single_list = models.Single.objects.all()
    return render(request, 'main/goods.html', {
        'goods': single_list,
        'name': name
    })

@login_required(login_url='login')
def evaporators(request):
    name = 'Испарители'
    evaporator_list = models.Evaporator.objects.all()
    return render(request, 'main/goods.html', {
        'goods': evaporator_list,
        'name': name
    })



# api viewsets
class LiquidViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.LiquidSerializer
    queryset = models.Liquid.objects.all()


class SingleViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.SingleSerializer
    queryset = models.Single.objects.all()


class PodViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.PodSerializer
    queryset = models.Pod.objects.all()


class EvaporatorViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.EvaporatorSerializer
    queryset = models.Evaporator.objects.all()


class LiquidBrandViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.LiquidBrandSerializer
    queryset = models.LiquidBrand.objects.all()


class SingleBrandViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.SingleBrandSerializer
    queryset = models.SingleBrand.objects.all()


class PodBrandViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.PodBrandSerializer
    queryset = models.PodBrand.objects.all()


class EvaporatorBrandViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.EvaporatorBrandSerializer
    queryset = models.EvaporatorBrand.objects.all()




