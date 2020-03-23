from django.shortcuts import render

def guide(request):
    if request.method == 'GET':
        template = 'guide/guide.html'
        context = {}

        return render(request, template, context)