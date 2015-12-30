from django.db import models

class TestModel(models.Model):
	can_interact = models.BooleanField(default=False)
	can_add_fields = models.BooleanField(default=True)
