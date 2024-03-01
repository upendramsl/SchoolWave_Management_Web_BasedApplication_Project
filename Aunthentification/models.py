from django.db import models

# Create your models here.
class management(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.CharField(max_length=20)
    password=models.CharField(max_length=100)

    def __str__(self):
       return self.name

class faculty(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.CharField(max_length=20)
    password=models.CharField(max_length=100)

    def __str__(self):
       return self.name





class class7(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.CharField(max_length=20)
    password=models.CharField(max_length=100)


    def __str__(self):

       return self.name



class class8(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.CharField(max_length=20)
    password=models.CharField(max_length=100)
    def __str__(self):
       return self.name

class class9(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.CharField(max_length=20)
    password=models.CharField(max_length=100)

    def __str__(self):
       return self.name

class class10(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.CharField(max_length=20)
    password=models.CharField(max_length=100)

    def __str__(self):
       return self.name

class class7Maths(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    pq=models.CharField(max_length=210)
    answer=models.CharField(max_length=1000)
    remarks=models.CharField(max_length=100)
    nq=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class class7Telugu(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    pq=models.CharField(max_length=210)
    answer=models.CharField(max_length=1000)
    remarks=models.CharField(max_length=100)
    nq=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class class7science(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    pq=models.CharField(max_length=210)
    answer=models.CharField(max_length=1000)
    remarks=models.CharField(max_length=100)
    nq=models.CharField(max_length=200)

    def __str__(self):
      return  self.name

class class7Social(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    pq=models.CharField(max_length=210)
    answer=models.CharField(max_length=1000)
    remarks=models.CharField(max_length=100)
    nq=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class class8Maths(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    pq=models.CharField(max_length=210)
    answer=models.CharField(max_length=1000)
    remarks=models.CharField(max_length=100)
    nq=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class class8Telugu(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    pq=models.CharField(max_length=210)
    answer=models.CharField(max_length=1000)
    remarks=models.CharField(max_length=100)
    nq=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class class8science(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    pq=models.CharField(max_length=210)
    answer=models.CharField(max_length=1000)
    remarks=models.CharField(max_length=100)
    nq=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class class8Social(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    pq=models.CharField(max_length=210)
    answer=models.CharField(max_length=1000)
    remarks=models.CharField(max_length=100)
    nq=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class class9Maths(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    pq=models.CharField(max_length=210)
    answer=models.CharField(max_length=1000)
    remarks=models.CharField(max_length=100)
    nq=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class class9Telugu(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    pq=models.CharField(max_length=210)
    answer=models.CharField(max_length=1000)
    remarks=models.CharField(max_length=100)
    nq=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class class9science(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    pq=models.CharField(max_length=210)
    answer=models.CharField(max_length=1000)
    remarks=models.CharField(max_length=100)
    nq=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class class9Social(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    pq=models.CharField(max_length=210)
    answer=models.CharField(max_length=1000)
    remarks=models.CharField(max_length=100)
    nq=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class class10Maths(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    pq=models.CharField(max_length=210)
    answer=models.CharField(max_length=1000)
    remarks=models.CharField(max_length=100)
    nq=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class class10Telugu(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    pq=models.CharField(max_length=210)
    answer=models.CharField(max_length=1000)
    remarks=models.CharField(max_length=100)
    nq=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class class10science(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    pq=models.CharField(max_length=210)
    answer=models.CharField(max_length=1000)
    remarks=models.CharField(max_length=100)
    nq=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class class10Social(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    pq=models.CharField(max_length=210)
    answer=models.CharField(max_length=1000)
    remarks=models.CharField(max_length=100)
    nq=models.CharField(max_length=200)

    def __str__(self):
        return self.name

