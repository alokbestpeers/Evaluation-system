from django.shortcuts import render, get_object_or_404
from .forms import CandidateForm
from .models import Technology, Questions

def home(request):
    return render(request, 'home.html')

def candidate_detail(request):
    form = CandidateForm()
    # import pdb; pdb.set_trace()
    if request.method == 'POST':
        if form.is_valid():
            form = CandidateForm(request.POST)
            form.save()
    else:
        form = CandidateForm()
    return render(request, 'candidate_detail.html', {'form':form})

def technology(request):
    technology = Technology.objects.all()
    return render(request, 'technology.html', {'technology':technology})

def tech_questions(request, pk):
    questions = Questions.objects.get(technology=pk)
    return render(request, 'tech_questions.html', {'questions':questions})