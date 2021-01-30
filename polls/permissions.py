from rest_framework.permissions import BasePermission

from .models import AuthID


class HasAnID(BasePermission):
    """ Checks if valid auth-id was provided in headers """

    def has_permission(self, request, view):
        try:
            auth_id = int(request.META['HTTP_AUTH_ID'])
        except ValueError or KeyError:
            return False

        id_set = {x.auth_id for x in AuthID.objects.all()}
        return auth_id in id_set
