from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=500)
    createdAt = models.DateTimeField('date created')

    def __str__(self):
        return self.username

class Memo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    memo_text = models.TextField

    def __str__(self):
        return self.memo_text