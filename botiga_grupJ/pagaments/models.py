from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)
# password = models.PasswordField(max_length=128)

class Pagament(models.Model):
    id = models.AutoField(primary_key=True)
    tarjet_num = models.CharField(max_length=100)
    exp_date = models.DateField()
    cvc = models.IntegerField()
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    