from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def paginate(item_list, page=1, items_per_page=5, num_page_links=5):
    """
    Takes a list of items and paging criteria and returns the items
    on the requested page along with a list of pages with length of
    num_page_links.
    """
    paginator = Paginator(item_list, items_per_page, orphans=1)
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    total_page_list = [i for i in range(1, paginator.num_pages + 1)]
    if items.number <= num_page_links:
        page_list = total_page_list[:num_page_links]
    else:
        page_list = total_page_list[(items.number - num_page_links / 2 - num_page_links % 2):(items.number + num_page_links / 2)]

    return items, page_list
