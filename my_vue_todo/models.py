from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    contents = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.id) + " " + self.contents

