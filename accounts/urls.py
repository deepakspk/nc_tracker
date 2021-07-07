from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.email_login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),

    path('admins/',views.AdminView.as_view(),name='admins'),
    path('admin/update/<str:pk>/',views.AdminUpdateView.as_view(),name='admin_update'),
    path('admin/delete/<str:pk>/',views.AdminDeleteView.as_view(),name='admin_delete'),

    path('change-password/',auth_views.PasswordChangeView.as_view(
    template_name='accounts/change-password.html', 
    success_url = '/'),
    name='change_password'),   
   

    # path('', include('django.contrib.auth.urls')),
    path("password_reset/",views.password_reset_request, name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),


]
