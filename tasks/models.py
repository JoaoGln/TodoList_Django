from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    completed = models.BooleanField(default=False, verbose_name="Concluído")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['completed', '-created_at']