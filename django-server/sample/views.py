from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'message': '코딩 좋아'
    }
    return render(request, 'sample/index.html', context)