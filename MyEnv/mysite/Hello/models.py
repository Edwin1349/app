from django.db import models
from django.contrib.auth.models import User as U
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Family(models.Model):
    familyName = models.CharField(max_length=20, blank=True, null=True, unique=True)
    key = models.CharField(max_length=20, blank=True, null=True)
    class Meta:
        unique_together = ["familyName", "key"]

    #password = models.CharField(max_length=20, blank=True, null=True)
    #def add_person(self, person):
        #if self.percon_set.count() <= 3:
            #raise Exception("need more people to create family")

        #self.person_set.add(person)
    #person=models.OneToOneField(Person,
    #on_delete=models.CASCADE, blank=True, null=True)

class User(models.Model):
    user = models.OneToOneField(U,on_delete = models.CASCADE,blank=True, null=True)
    #name = models.CharField(max_length=20, blank=True, null=True)
    family = models.ForeignKey(Family, on_delete = models.CASCADE,blank=True, null=True, related_name='people')
    #password = models.CharField(max_length=20, blank=True, null=True)
    #class Meta:
       # unique_together = ["password"]
class Budget(models.Model):
    stonks = models.IntegerField( blank=True, null=True,default=0)
    user = models.ForeignKey(User, on_delete = models.CASCADE,blank=True, null=True)

   # def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        #if self.person_set.count() > 3:
           #super(Person, self).save()
       # else:
            #raise Exception("{self.Family.name} has no 3 people")
#
#
