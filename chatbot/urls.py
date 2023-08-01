from django.urls import path
from . import views

app_name = 'chatbot'

urlpatterns = [
    # 챗봇에 질문하기
    path('', views.ChatbotView.as_view(), name='chat'),
    # 챗봇 마지막 질문+답변 지우기
    path('', views.ClearChatView.as_view(), name='clearchat')
]
