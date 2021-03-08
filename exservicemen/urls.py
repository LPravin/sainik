from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('apply/', views.applyview, name="apply"),
    path('registration/', views.personalformview, name="registration"),
    path('registration/discharge-details', views.dischargeformview, name="discharge details"),
    path('registration/employment-details', views.employementformview, name='employment details'),
    path('registration/spouse-details', views.spouseformview, name='spouse details'),
    path('registration/dependent-details', views.dependentformview, name='dependent details'),
    path('user-login/', views.userlogin, name="user login"),
    path('officer-login/', views.officerlogin, name="officer login"),
    path('ajax/load-record-office/', views.load_record_office, name='ajax_load_records'),
    path('ajax/load-trades/', views.load_trades, name='ajax_load_trades'),
    path('ajax/load-ranks/', views.load_ranks, name='ajax_load_ranks'),
    path('ajax/load-disrticts/', views.load_districts, name='ajax_load_districts'),
    path('logout/', views.userlogout, name='logout'),
]