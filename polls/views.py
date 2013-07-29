from django.shortcuts import render
from django.http import HttpResponse

from polls.models import Poll


def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)


def detail(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    context = {'poll': poll}
    return render(request, 'polls/detail.html', context)


def vote(request, poll_id):
    return HttpResponse("You're voting on poll {0}".format(poll_id))


def results(request, poll_id):
    return HttpResponse("You're viewing poll {0}'s results".format(poll_id))
