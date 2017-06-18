from django.http import HttpResponse
from models import Question, Choice

def index(request):
    questions = Question.objects.all().order_by("-pub_date")[:5]
    response = reduce((lambda a, b: str(a)+", "+str(b)), questions)
    return HttpResponse(response)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
