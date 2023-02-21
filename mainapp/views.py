from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from mainapp.models import  (
    School, Teacher,
     Gallery,Review, 
     New, 
)

from mainapp.serializers import (
    SchoolSerializer,
    TeacherSerializer,
    GallerySerializer,
    ReviewSerializer,
    NewSerializer,
    
)



class SchoolView(ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = (IsAuthenticated, )

class TeacherView(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = (IsAuthenticated, )

class GalleryView(ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = (IsAuthenticated, )

class ReviewView(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticated, )

class NewView(ModelViewSet):
    queryset = New.objects.all()
    serializer_class = NewSerializer
    permission_classes = (IsAuthenticated, )