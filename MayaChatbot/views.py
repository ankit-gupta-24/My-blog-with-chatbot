from django.shortcuts  import redirect
from django.http import HttpResponse

def MayaResponse(request):
    if request.method == 'POST':
        # resonse = maya.get_response(request.POST['msg'])
        response = 'welcome to my world bro...'
        return HttpResponse(response)
    return redirect('/')
