from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser,UserManager
class Role(models.Model):
  
  STUDENT = 1
  TEACHER = 2
  SECRETARY = 3
  
  ROLE_CHOICES = (
      (STUDENT, 'student'),
      (TEACHER, 'teacher'),
      (SECRETARY, 'secretary'),
      
      
  )

  id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

  def __str__(self):
      return self.get_id_display()

class User(AbstractUser):
    
    roles = models.ManyToManyField(Role,related_name='roles',blank=True)
    phone_number = models.CharField(max_length=10,unique=True)
    email = models.EmailField(unique=True,)

    REQUIRED_FIELDS = ["email","phone_number"]

    objects = UserManager()