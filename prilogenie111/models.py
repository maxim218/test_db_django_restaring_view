from django.db import models
from django.utils import timezone

class MyModelTest(models.Model):
    contentA = models.TextField()
    contentB = models.TextField()

    def __str__(self):
        return str(self.contentA) + "__" + str(self.contentB)


