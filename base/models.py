from django.db import models

class Class(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Content(models.Model):
    group=models.ManyToManyField(Class)
    type = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    slug= models.SlugField(unique=True)
    
    def __str__(self):
        return self.type


class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    question_a = models.CharField(max_length=255)
    question_b = models.CharField(max_length=255)
    question_c = models.CharField(max_length=255)
    question_d = models.CharField(max_length=255)
    question_e = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class MCQ(models.Model):
    question = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)

    def __str__(self):
        return self.question


class Exercise(models.Model):
    book_image = models.ImageField(upload_to='images/')
    book_name = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    exercise_number = models.FloatField()
    solved_exercise_pdf = models.FileField(upload_to='solved_exercises/')

    def __str__(self):
        return f"{self.book_name} - Exercise {self.exercise_number}"
