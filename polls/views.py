from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from polls.models import Poll, Choice


def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)


def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})


def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        chosen_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay poll voting form
        return render(request, 'polls/detail.html', {'poll': p, "error_message":
                                                     "You didn't select a choice."})
    else:
        chosen_choice.votes += 1
        chosen_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/results.html', {'poll': poll})
