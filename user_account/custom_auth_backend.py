from django.contrib.auth.backends import BaseBackend, ModelBackend
from django.db.models import Q

from .models import User


class CustomBackend(ModelBackend):
    """"
    These are the method tahat should be overrided and should be provided in authentication backend
    when this calss is listed django runs the authentication backend as listed and 
    stops if one of authenticate method return result
    
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.filter(
                Q(email=username) | Q(phone_number=username) | Q(username=username)
            ).first()

            if user and user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    def get_user_by_username(self, username):
        try:
            return User.objects.get(
                Q(email=username) | Q(phone_number=username) | Q(username=username)
            )
        except User.DoesNotExist:
            return None