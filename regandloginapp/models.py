from django.db import models
class Reg(models.Model):
    fname=models.CharField(max_length=10)
    lname=models.CharField(max_length=10)
    dob=models.DateField()
    mobno=models.IntegerField()
    emailid=models.EmailField(max_length=30,default='lokeshitinfo@gmail.com')
    username = models.CharField(primary_key=True,
                                max_length=20)
    password = models.CharField(max_length=20,default='lokeshit')
    cpassword = models.CharField(max_length=20,default='lokeshit')
    def __str__(self):
        return self.user
