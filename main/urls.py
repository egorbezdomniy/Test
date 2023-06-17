from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('availability', views.availability, name='availability'),

    path('liquid/<str:pk>', views.liquid, name='liquid'),
    path('pod/<str:pk>', views.pod, name='pod'),
    path('single/<str:pk>', views.single, name='single'),
    path('evaporator/<str:pk>', views.evaporator, name='evaporator'),

    path('liquids', views.liquids, name='liquids'),
    path('pods', views.pods, name='pods'),
    path('singles', views.singles, name='singles'),
    path('evaporators', views.evaporators, name='evaporators'),

    path('sales', views.sales, name='sales'),

    path('liquidBrand/<str:pk>', views.liquidBrand, name='liquidBrand'),
    path('singleBrand/<str:pk>', views.singleBrand, name='singleBrand'),
    path('podBrand/<str:pk>', views.podBrand, name='podBrand'),
    path('evaporatorBrand/<str:pk>', views.evaporatorBrand, name='evaporatorBrand'),

    path('changeLiquid/<str:pk>', views.changeLiquid, name='changeLiquid'),
    path('changePod/<str:pk>', views.changePod, name='changePod'),
    path('changeSingle/<str:pk>', views.changeSingle, name='changeSingle'),
    path('changeEvaporator/<str:pk>', views.changeEvaporator, name='changeEvaporator'),

    path('create_sale/<str:type>/<int:item_id>/', views.create_sale, name='create_sale'),

    path('login', views.loginView, name='login'),   
    path('logout', views.logoutView, name='logout'), 


    path('api')
]