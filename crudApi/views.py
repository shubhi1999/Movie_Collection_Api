from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .serializers import CollectionSerializer
from .models import Movie, Collection
from .utils import movieList
import jwt
from rest_framework.decorators import api_view, permission_classes
from rest_framework_jwt.settings import api_settings
from django.conf import settings
from django.contrib.auth.models import User

class ThirdPartyAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def get(self, request):
        
        num = request.query_params.get('page')
        return movieList(num)

class ListCreateMovieAPIView(ListCreateAPIView):
    serializer_class = CollectionSerializer
    queryset = Collection.objects.all()
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        movies = Movie.objects.all()
        serializer.save(movies = movies)


class RetrieveUpdateDestroyMovieAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CollectionSerializer
    queryset = Collection.objects.all()
    permission_classes = [IsAuthenticated]

@api_view(['POST'])
@permission_classes([AllowAny, ])
def user_authentication(request):
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    data = request.data
    user = User.objects.create(username=data['username'])
    user.set_password(data['password'])
    if user:
        try:
            payload = jwt_payload_handler(user)
            token = jwt.encode(payload, settings.SECRET_KEY)
            return Response({'access_token': token }, status=status.HTTP_200_OK)
        except Exception as e:
            raise e
    else:
        res = {
            'error': 'can not authenticate with the given credentials or the account has been deactivated'}
        return Response(res, status=status.HTTP_403_FORBIDDEN)

