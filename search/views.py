from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core import serializers
from search import search


# Create your views here.
def results(request, template_name = "search/results.html"):

    q = request.GET.get('q', '')

    try:
        page = int(request.GET.get('page', 1))

    except ValueError:
        page = 1

    matching = search.products(q).get('products')
    json_products = serializers.serialize('json', matching)
    paginator = Paginator(matching, 9)

    try:
        results = paginator.page(page).object_list

    except (InvalidPage, EmptyPage):
        results = paginator.page(1).object_list

    search.store(request, q)
    page_title = 'Search Results for: '+ q

    return render_to_response(template_name, locals(), context_instance = RequestContext(request))
