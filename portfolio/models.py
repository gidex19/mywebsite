from django.db import models
from django.utils import timezone
# Create your models here.

software_list = plan_type = (('Web Application','Web Application'), ('Mobile Application','Mobile Application'), ('Desktop Application','Desktop Application'),
                             ('Chatbot','Chatbot'), ('Web Crawler','Web Crawler'), ('Others','Others'))
category_list = (('Personal Project','Personal Project'), ('Business Project','Business Project'), ('Academic/School Project','Academic/School Project'),
                 ('Research Project','Research Project'), ('Others','Others'))
class Customer(models.Model):
    full_name = models.CharField(max_length=70, blank=False)
    email = models.EmailField(max_length=70, blank=False)
    phone_number = models.CharField(max_length=15, blank=False)
    details  = models.TextField(max_length=400, blank=True)
    software_type = models.CharField(choices=software_list, max_length= 30, blank=False)
    category = models.CharField(choices=category_list, max_length=70, blank=True)
    viewed = models.BooleanField(default=False)
    date_sent = models.DateField(default= timezone.now)
