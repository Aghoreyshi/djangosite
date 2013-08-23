from django.shortcuts import render, get_object_or_404

from models import Entry, Category

def main(request):
    entries_per_page = 5
    num_page_links = 4
    query = ""

    if request.method == 'GET':
        query = request.GET.get('query', '')

    if query:
        entry_list = Entry.objects.all().filter(title__icontains=query).order_by('-pub_date')
    else:
        entry_list = Entry.objects.all().order_by('-pub_date')[:5]

    return render(request, 'blog/main.html',
                  {'entry_list': entry_list,
                   'query': query,
                  })


def detail(request, entry_id, **kwargs):
    entry = get_object_or_404(Entry, id=entry_id)
    return render(request, 'blog/detail.html', {'entry': entry})


