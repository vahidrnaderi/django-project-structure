from django.http import HttpResponse


# Create your views here.
def core_api_v1_urls(request):
    response = "This is core/api/v1/ urls!"
    return HttpResponse(response)
