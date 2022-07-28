from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class User(models.Model):
    name = models.CharField(max_length=100)
    EDV = models.CharField(max_length=10)
    id_card = models.CharField(max_length=30, default='')

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=30,default='')

    def __str__(self):
        return self.name

class Apprentice(models.Model):
    course = models.ForeignKey(Course, related_name="CourseApprentice", on_delete=models.CASCADE)
    idApprenticeFK = models.ForeignKey(User, related_name="userApprentice", on_delete=models.CASCADE)

class typeAssociente(models.Model):
    type = models.CharField(max_length=30)

    def __str__(self):
        return self.type

class Associate(models.Model):
    type = models.CharField(max_length=30)
    idAssociateFK = models.ForeignKey(User, related_name="userADM", on_delete=models.CASCADE)



class Machine(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    status = models.BooleanField()
    ipaddress = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Question(models.Model):
    type = models.CharField(max_length=15)

    def __str__(self):
        return self.type

class GreenBook(models.Model):
    idMachineFK = models.ForeignKey(Machine, related_name="machineGreenBook", on_delete=models.CASCADE)
    typeQuestion = models.ForeignKey(Question, related_name="question", on_delete=models.CASCADE)
    question = models.CharField(max_length=50)



class Maintenance(models.Model):
    date = models.DateField()
    hour = models.TimeField()
    idMachineFK = models.ForeignKey(Machine, related_name="machineMaintenance", on_delete=models.CASCADE)
    idAssociateFK = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)


class ReleaseMachine(models.Model):
    date = models.DateField()
    hour = models.TimeField()
    idMachineFK = models.ForeignKey(Machine, related_name="machineReleaseMachine", on_delete=models.CASCADE)
    idAssociateFK = models.ForeignKey(User, related_name="userReleaseMachine", on_delete=models.CASCADE)

class QRcode(models.Model):
    router_ip = models.CharField(max_length=300)
    idMachineFK = models.ForeignKey(Machine, related_name="machineQRcode", on_delete=models.CASCADE)

class Observation(models.Model):
    date = models.DateField()
    hour = models.TimeField()
    idMachineFK = models.ForeignKey(Machine, related_name="machineObservation", on_delete=models.CASCADE)
    idAssociateFK = models.ForeignKey(User, related_name="userObservation", on_delete=models.CASCADE)

class MaintenanceOrder(models.Model):
    status = models.CharField(max_length=15)
    idMachineFK = models.ForeignKey(Machine, related_name="machineMaintenanceOrder", on_delete=models.CASCADE)
    idAssociateFK = models.ForeignKey(User, related_name="userMaintenanceOrder", on_delete=models.CASCADE)



