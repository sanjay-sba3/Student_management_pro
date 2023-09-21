from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, UserManager

class CustomUserManager(UserManager):
    def create_superuser(self, username, email=None, password=None, **extra_fields):
        role = Role.objects.get(role = 'superadmin')
         
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role_id', role.id)

        return self._create_user(username, email, password, **extra_fields)

class Role(models.Model):
    id = models.SmallAutoField(primary_key=True, unique=True)
    role = models.CharField(max_length=255, unique=True, blank=False, null=False)

    class Meta:
        db_table = 'proj_user_role'


class User(AbstractUser):
    id = models.SmallAutoField(primary_key=True,unique=True)
    username = models.CharField(max_length = 25, unique = True,blank=False,null=False)
    email = models.EmailField(unique = True,)
    role = models.ForeignKey(Role,on_delete=models.SET_NULL, null=True,blank=True)
    failed_login_count = models.IntegerField(default=0)
    is_password_change = models.IntegerField(default=0)
    created_by = models.IntegerField(null=True,blank=True)
    updated_by = models.IntegerField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)
    is_active = models.BooleanField(default=1)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','first_name', 'last_name']

    objects = CustomUserManager()

    class Meta:
            db_table = "proj_user"    
