from django.db import models
from django.contrib.auth.models import User  # Using Django's built-in User model

# Instructor model
class Instructor(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField(unique=True)
    profile_image = models.CharField(max_length=255, blank=True, null=True)  # Change to CharField to store URL

    def __str__(self):
        return self.name

# Course model
class Course(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=255, blank=True, null=True)  # Change to CharField to store URL
    description = models.TextField(blank=True, null=True)
    free_videos = models.JSONField(blank=True, null=True)  # Store links to free videos (e.g., 1-2 videos)
    paid_videos = models.JSONField(blank=True, null=True)  # Store links to all paid videos
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.DecimalField(help_text="Duration in hours", max_digits=8, decimal_places=2)
    level = models.CharField(max_length=100, choices=[
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced')
    ])
    language = models.CharField(max_length=50, choices=[
        ('Dart', 'Dart'),
        ('Java', 'Java'),
        ('Python', 'Python'),
        ('JavaScript', 'JavaScript')
    ])
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.title

# Student model
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # One-to-one relation with Django's User model
    username = models.CharField(max_length=100)  # Redundant; typically the User model handles usernames
    email = models.EmailField(max_length=100)    # Also redundant, User model includes email field

    def __str__(self):
        return self.username

# Enrollment model (Many-to-Many between Student and Course through Enrollment)
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateTimeField(auto_now_add=True)
    is_purchased = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.student.username} enrolled in {self.course.title}"

# Transaction model
class Transaction(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    transaction_date = models.DateTimeField(auto_now_add=True)
    amount_paid = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.student.username} paid {self.amount_paid} for {self.course.title}"

# Review model
class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Add unique constraint on (student, course) to prevent multiple reviews
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student.user.username}'s review of {self.course.title}"


