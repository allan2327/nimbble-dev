from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from nimbble.fitnessaccount.signals import activities_loaded
from nimbble.models import FitnessActivity
from django.db.models import Sum


@receiver(user_signed_up)
def set_additional_values(sender, **kwargs):
    user = kwargs.pop('user')

    FbSignalReceiver().new_user(user)
    DefaultCommunityReceiver().set_default(user)


@receiver(activities_loaded)
def update_user_score(sender, **kwargs):
    user = kwargs.pop('user')
    pointObj = FitnessActivity.objects.aggregate(Sum('score'))
    user.points = pointObj.get('score__sum')
    user.save()


class FbSignalReceiver(object):
    def new_user(self, user):
        fb = user.socialaccount_set.filter(provider='facebook')

        if fb.count() == 0:
            return

        data = fb[0].extra_data
        self.set_picture(user, data)
        self.set_username(user, data)

        user.save()

    def set_picture(self, user, data):
        if 'picture' not in data:
            return

        user.picture_url = data['picture']['data']['url']

    def set_username(self, user, data):
        if 'id' not in data or user.username:
            return

        username = '{}{}'.format(user.first_name.lower(), data['id'])
        user.username = username

from nimbble.models import Community
from django.core.exceptions import ObjectDoesNotExist

class DefaultCommunityReceiver(object):

    def set_default(self, user):
        try:
            comm = Community.objects.get(is_default=True)
            user.communities.add(comm)
            user.save()
        except ObjectDoesNotExist:
            pass
