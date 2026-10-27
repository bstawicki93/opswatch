from django.db import models

# Create your models here.
class Endpoint(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(max_length = 200)
    expected_status = models.IntegerField(default = 200)
    enabled = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add = True)

