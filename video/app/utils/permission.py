import functools

from .consts import COOKIE_NAME
from app.models import ClientUser
from django.shortcuts import redirect, reverse


def dashboard_auth(func):

    @functools.wraps(func)
    def wrapper(self, request, *args, **kwargs):

        user = request.user

        if not user.is_authenticated or not user.is_superuser:
            return redirect('{}?to={}'.format(reverse('login'), request.path))

        return func(self, request, *args, **kwargs)

    return wrapper


def client_auth(request):

    value = request.COOKIES.get(COOKIE_NAME)

    if not value:
        return None

    user = ClientUser.objects.filter(pk=value)
    users = ClientUser.objects.get(pk=value)

    if user and users.status:
        return user[0]
    else:
        return None
