from rest_framework import viewsets
from .models import Instructor, Course, Student, Enrollment, Transaction, Review
from .serializers import InstructorSerializer, CourseSerializer, StudentSerializer, EnrollmentSerializer, TransactionSerializer, ReviewSerializer
from django.contrib.auth.models import User
from .serializers import UserSerializer

# ViewSet for User
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# ViewSet for Instructor
class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

# ViewSet for Course
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# ViewSet for Student
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# ViewSet for Enrollment
class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

# ViewSet for Transaction
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

# ViewSet for Review
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

