from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from django.conf import settings


class UserProfileManager(BaseUserManager):
    """manager for user profiles"""

    def create_user(self, name, email, password=None):
        """creates a new user profile"""
        if not email:
            raise ValueError('User must have an email address!')
        email = self.normalize_email(email)
        user = self.model(name=name, email=email)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, name, email, password):
        """creates superuser"""
        user = self.create_user(name, email, password)
        
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)

        return user
    


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users"""

    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['name']

    def get_name(self):
        return self.name
    
    def __str__(self):
        return self.email


class ProfileFeedItem(models.Model):
    """profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.status_text
