from django.db import models
from django.urls import reverse
from datetime import date

FED = (
    ('N', 'watered and not fed on'),
    ('Y', 'watered and fed on')
)

STATES = (
    ('A', 'Actively Growing'),
    ('D', 'Dormant'),
    ('R', 'Rehabbing: Health Declining.')
)

class Pot(models.Model):
    vessel = models.CharField(max_length=20)
    medium = models.CharField(max_length=200)

    def __str__(self):
        return self.vessel
    
    def get_absolute_url(self):
        return reverse('pots_detail', kwargs={'pk': self.id})
    
    
class Plant(models.Model):
    species = models.CharField(max_length=100)
    common_name = models.CharField(max_length=100)
    genus = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    pots = models.ManyToManyField(Pot)

    def __str__(self):
        return f'{self.species} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'plant_id': self.id})
    
    def watered_today(self):
        return self.watered_set.filter(date=date.today()).count() >= len(FED)
    
class Watered(models.Model):
    date = models.DateField('watered date')
    fed = models.CharField(
        max_length=1,
        choices=FED,
        default=FED[0][0]
        )
    
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    def __str__(self):
      return f"{self.get_fed_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']

class Status(models.Model):
    date = models.DateField('Status Date')
    no_of_leaves = models.IntegerField()
    state = models.CharField(
        max_length=1,
        choices=STATES,
        default=STATES[0][0]
    )
    status_log = models.CharField(max_length=1000)

    plant = models.ForeignKey(
        Plant,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.get_state_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']






# Create your models here.
