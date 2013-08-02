from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from polls.models import Poll


def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)


def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})


def vote(request, poll_id):
    return HttpResponse("You're voting on poll {0}".format(poll_id))


def results(request, poll_id):
    return HttpResponse("You're viewing poll {0}'s results".format(poll_id))
