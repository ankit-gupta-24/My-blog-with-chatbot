from django.db import models
# import datetime

# Create your models here.
# model to store education
class education_model(models.Model):
    std_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    percent = models.IntegerField()
    institute = models.CharField(max_length=100)
    start_year = models.DateField()
    end_year = models.DateField()

    def __str__(self):
        return self.std_name


# models to store experience 
class Experience(models.Model):
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100,default='No company')
    description = models.TextField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField()
    skills_learned = models.CharField(max_length=200)

    def __str__(self):
        return self.job_title


# model to store information of conatct form at contact page
class ContactMessages(models.Model):
    name = models.CharField(max_length=80)
    mobile_number = models.IntegerField()
    email = models.EmailField()
    message = models.TextField(max_length=500)
    msg_date = models.DateField(auto_now_add=True)

    # class Meta:
    #     db_table = 'ContactMessages'

    def __str__(self):
        return self.name + " " + self.email


# model to store technical skills

percent = ((str(i),str(i)) for i in range(101))
class TechnicalSkills(models.Model):
    skill_name = models.CharField(max_length=50)
    skill_level = models.CharField(max_length=3,choices=percent,default='80')

    def __str__(self):
        return self.skill_name

# model to store interpersonal skills

class interpersonalSkills(models.Model):
    skill_name = models.CharField(max_length=50)

    def __str__(self):
        return self.skill_name

# model to store achievements

class Achievements(models.Model):
    achievemnt = models.CharField(max_length=300)

    def __str__(self):
        return self.achievemnt

# model to store projects done by me shown at my work page

class MyProjects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    technologies = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.title

