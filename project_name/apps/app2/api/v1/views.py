from django.http import HttpResponse


# Create your views here.
def app2_api_v1_urls_views(request):
    response = "This is app2/api/v1/ urls!"
    return HttpResponse(response)
