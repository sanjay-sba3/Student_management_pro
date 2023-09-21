from rest_framework import serializers
from ..models.student import Student, Branch

class StudentSerializer(serializers.ModelSerializer):
    # role_name = serializers.CharField(source='role.role')
    branch_name = serializers.CharField(source = 'branch_Id.student_branch')
    

    class Meta:
        model = Student
        fields = ['roll_No', 'f_Name','m_name', 'l_Name','branch_name']


class BranchSerializer(serializers.Serializer):

    class Meta:
        model = Branch
        fields = '__all__'        
        