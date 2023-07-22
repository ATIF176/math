from django.db import models

class ClassName(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Content(models.Model):
    group = models.ManyToManyField(ClassName)
    content_type = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.content_type

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    question_a_text = models.CharField(max_length=255, null=True)
    question_b_text = models.CharField(max_length=255, null=True)
    question_c_text = models.CharField(max_length=255, null=True)
    question_d_text = models.CharField(max_length=255, null=True)
    question_e_text = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.title

class MCQ(models.Model):
    question_text = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)

    def __str__(self):
        return self.question_text

class Exercise(models.Model):
    book_image = models.ImageField(upload_to='images/')
    book_name = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    exercise_number = models.FloatField()
    solved_exercise_pdf = models.FileField(upload_to='solved_exercises/')

    def __str__(self):
        return f"{self.book_name} - Exercise {self.exercise_number}"
