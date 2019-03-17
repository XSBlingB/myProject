from django.shortcuts import render,get_object_or_404
#载入模板，填充上下文，再返回由它生成的 HttpResponse 对象

# Create your views here.
#添加视图，之后要到polls.urls里面添加url（）调用函数
#视图需要做的是返回HTTresponse或者是抛出异常，如404

# from django.http import HttpResponse
# from django.template import loader
#使用模版，要添加模版的对应视图
from .models import Question
from django.http import Http404
#引入异常机制


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    #return HttpResponse(template.render(context, request))
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'polls/index.html',context)

def detail(request,question_id):
    #try:
    #   question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #    raise Http404("Question does not exist")
    #return HttpResponse("You are looking at question %s."
    #% question_id)
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',
    {'question':question})

def results(request,question_id):
    response = "You are looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("You're voting on question %s."
    % question_id)
