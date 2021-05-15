from django.db import models

class reg(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.IntegerField()
    gender=models.CharField(max_length=10)
    password=models.CharField(max_length=10)

class exe(models.Model):
    ename=models.CharField(max_length=20)
    def __str__(self):
        return self.ename

class subexe(models.Model):
    ename=models.ForeignKey(exe,on_delete=models.CASCADE)
    sname=models.CharField(max_length=20)
    def __str__(self):
        return self.sname

class workout(models.Model):
    ename=models.ForeignKey(exe,on_delete=models.CASCADE)
    sname=models.ForeignKey(subexe,on_delete=models.CASCADE)
    wname=models.CharField(max_length=20)
    wdisc=models.TextField()
    image=models.ImageField(upload_to='image')

class trainer(models.Model):
    name=models.CharField(max_length=20)
    exercise=models.CharField(max_length=20)
    tdisc=models.TextField()
    image1=models.ImageField(upload_to='img',null=True)


