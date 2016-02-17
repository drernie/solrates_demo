from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible  # only if you need to support Python 2
class Assumptions(models.Model):
    installers_start = models.IntegerField(default=1)
    installers_weekly_growth = models.FloatField(default=0.10)
    deal_frequency_in_weeks = models.IntegerField(default=8)
    deal_latency_in_weeks = models.IntegerField(default=4)
    deal_revenue_thousands = models.IntegerField(default=5)

    def __str__(self):
        return "%.2f %% growth of %i ($K) @ %i weeks + %i latency " % (
            self.installers_weekly_growth * 100,
            self.deal_revenue_thousands,
            self.deal_frequency_in_weeks,
            self.deal_latency_in_weeks,
        )
    
class Weekly(models.Model):
    assumptions = models.ForeignKey(Assumptions, on_delete=models.CASCADE)
    week_index = models.IntegerField(default=1)
    installers_current = models.FloatField(default=0.0)
    installers_count = models.IntegerField(default=0)
    deals_count = models.IntegerField(default=0)
    deals_revenue = models.IntegerField(default=0)
    deals_revenue_cumulative = models.IntegerField(default=0)

    def __str__(self):
        return "%i: %i/%i ($K) for %i installers " % (
            self.week_index,
            self.deals_revenue,
            self.deals_revenue_cumulative,
            self.installers_count,
        )

    