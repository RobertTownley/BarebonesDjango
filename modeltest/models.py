from django.db import models

class TestModel(models.Model):
	can_interact = models.BooleanField(default=False)
