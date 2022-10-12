from django.db import models


class Post(models.Model):
    # Male = 'M'
    # FeMale = 'F'
    # GENDER_CHOICES = (
    # (Male, 'Male'),
    # (FeMale, 'Female'),
    # )
    firstname = models.CharField( max_length = 20, blank = False,
                                 null = True)
    username = models.CharField( max_length = 20, blank = False,
                                 null = False)
    phone = models.IntegerField(null = True)
    password = models.CharField( max_length = 20, blank = False,
                                 null = True)
    #, widget=forms.PasswordInput
    # text = models.TextField(blank = False, null = False)
     
    # # Values for gender are restricted by giving choices
    # gender = models.CharField(max_length = 6, choices = GENDER_CHOICES,
    #                           default = Male)
     
    # time = models.DateTimeField(auto_now_add = True)