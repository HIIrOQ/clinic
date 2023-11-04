from django.db import models

# Create your models here.
class Doctor(models.Model):
    first_name = models.CharField('Имя доктора ', max_length=100)
    last_name = models.CharField('Фамилия доктора ', max_length=100)
    phone_num = models.DecimalField('Номер телефона ' ,decimal_places=2, max_digits=12,)
    email = models.EmailField('Электронная почта',unique=True)
    exp = models.DecimalField('Опыт работы ',decimal_places=2 , max_digits=12)
    speciality = models.CharField('Название специальности   ', max_length=100)
    photo = models.ImageField(upload_to='media/')