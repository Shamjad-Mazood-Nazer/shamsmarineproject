from django.db import models


# Create your models here.

class ContactUs(models.Model):
    full_name = models.CharField(max_length=50, verbose_name='Full Name')
    email = models.CharField(max_length=50, verbose_name='Email Address')
    phone = models.CharField(max_length=15, verbose_name='Contact Number')
    comment = models.TextField(max_length=500, verbose_name='Enquiry Message')
    date_time = models.DateTimeField(verbose_name='Date & Time', auto_now_add=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = 'Enquiry Details'
