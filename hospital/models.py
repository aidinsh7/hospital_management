from django.db import models

# Create your models here.



class Department(models.Model):
    department_name = models.CharField(max_length=255)
    department_discription = models.TextField()

    def __str__(self):
        return self.department_name


class Doctor(models.Model):
    doc_name =models.CharField(max_length=250)
    doc_spec = models.CharField(max_length=250)
    doc_image =models.ImageField(upload_to='doctor')
    doc_email =models.EmailField()
    department_name = models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.doc_name+ " ( " +self.doc_spec + " )"


class Booking(models.Model):
    p_name = models.CharField(max_length=100)
    p_phone = models.CharField(max_length=11)
    p_email = models.EmailField()
    doc_name = models.ForeignKey(Doctor,on_delete=models.CASCADE )
    booking_date = models.DateField()
    booking_on = models.DateField(auto_now= True)
    p_image = models.ImageField(upload_to='images')


    def __str__(self):
        return self.p_name





