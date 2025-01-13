from django.db import models

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='First name')
    last_name = models.CharField(max_length=30, verbose_name='last name')
    date_of_birth = models.DateField(verbose_name='Date of birth')
    phone_number = models.CharField(max_length=12, verbose_name='Phone number')
    email = models.EmailField(verbose_name='Email', unique=True)


    def __str__(self):
        return f'{self.pk} {self.first_name}'


class Doctor(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='First name')
    last_name = models.CharField(max_length=30, verbose_name='last name')
    specialty = models.CharField(max_length=30, verbose_name='Specialty')
    phone_number = models.CharField(max_length=12, verbose_name='Phone number')
    email = models.EmailField(verbose_name='Email', unique=True)


    def __str__(self):
        return f'{self.pk} {self.first_name}'


class Diagnosis(models.Model):
    name = models.CharField(max_length=30, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    patient = models.ManyToManyField(Patient, related_name='diagnoses')


    def __str__(self):
        return f'{self.pk} {self.name}'


class Appointment(models.Model):
    reception_time = models.DateTimeField(verbose_name='Time of reception')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments') 
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')

    
    def __str__(self):
        return f'{self.pk} {self.reception_time}'