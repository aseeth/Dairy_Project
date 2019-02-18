from django.db import models

class Farmer(models.Model):
    fid = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=30)
class MilkData(models.Model):
    date = models.DateField(default="2018-6-8")
    fid = models.OneToOneField(Farmer,unique=True,primary_key=True,on_delete=models.CASCADE)
    milkqty = models.PositiveIntegerField()
    fat = models.PositiveIntegerField()
    rate = models.PositiveIntegerField()
    totalamt=models.PositiveIntegerField()

    '''def save(self,*args,**kwargs):
        totalamt=self.milkqty*self.fat*self.rate
        super(MilkData,self).save(*args,**kwargs)'''


