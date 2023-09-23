from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response
from student.models.student import Student, Branch
from student.serializers.user import UserSerializer 
from student.serializers.student import StudentSerializer, BranchSerializer
from rest_framework.response import responses
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
import jwt


# API for get loging details
def getLoginUser(request):
    header = request.headers['Authorization']
    token = header.split(' ')
    decodedata = jwt.decode(token[1], 'SECRET_KEY', algotithums= ['HS256'])
    print(decodedata)
    return decodedata['user_id']

# User CRUD
class StudentViews(GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    def get(self, request):
        
        try:
            id = request.data.get('roll_no', None)
            if (id in (None, "")):
                student  = Student.objects.all()
                serializer = StudentSerializer(student, many=True)
                return Response(serializer.data)
            elif Student.objects.filter(roll_No=id).exists():
                student_serializer = StudentSerializer(Student.objects.get(roll_No = id))
                return Response({'mesage':'student with roll number exists', 'data': student_serializer.data})
            else:
                return Response({'mesage':'student with roll number dosenot exists'})
        except Exception as e:
            return Response(str(e))  

    def post(self, request):
        try:
            if (request.data['roll_No'] not in (None, "") and request.data['branch_name'] not in (None, "")):
                
                if not (Student.objects.filter(roll_No = request.data.get('roll_No')).exists()):
                    # student_serializer = UserSerializer(data= request.data)
                    print(request.data.get('roll_No'))
                    print(request.data['branch_name'])
                    branch = Branch.objects.get(student_branch= request.data['branch_name'])
                    print(branch)
                    # branch_serializer = BranchSerializer(data = branch)
                    # if branch_serializer.is_valid():
                    #     print((branch_serializer))

                    student = Student(roll_No = request.data['roll_No'],
                                        f_Name = request.data['f_Name'].capitalize(),
                                        m_name = request.data['m_name'].capitalize(),
                                        l_Name = request.data['l_Name'].capitalize(),
                                        branch_Id = branch)
                    student.save()
                    
                    
                    return Response({"data": [StudentSerializer(student).data]})
                    # return Response({ "message":"Some data is missing....."})
                return Response({"error": {}, "message":"Roll Number already exists"})
                # return Response ({'error':'Branch id dose not exists'})
            else:
                return Response({'error': 'Invalid roll number of branch id'})
        except Exception as e:
            return Response({"error": str(e), "message":"Some data is missing....."})
        

    def put(self, request):
        try:
            data = getLoginUser(request)
            print(data)
            return Response('data updated')

            # if Student.objects.filter(id = request.get('id')).exists():
            #     student_serilizer = StudentSerializer(Student.objects.filter(id =request.get('id')))
            #     return Response({"student": student_serilizer.data})
        except Exception as e:
            return str(e)        