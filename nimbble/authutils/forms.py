
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from nimbble.models import Community
from users.models import User


class NimbbleSignupForm(forms.Form):
    error_message = 'Default community was not found.'
    name = forms.CharField(label='Name', max_length=100, required=True)

    def signup(self, request, user):
        try:
            comm = Community.objects.get(is_default=True)
            user.communities.add(comm)
        except ObjectDoesNotExist:
            raise forms.ValidationError(self.error_message)


'''

class NimbbleSignupForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, required=True)
    community = forms.ModelChoiceField(queryset=Community.objects.all(),
                                        required=True,
                                        empty_label='')

    def signup(self, request, user):
        comm_id = int(request.POST['community'])
        comm = Community.objects.get(pk=comm_id)
        user.communities.add(comm)


'''
