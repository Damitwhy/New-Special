from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


from django.shortcuts import render

from .models import Engine

# Create your views here.
@login_required
def engine(request):
    engine = engine.objects.filter(created_by=request.user)
    
    return render(request, 'engine/engine.html', {'engine': engine})

@login_required
def engine_create(request):
    if request.method == 'POST':
        title = request.POST.get('title','')
        description = request.POST.get('description','')
        
        if title:
            Engine.objects.create(title=title, description=description, created_by=request.user, created_at=timezone.now())

            return redirect('/engine/engine.html')
        else:
            return render(request, 'engine/create.html', {'error': 'Title is required'})
            
    return render(request, 'engine/engine.html')