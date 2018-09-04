from django.shortcuts import render
from .forms import CandidateForm

def home(request):
	return render(request, 'home.html')

def candidate_detail(request):
	form = CandidateForm()
	return render(request, 'candidate_detail.html', {'form':form})