from django.http import HttpResponse


def home_page(request):
    return HttpResponse(
        "Hi. This is homepage. Welcome! Please enter your 'name' and, if you want - amount, "
        "for generate users in 'get-user/' section"
    )
