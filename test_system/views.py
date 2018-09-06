from django.shortcuts import render, get_object_or_404, redirect
from .forms import CandidateForm
from .models import Technology, Questions

def home(request):
    form = CandidateForm()
    # import pdb; pdb.set_trace()
    if request.method == 'POST':
        form = CandidateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('technology')
    else:
        form = CandidateForm()
    return render(request, 'home.html', {'form':form})

def technology(request):
    technology = Technology.objects.all()
    return render(request, 'technology.html', {'technology':technology})

def tech_questions(request, pk):
    questions = Questions.objects.filter(technology=pk)
    return render(request, 'tech_questions.html', {'questions':questions})