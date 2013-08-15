from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from polls.models import Poll, Choice
from polls.forms import PollForm


def index(request):
    polls_per_page = 5
    num_page_links = 5
    poll_list = Poll.objects.order_by('-pub_date')
    paginator = Paginator(poll_list, polls_per_page, orphans=1)

    page = request.GET.get('page')
    try:
        polls = paginator.page(page)
    except PageNotAnInteger:
        polls = paginator.page(1)
    except EmptyPage:
        polls = paginator.page(paginator.num_pages)

    total_page_list = [i for i in range(1, paginator.num_pages + 1)]
    if polls.number <= num_page_links:
        page_list = total_page_list[:num_page_links]
    else:
        page_list = total_page_list[(polls.number - num_page_links / 2 - num_page_links % 2):(polls.number + num_page_links / 2)]

    context = {'polls': polls,
               'page_list': page_list,
              }
    return render(request, 'polls/index.html', context)


def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {
        'poll': poll,
    })


def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        chosen_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay poll voting form
        return render(request, 'polls/detail.html', {
            'poll': p,
            "error_message": "You didn't select a choice."
        })
    else:
        chosen_choice.votes += 1
        chosen_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


def create(request):
    if request.method == 'POST':
        form = PollForm(request.POST)
        if form.is_valid():
            poll = Poll(question=form.cleaned_data['question'])
            poll.save()
            for c in ['choice{0}'.format(i) for i in range(1, 5)]:
                try:
                    text = form.cleaned_data[c]
                except KeyError:
                    break
                if text:
                    poll.choice_set.create(choice_text=text)
            return HttpResponseRedirect('/polls/')
    else:
        form = PollForm()  # an unbound form

    return render(request, 'polls/create.html', {'form': form})


def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/results.html', {
    'poll': poll,
})
