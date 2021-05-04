from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfileInfo(models.Model):
    
    """ the reason for that is because this is basically a model class to add an additional information that the default user doesn't have.
    Remember the default user already has things like their username email password first name and last name.
    But if you want to add more attributes to your actual user you can essentially almost like extending the class of this one to one relationship.
    What you don't want to do is just directly inherit from the User class that may seem really tempting but doing that may screw up your database 
    in thinking that it has multiple instances of the same user.So instead we use a one to one field relationship.
    """
    user = models.OneToOneField(User,on_delete = models.CASCADE)

    #addtional
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to= 'profile_pics', blank=True)

    def __str__(self):
        return self.user.username
    