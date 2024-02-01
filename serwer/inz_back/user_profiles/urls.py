from django.urls import path
from .views import LoginView, LogoutView, UserRegistrationView, UserDetailView, EditUserProfileView, DeleteUserView, PasswordResetRequestView, PasswordResetConfirmView


urlpatterns = [
    path('api/login/', LoginView.as_view(), name='api_login'),
    path('api/logout/', LogoutView.as_view(), name='api_logout'),
    path('api/register/', UserRegistrationView.as_view(), name='api_register'),
    path('api/user-detail/', UserDetailView.as_view(), name='api_user_detail'),
    path('api/edit-profile/', EditUserProfileView.as_view(), name='edit_profile'),
    path('api/delete-user/', DeleteUserView.as_view(), name='delete-user'),
    path('api/password-reset-request/', PasswordResetRequestView.as_view(), name='password_reset_request'),
    path('api/password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

]

