from nimbble.models import Community

def get_current_community(request):
    comm = Community.objects.get(is_default=True)
    return comm



