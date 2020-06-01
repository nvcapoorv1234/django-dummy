from django.db import models
from datetime import datetime
class LandingPageVisitor(models.Model):
   visit_date=models.DateField((u"Conversation Date"), blank=True)
   visit_time=models.TimeField((u"Conversation Time"), blank=True)

   
class BalanceActivity(models.Model):
    user_name=models.CharField(max_length=20,null=True, blank=True)
    visit_date=models.DateField((u"Conversation Date"), blank=True)
    visit_time=models.TimeField((u"Conversation Time"), blank=True)

class LoanActivity(models.Model):
    user_name=models.CharField(max_length=20,null=True, blank=True)
    visit_date=models.DateField((u"Conversation Date"), blank=True)
    visit_time=models.TimeField((u"Conversation Time"), blank=True)

class FundsActivity(models.Model):
    user_name=models.CharField(max_length=20,null=True, blank=True)
    visit_date=models.DateField((u"Conversation Date"), blank=True)
    visit_time=models.TimeField((u"Conversation Time"), blank=True)
