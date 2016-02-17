from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Assumptions(models.Model):
    installers_start = models.IntegerField(default=1)
    installers_weekly_growth = models.FloatField(default=0.10)
    deal_frequency_in_weeks = models.IntegerField(default=8)
    deal_latency_in_weeks = models.IntegerField(default=4)
    deal_revenue_thousands = models.IntegerField(default=5)
    
class Weekly(models.Model):
    assumptions = models.ForeignKey(Assumptions, on_delete=models.CASCADE)
    installers_current = models.FloatField()
    installers_count = models.IntegerField()
    deals_count = models.IntegerField()
    deals_revenue = models.IntegerField()
    deals_revenue_cumulative = models.IntegerField()