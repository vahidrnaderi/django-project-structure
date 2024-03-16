from django.http import HttpResponse


# Create your views here.
def app1_api_v1_urls(request):
    response = "This is app1/api/v1/ urls!"
    return HttpResponse(response)
