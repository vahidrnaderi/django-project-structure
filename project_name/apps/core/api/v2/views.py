from django.http import HttpResponse


# Create your views here.
def core_api_v2_urls_views(request):
    response = "This is core/api/v2/ urls!"
    return HttpResponse(response)
