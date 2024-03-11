
from django.http import HttpResponse

# Create your views here.
def app1_api_v2_urls(request):
    response="This is app1/api/v2/ urls!"
    return HttpResponse(response)