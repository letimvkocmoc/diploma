from django.urls import path

import views

urlpatterns = [
    path("signup", views.SingupView.as_view(), name="signup"),
    path("login", views.LoginView.as_view(), name="login"),
    path("profile", views.ProfileView.as_view(), name="profile"),
    path("update_password", views.UpdatePasswordView.as_view(), name="update_password"),
]
