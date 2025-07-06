from django.db import models
from django.utils import timezone
from datetime import timedelta

class DrawOffset(models.Model):
    offset_seconds = models.IntegerField(default=0)
    scheduled_draw_time = models.DateTimeField(null=True, blank=True)

    @classmethod
    def get_offset(cls):
        instance, _ = cls.objects.get_or_create(pk=1)
        return timedelta(seconds=instance.offset_seconds)

    @classmethod
    def add_offset(cls, minutes, seconds):
        instance, _ = cls.objects.get_or_create(pk=1)
        instance.offset_seconds += minutes * 60 + seconds
        instance.save()

    @classmethod
    def reset_offset(cls):
        instance, _ = cls.objects.get_or_create(pk=1)
        instance.offset_seconds = 0
        instance.scheduled_draw_time = None
        instance.save()

    @classmethod
    def set_scheduled_draw(cls, dt):
        instance, _ = cls.objects.get_or_create(pk=1)
        instance.scheduled_draw_time = dt
        instance.save()

    @classmethod
    def get_scheduled_draw(cls):
        instance, _ = cls.objects.get_or_create(pk=1)
        return instance.scheduled_draw_time

class LotteryResult(models.Model):
    date = models.DateField(auto_now_add=True)
    time_slot = models.TimeField()
    row = models.IntegerField()
    column = models.IntegerField()
    number = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)
    # editable_until = models.DateTimeField()
    # def is_editable(self):
    #     return timezone.now() <= self.editable_until

    @property
    def first_two_digits(self):
        return f"{self.row * 10 + self.column:02}"

    @property
    def last_two_digits(self):
        return self.number[2:]

    @property
    def is_editable(self):
        return True 

