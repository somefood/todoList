from django.db import models
from django.conf import settings


class TodoList(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='유저명')
    title = models.CharField(max_length=30, verbose_name='타이틀')
    content = models.TextField(verbose_name='내용')
    is_progressed = models.BooleanField(verbose_name='진행여부', default=False)
    is_completed = models.BooleanField(verbose_name='완료여부', default=False)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "TODO 목록"
        verbose_name_plural = "TODO 목록"