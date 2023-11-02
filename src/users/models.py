from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=65)

    def _str_(self):
        return self(self.name)