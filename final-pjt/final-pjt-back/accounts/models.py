from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter
from movies.models import Genre, Movie, Actor

# Create your models here.
class User(AbstractUser):
    # 회원가입시 기입해야하는 값
    email = models.EmailField(max_length=254, null=True)
    nickname = models.CharField(max_length=100)
    followings = models.ManyToManyField(settings.AUTH_USER_MODEL, symmetrical=False, related_name='followers')

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
 
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        from allauth.account.utils import user_email, user_field, user_username
        data = form.cleaned_data
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        username = data.get("username")

        nickname = data.get("nickname")
        user_email(user, email)
        user_username(user, username)
        if first_name:
            user_field(user, "first_name", first_name)
        if last_name:
            user_field(user, "last_name", last_name)
        if nickname:
            user_field(user, "nickname", nickname)
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            user.save()
        return user