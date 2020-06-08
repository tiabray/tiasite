from django.db import models
from django.contrib.auth.models import User

# admin.site.register(<Name of model>)
admin.site.register(Instance)
admin.site.register(Card)
admin.site.register(Card_Status)
admin.site.register(Queue_Status)
admin.site.register(Queue)

# Create your models here.
# class Person(models.Model):
#     first_name = models.CharField(max_length=30)
#
#         last_name =
#     models.CharField(max_length=30)
#
# CREATE TABLE myapp_person (
#     "id" serial NOT NULL PRIMARY KEY,
#     "first_name" varchar(30) NOT NULL,
#     "last_name" varchar(30) NOT NULL
# );

class Instance(models.model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    queue = models.ManytoMany(Queue)

class Card(models.model):
    # id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Queue, on_delete=models.CASCADE)
    card_status = models.ForeignKey(CardStatus, on_delete=models.CASCADE)
    queue_timestamp = models.DateField()
    position = models.PositiveIntegerField()
    head_timestamp = models.DateField()
    defer_count = models.PositiveIntegerField()
    time_to_completion = models.DurationField()

class Card_Status(models.model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)

class Queue_Status(models.model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)

class Queue(models.model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    card = models.ManytoMany(Card)
    queue_status = models.ForeignKey(QueueStatus, on_delete=models.CASCADE)
    head_card = models.ForeignKey(Card, on_delete=models.CASCADE)
    mins_to_auto_defer = models.PositiveIntegerField()
    num_times_defer = models.PositiveIntegerField()
    num_times_in_queue = models.PositiveIntegerField()
    display_position_only = models.BooleanField(default=True)
    display_completion_time = models.BooleanField(default=True)