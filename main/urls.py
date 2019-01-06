from django.conf.urls import url

from main import views

urlpatterns=[
    url('login/', views.login),
    url('signup/', views.signup),
    url('dashboard/', views.dashboard),
    url('credit/', views.credit),
    url('debit/', views.debit),
    url('Account_statement/', views.Account_statement),
    url('transfer/', views.transfer),
    url('', views.homePageView),
    ]
