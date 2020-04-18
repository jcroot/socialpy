from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Post, SocialProgram


# Create your views here.
def post_list(request):
    return render(request, 'core/post_list.html', {})


def post_request(request):
    posts = Post.objects.all()
    response_data = {}
    social_code = ''
    fullname = ''

    if request.POST:
        cic = request.POST.get('ci')

        # post = get_object_or_404(Post, cic=cic)
        post_set = Post.objects.filter(cic=cic)

        if post_set.count() > 0:
            for result in post_set:
                fullname = result.fullname
                social_code += SocialProgram.objects.get(code=result.social_code).description + ' '

            response_data['cic'] = cic
            response_data['fullname'] = fullname
            response_data['social_code'] = social_code
            status = 200
        else:
            status = 404

        return JsonResponse(response_data, status=status)

    return render(request, 'core/post_list.html', {'posts': posts})
