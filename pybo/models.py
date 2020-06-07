# [/Users/candicehan/projects/mysite/pybo/models.py]
# ---------------------------------------- [edit] ---------------------------------------- #
from django.db import models
from django.contrib.auth.models import User

""" 장고의 기능을 개발하는 패턴 
1. 템플릿에 추가 기능을 위한 링크(버튼 등) 추가 
2. urls.py에 링크에 해당하는 url 매핑을 작성 
3. forms.py에 폼 작성(폼이 필요 없는 경우에는 생략)
4. 함수에서 사용하는 템플릿 작성 """

# Create your models here.


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(
        null=True, blank=True)  # 수정일시는 수정이 발생할 경우에만 생성되는 데이터
    voter = models.ManyToManyField(User, related_name='voter_question')

    def __str__(self):
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(
        Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(
        Answer, null=True, blank=True, on_delete=models.CASCADE)

# ---------------------------------------------------------------------------------------- #
