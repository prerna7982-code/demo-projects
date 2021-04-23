from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
# from rest_framework_simplejwt.tokens import RefreshToken
import random
import os
from django.core.validators import RegexValidator

class UserManager(BaseUserManager):

    def create_user(self, username, email, password):
        if username is None:
            raise TypeError('Users should have a username')
        if password is None:
            raise TypeError('Users should have a password')

        user = self.model(username=username,email=email)
        user.username = username
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


def upload_image_path_profile(instance, filename):
	new_filename = random.randint(1,9996666666)
	name, ext = get_filename_ext(filename)
	final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
	return "Profile/{new_filename}/{final_filename}".format(
			new_filename=new_filename,
			final_filename=final_filename
	)
		 

def get_filename_ext(filepath):
	base_name = os.path.basename(filepath)
	name, ext = os.path.splitext(base_name)
	return name, ext


class CustomUser(AbstractUser):
	id = models.BigAutoField(auto_created=True, primary_key=True, serialize=True, verbose_name='ID')
	username = models.CharField('username',unique=True, max_length=255, blank=False,null=False)
	email = models.EmailField('email address', max_length=255, blank=True,null=True)
	password = models.CharField(max_length= 126,blank=False)
	first_name = models.CharField(verbose_name='first name', max_length=30, blank=True)
	last_name = models.CharField(verbose_name='last name', max_length=30, blank=True)
	is_active = models.BooleanField(default=True)
	avatar = models.ImageField(default = 'static/default_image/default.png', upload_to = upload_image_path_profile, blank = True)


	USERNAME_FIELD = 'username'

	def __str__(self):
		return f"{self.username}"
