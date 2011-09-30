from django.http import HttpResponse
import django.dispatch

upload_received = django.dispatch.Signal(providing_args=['data', 'user'])

def upload(request, *args, **kwargs):
    if request.method == 'POST':
        if request.FILES:
            upload_received.send(sender='uploadify', data=request.FILES['Filedata'], user=request.user)
    return HttpResponse('True')


