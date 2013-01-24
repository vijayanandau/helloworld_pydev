from django.db import models

class MyPoll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField("Date Published")
    
class MyChoice(models.Model):
    myPoll = models.ForeignKey(MyPoll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()
    
        
    
