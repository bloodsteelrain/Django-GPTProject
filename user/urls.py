from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    # 회원가입
    path('register/', views.RegisterationView.as_view(), name='register'),
    # 로그인
    path('login/', views.LoginView.as_view(), name='login'),
    # 로그아웃
    path('logout/', views.LogoutView.as_view(), name='logout'),
    # 프로필 상세보기
    path('profile/', views.ProfileView.as_view(), name='profile'),
    # 프로필 수정
    path('profile/edit/', views.ProfileEditView.as_view(), name='profile-edit'),
]
