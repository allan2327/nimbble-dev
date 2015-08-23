
from django import forms
from nimbble.models import Community


class NimbbleSignupForm(forms.Form):
    community = forms.ModelChoiceField(queryset=Community.objects.all(),
                                        required=True,
                                        empty_label='')

    def signup(self, request, user):
        comm_id = int(request.POST['community'])
        comm = Community.objects.get(pk=comm_id)
        user.communities.add(comm)
