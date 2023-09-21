from django.db import models


# model for branch
class Branch(models.Model):
    id = models.SmallAutoField(primary_key=True, unique=True)
    student_branch = models.CharField(max_length= 255 ) 

    class Meta:
        db_table = 'proj_student_branch'


# model for student
class Student(models.Model):
    id = models.SmallAutoField(primary_key=True, unique=True)
    roll_No = models.IntegerField(unique= True)
    f_Name = models.CharField(max_length = 255)
    m_name = models.CharField(max_length= 255)
    l_Name = models.CharField(max_length = 255)
    branch_Id = models.ForeignKey(Branch, on_delete=models.SET_NULL, blank=True, null= True)
    is_admitted = models.BooleanField(null= False, default=1)
    created_by = models.CharField(max_length = 255, null=True, blank=True, default = 'admin')
    updated_by = models.CharField(max_length = 255, null=True, blank=True, default = 'admin')
    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = 'proj_students'

    





