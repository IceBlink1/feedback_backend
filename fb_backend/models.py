from django.db import models


class Feedback(models.Model):
    feedback = models.CharField(max_length=10000)
    author = models.CharField(max_length=10000)

    class Meta:
        managed = False
        db_table = "fb_backend_feedback"
