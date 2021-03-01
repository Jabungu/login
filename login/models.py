from django.db import models
import re

# Create your models here.
class LoginManager(models.Manager):
    def login_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        return errors
    def registration_validator(self, postData):
        errors = {}
        if len(postData['username']) < 2:
            errors["username"] = "User name should be at least 2 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['emailmatch'] = "Invalid email address!"
        if len(postData['firstName']) < 3:
            errors["firstName"] = "First name should be at least 2 characters"
        if len(postData['lastName']) < 3:
            errors["lastName"] = "Last name should be at least 5 characters"
        
        if len(postData['email']) < 3:
            errors["email"] = "email should be at least 5 characters"
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters"
        if postData['password'] != postData['cpwd']:
            errors['cpwd'] = "Passwords don't match"
        return errors

# Create your models here.

class User(models.Model):
    userId = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    Address_Line_1 = models.CharField(max_length=40)
    Address_Line_2 = models.CharField(max_length=30)
    City = models.CharField(max_length=30)
    State = models.CharField(max_length=20)
    Zip = models.IntegerField(max_length=40)
    Country = models.CharField(max_length=30)
    Email = models.CharField(max_length=45, null=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=45, null=True)
    connections = models.ManyToManyField("User", blank=True)
    image =models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = LoginManager()