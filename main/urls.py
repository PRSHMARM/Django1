from django.conf.urls import url

from main import views
from My_project import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
    url('login/', views.login),
    url('signup/', views.signup),
    url('dashboard/', views.dashboard),
    url('credit/', views.credit),
    url('debit/', views.debit),
    url('Account_statement/', views.Account_statement),
    url('loginemp/',views.loginemp),
    url('signupemp/',views.signupemp),
    url('transfer/', views.transfer),
    url('dashboardemp/',views.dashboardemp),
    url('', views.homePageView),
    ]
