from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('apply/', views.ApplyView.as_view(), name="apply"),
    path('registration/', views.RegistrationFormView.as_view(), name="registration"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('registration/personal-details', views.PersonalFormView.as_view(), name='personal details'),
    path('registration/employment-details', views.EmploymentFormView.as_view, name='employment details'),
    path('registration/spouse-details', views.SpouseFormView.as_view(), name='spouse details'),
    path('registration/dependent-details', views.DependentFormView.as_view(), name = 'dependent details')
]