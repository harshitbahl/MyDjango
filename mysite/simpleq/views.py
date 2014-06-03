from django.shortcuts import render
from simpleq.models import Question
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response

def index(request):
	questions = Question.objects.all()
	return render_to_response('questions/index.html',{'questions': questions})

def question_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render_to_response('questions/question_detail.html', {'question': question})