from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from student.models.user import User 
from student.serializers.user import UserSerializer, LoginSerializer 
from django.contrib.auth import authenticate 
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken 
# login Api
class LoginViews(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if (username != None and username != "" and password != None and password != ""):
            if (User.objects.filter(username=username, is_active=True).exists()):
                user = authenticate(username = username, password = password)
                print(user)
                if user is None:
                    return Response('login failed ...... ')
                access_token = AccessToken.for_user(user)
                return Response({"status": "login sucess", "message":'Hi '+username, "Token": str(access_token),})
                
            else:
                return Response('login failed')
        else:
            return Response({"error":"login Credentials are incorrect"})    

# User CRUD

class UserViews(GenericAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get(self, request):
        try:
            id = request.data.get('id', None)
            if id in (None, ''):
                users  = User.objects.all()
                users_serializer = UserSerializer(users, many=True)
                return Response(users_serializer.data)
            if User.objects.filter(id=id).exists():
                user = User.objects.get(id=id)
                user_serializer = UserSerializer(user)
                return Response(user_serializer.data) 
        except Exception as e:
            return Response(str(e))    



      
    def post(self, request):
        
        user_serializer = UserSerializer(data= request.data)
        if user_serializer.is_valid():
            # validated_data = user_serializer.validated_data
            user_serializer.save()
            return Response(user_serializer.data)


