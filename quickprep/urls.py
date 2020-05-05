from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from users import views as user_views
from content import views as content_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',content_views.QuestionsListView.as_view(),name='home'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login' ),
    path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('register/',user_views.register,name='register'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='reset.html'),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='resetdone.html'),name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='resetconfirm.html'),name='password_reset_confirm'),
    path('password_reset/complete/',auth_views.PasswordResetCompleteView.as_view(template_name='resetcomplete.html'),name='password_reset_complete'),
   
]
