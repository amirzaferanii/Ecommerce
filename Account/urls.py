from django.urls import path
from . import views

app_name = 'account'


urlpatterns = [
    path('login', views.UserLoginView.as_view(), name='login'),
    path('otp_login', views.OtpLoginView.as_view(), name='otp_login_request'),
    path('check_otp_login', views.CheckOtpLoginView.as_view(), name='check_otp_login'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('check_otp', views.CheckOtpView.as_view(), name='check_otp'),
    path('logout', views.UserLogoutView.as_view(), name='logout'),
    path('reset_password_request', views.ResetPasswordRequestView.as_view(), name='reset_password_request'),
    path('reset_password_confirm', views.ResetPasswordConfirmView.as_view(), name='reset_password_confirm'),
    path('reset-password-complete/', views.ResetPasswordCompleteView.as_view(), name='reset_password_complete'),
    path('add_address', views.AddAddressView.as_view(), name='add_address'),
    path('profile/<str:slug>', views.UserProfileView.as_view(), name='profile'),
    path('profile/edit/photo/<str:slug>', views.UserProfilePhotoEditView.as_view(), name='profile_edit_photo'),
    path('profile/edit/fullname/<str:slug>', views.UserProfileFullnameEditView.as_view(), name='profile_edit_fullname'),
    path('profile/edit/email/<str:slug>', views.UserProfileEmailEditView.as_view(), name='profile_edit_email'),
    path('profile/edit/bio/<str:slug>', views.UserProfileBioEditView.as_view(), name='profile_edit_bio'),


]