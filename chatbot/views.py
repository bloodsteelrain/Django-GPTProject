from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth import get_user_model
from .models import Conversation
import openai

User = get_user_model()


class ChatbotView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        conversations = Conversation.objects.filter(user=user)
        serialized_conversations = [
            {'prompt': c.prompt, 'response': c.response} for c in conversations]
        return Response({'conversations': serialized_conversations}, status=status.HTTP_200_OK)

    def post(self, request):
        prompt = request.data.get('prompt')
        if prompt:
            user = request.user

            # 데이터베이스에서 과거 대화들 가져오기
            previous_conversations = Conversation.objects.filter(
                user=user).order_by('id')
            previous_conversations_text = "\n".join(
                [f"User: {c.prompt}\nAssistant: {c.response}" for c in previous_conversations])

            # 과거 대화들을 새 질문과 합치기
            prompt_with_previous = f"{previous_conversations_text}\nUser: {prompt}\nAssistant:"

            # OpenAI를 사용해 AI의 답변을 생성하기
            model_engine = "text-davinci-003"
            completions = openai.Completion.create(
                engine=model_engine,
                prompt=prompt_with_previous,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            response = completions.choices[0].text.strip()

            # 새 질문(prompt)과 답변(response)을 데이터베이스에 저장하기
            conversation = Conversation.objects.create(
                prompt=prompt, response=response, user=user)

            return Response({'prompt': prompt, 'response': response}, status=status.HTTP_200_OK)
        return Response({'error': 'Prompt field is required.'}, status=status.HTTP_400_BAD_REQUEST)
