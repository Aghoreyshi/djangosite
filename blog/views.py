from django.shortcuts import render, get_object_or_404

from models import Entry, Category

def main(request):
    entry_list = Entry.objects.all().order_by('-pub_date')
    return render(request, 'blog/main.html', {'entry_list': entry_list})


def detail(request, entry_id, **kwargs):
    entry = get_object_or_404(Entry, id=entry_id)
    return render(request, 'blog/detail.html', {'entry': entry})


