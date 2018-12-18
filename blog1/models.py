from django.db import models

# Create your models here.
#
# class comment_info(models.Model):
#     id = models.IntegerField(primary_key=True)
#     user_name = models.CharField(max_length=50)
#     user_id = models.IntegerField()
#     content = models.CharField(max_length=50)
#     create_time = models.DateField()

class message_info(models.Model):
    id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=50)
    user_id = models.IntegerField()
    content = models.CharField(max_length=50)
    create_time = models.DateTimeField()

