from django.core.exceptions import PermissionDenied, FieldDoesNotExist

from mailinglist.models import MailingList


class UserCanUseMailingList:

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        user = self.request.user
        if type(obj) is MailingList:
            if obj.user_can_use_mailing_list(user):
                return obj
            else:
                raise PermissionDenied()

        mailing_list_attr = getattr(obj, 'mailing_list')
        if type(mailing_list_attr) is MailingList:
            if mailing_list_attr.user_can_use_mailing_list(user):
                return obj
            else:
                raise PermissionDenied
        raise FieldDoesNotExist('view does not know how to get mailing '
                                   'list.')