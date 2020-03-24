from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def guide(request):
    if request.method == 'GET':
        template = 'guide/guide.html'
        context = {}

        return render(request, template, context)