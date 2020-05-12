from django.db import models

class Sighting(models.Model):

    latitude = models.DecimalField('Latitude',default = None,max_digits =50,decimal_places = 10)

    longitude = models.DecimalField('Longitude',default = None,max_digits =50,decimal_places = 10)

    unique_squirrel_id = models.CharField('ID',max_length = 50,default = None)

    CHOICE1 = {('AM','AM'),('PM','PM'),}

    shift = models.CharField('Shift',max_length = 50,default = None,choices = CHOICE1)

    date = models.DateField('Date',max_length = 50,default = None,)

    CHOICE2 = {('Adult','Adult'),('Juvenile','Juvenile'),('None','None'),}
    age = models.CharField('Age',max_length = 50,default = None,choices = CHOICE2)

#    CHOICE3 = {('Black','Black'),('Cinnamon','Cinnamon'),('Gray','Gray'),}
#    primary_fur_color = models.CharField('Color',max_length = 50,default = None,choices = CHOICE3)

    specific_location = models.CharField('Specific_location',max_length = 50,default = None)

    running = models.BooleanField('Running',default = False)

    chasing = models.BooleanField('Chasing',default = False)

    climbing = models.BooleanField('Climbing',default = False)

    eating = models.BooleanField('Eating',default = False)

    foraging = models.BooleanField('Foraging',default = False)

    other_activities = models.CharField('Other_activity',max_length = 50,default = None)

    kuks = models.BooleanField('Kuks',default = False)

    quaas = models.BooleanField('Quaas',default = False)

    moans = models.BooleanField('Moans',default = False)

    tail_flags = models.BooleanField('Tail_flags',default = False)

    tail_twitches = models.BooleanField('Tail_twitches',default = False)

    approaches = models.BooleanField('Approaches',default = False)

    indifferent = models.BooleanField('Indifferent',default = False)

    runs_from = models.BooleanField('Runs_from',default = False)

