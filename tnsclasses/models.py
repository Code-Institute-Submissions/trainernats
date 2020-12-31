from django.db import models
import datetime


class Day(models.Model):
    day = models.CharField(max_length=254)
    friendly_name = models.CharField(
                                    max_length=254,
                                    null=True,
                                    blank=True
                                    )
    class_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.day

    def get_friendly_name(self):
        return self.friendly_name


class Class_Type(models.Model):
    class_type = models.CharField(
                                max_length=254,
                                null=True,
                                blank=True
                                )

    def __str__(self):
        return self.class_type


class TNS_Class(models.Model):
    day = models.ForeignKey(
                            'Day',
                            null=True,
                            blank=True,
                            on_delete=models.SET_NULL
                            )
    class_type = models.ForeignKey(
                                    'Class_Type',
                                    null=True,
                                    blank=True,
                                    on_delete=models.SET_NULL
                                    )
    class_name = models.CharField(max_length=254)
    class_description = models.TextField()
    class_more_detail = models.TextField(null=True,
                                         blank=True
                                         )
    price = models.DecimalField(
                                max_digits=6,
                                decimal_places=2
                                )
    image_url = models.URLField(
                                max_length=1024,
                                null=True,
                                blank=True
                                )
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.class_name
