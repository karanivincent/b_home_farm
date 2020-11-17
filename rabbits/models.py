from django.db import models

# Create your models here.


class BirthLot(models.Model):
    date = models.DateField()
    doe = models.ForeignKey(
        'Rabbit', related_name='mother_of', on_delete=models.PROTECT)
    buck = models.ForeignKey(
        'Rabbit', related_name='father_of', on_delete=models.PROTECT, null=True, blank=True)
    noBunnies = models.PositiveIntegerField()
    noMale = models.PositiveIntegerField()
    noFemales = models.PositiveIntegerField()
    noDeaths = models.PositiveIntegerField()

    def __str__(self):
        return str(self.doe.tagId) + ' :: ' + str(self.date)


class Rabbit(models.Model):
    GENDER_CHOICES = (('Male', 'Male'), ('Female', 'Female'))
    tagId = models.CharField(max_length=50, primary_key=True)
    gender = models.CharField(
        max_length=10,  choices=GENDER_CHOICES)
    breed = models.CharField(max_length=20, null=True, blank=True)
    weight = models.FloatField()
    birthLot = models.ForeignKey(
        BirthLot, related_name='bunny', on_delete=models.PROTECT, null=True, blank=True)

    available = models.BooleanField(default=True)

    def __str__(self):
        return self.tagId + ' ' + self.gender


class Disease(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    medication = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Diagnosis(models.Model):
    rabbit = models.ForeignKey(
        Rabbit, related_name='diagnosis', on_delete=models.PROTECT)
    disease = models.ForeignKey(
        Disease, related_name='diagnosis', on_delete=models.PROTECT)
    date = models.DateField()
    treated = models.BooleanField()

    def __str__(self):
        state = "Not Treated"
        if(self.treated == True):
            state = "Treated"
        return str(self.rabbit) + " :: " + str(self.disease) + " :: " + state


class Sale(models.Model):
    rabbit = models.ForeignKey(
        Rabbit, related_name='sale', on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.FloatField()
    customer = models.CharField(max_length=250, null=True, blank=True)


class Purchase(models.Model):
    TYPE_CHOICES = (('feed', 'feed'), ('medication', 'med'))
    p_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    name = models.CharField(max_length=200)
    amount = models.PositiveIntegerField()
    date = models.DateField()
    description = models.CharField(max_length=1000, null=True, blank=True)
    seller = models.CharField(max_length=250, null=True, blank=True)
