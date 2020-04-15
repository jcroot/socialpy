from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Post


# Create your views here.
def post_list(request):
    return render(request, 'core/post_list.html', {})


def post_request(request):
    posts = Post.objects.all()
    response_data = {}

    if request.POST:
        cic = request.POST.get('ci')

        post = get_object_or_404(Post, cic=cic)

        response_data['cic'] = cic
        response_data['fullname'] = post.fullname
        response_data['social_code'] = post.social_code

        return JsonResponse(response_data)

    return render(request, 'core/post_list.html', {'posts': posts})
