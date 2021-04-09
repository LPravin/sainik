from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeview, name='home'),
    # path('apply/', views.applyview, name="apply"),
    # path('registration/', views.serviceformview, name="service details"),
    path('registration/pension-info', views.pensionformview, name="pension details"),
    path('registration/personal-info', views.personalformview, name="personal details"),
    path('registration/employment-info', views.employmentformview, name='employment details'),
    path('registration/spouse-info', views.spouseformview, name='spouse details'),
    path('registration/dependent-info', views.dependentformview, name='dependent details'),
    path('registration/contact-info', views.contactformview, name='contact details'),
    path('user-login/', views.userlogin, name="user login"),
    path('officer-login/', views.officerlogin, name="officer login"),
    path('ajax/load-record-office/', views.load_record_office, name='ajax_load_records'),
    path('ajax/load-trades/', views.load_trades, name='ajax_load_trades'),
    path('ajax/load-ranks/', views.load_ranks, name='ajax_load_ranks'),
    path('ajax/load-disrticts/', views.load_districts, name='ajax_load_districts'),
    path('registration/ajax/load_dependent/', views.load_dependent, name='ajax_load_dependent'),
    path('registration/ajax/add_dependent/', views.add_dependent, name='ajax_add_dependent'),
    path('registration/ajax/<int:pk>/update', views.update_dependent, name='ajax_update_dependent'),
    # path('ajax/load-mcs/', views.load_mcs, name='ajax_load_mcs'),
    path('logout/', views.userlogout, name='logout'),
    path('addesm/', views.addesm, name='add ESM'),
    path('addesm/basic-info', views.addbasicinfo, name='basic details'),
    path('addesm/service-info', views.serviceformview, name='service details'),

]