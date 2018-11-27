from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from auths.serializers import (
UserSerializer,
UserLoginSerializer,
)
from django.contrib.auth.models import User

from rest_framework.permissions import(
AllowAny,
IsAuthenticated,
IsAdminUser,
IsAuthenticatedOrReadOnly,
)
class UserCreate(CreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

'''we are using the base APIView therefore have to specify the methods
		we want to use'''
class UserLoginAPIView(APIView):
	permission_classes=[AllowAny]
	serializer_class=UserLoginSerializer
	'''post and createapiview are different in that post is not going
	to save any data'''
	def post(self,request,*args,**kwargs):
		data=request.data
		serializer=UserLoginSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			new_data= serializer.data
			return Response(new_data,status=HTTP_200_OK)
		return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
