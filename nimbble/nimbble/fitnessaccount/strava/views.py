from django.shortcuts import redirect
from django.contrib import messages

def token_login(request):
    if request.method == 'GET':
        messages.success(request, 'Hello world.')
        return redirect('ui:trackers')
