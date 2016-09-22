from django.shortcuts import render_to_response, get_object_or_404
from django.template.loader import render_to_string
from django.core import serializers
from django.http import JsonResponse
from django.template import RequestContext
from spiritbuzz.models import Category, Product, ProductReview
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core import urlresolvers
from spiritbuzz.forms import ProductAddToCartForm, ProductReviewForm
from stats import stats
from spirit_buzz.settings import PRODUCTS_PER_ROW


def get_json_products(request):
    products = Product.active.all()
    json_products = serializers.serialize('json', products)
    return HttpResponse(json_products, content_type = 'application/javascript; charset=utf-8')







def index(request, template_name="spiritbuzz/index.html"):

    page_title = 'Small Batch, Artisanal, and Expressive Spirits'
    search_recs = stats.recommended_from_search(request)
    featured = Product.featured.all()[0:PRODUCTS_PER_ROW]
    recently_viewed = stats.get_recently_viewed(request)
    view_recs = stats.recommended_from_views(request)

    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def category(request, category_slug, template_name="spiritbuzz/category.html"):
    # Request our context from the request passed to us.
    #categories = categoryList
    c = get_object_or_404(Category, slug = category_slug)

    products = c.product_set.all()
    page_title = c.name
    meta_keywords = c.meta_keywords
    meta_description = c.meta_description
    return render_to_response(template_name, locals(), context_instance = RequestContext(request))

from cart import cart

def product(request, category_slug, product_slug, template_name="spiritbuzz/product.html"):
    # Request our context from the request passed to us.

    p = get_object_or_404(Product, slug = product_slug)
    #categories = p.categories.all()
    page_title = p.name
    meta_keywords = p.meta_keywords
    meta_description = p.meta_description
    stats.log_product_view(request, p)
    product_reviews = ProductReview.approved.filter(product = p).order_by('-date')
    review_form = ProductReviewForm()
    #form = ProductAddToCartForm()
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = ProductAddToCartForm(request, postdata)
        if form.is_valid():

            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
            cart.add_to_cart(request)
            url = urlresolvers.reverse('show_cart')
            return HttpResponseRedirect(url)


    else:
        form = ProductAddToCartForm(request = request, label_suffix = ':')
    form.fields['product_slug'].widget.attrs['value'] = product_slug


    request.session.set_test_cookie()


    return render_to_response(template_name, locals(), context_instance = RequestContext(request))







from checkout import checkout

def show_cart(request, template_name = 'cart/cart.html'):

    if request.method == 'POST':
        postdata = request.POST.copy()
        if postdata['submit'] == 'Remove':
            cart.remove_from_cart(request)
        if postdata['submit'] == 'Update':
            cart.update_cart(request)
        if postdata['submit'] == 'Checkout':
            checkout_url = checkout.get_checkout_url(request)
            return HttpResponseRedirect(checkout_url)
    cart_item_count = cart.cart_distinct_item_count(request)
    cart_items = cart.get_cart_items(request)
    page_title = 'Shopping Cart'
    cart_subtotal = cart.cart_subtotal(request)

    return render_to_response(template_name, locals(), context_instance = RequestContext(request))



@login_required
def add_review(request):

    form = ProductReviewForm(request.GET)

    if form.is_valid():
        review = form.save(commit = False)
        slug = request.GET.get('slug')
        product = Product.active.get(slug = slug)
        review.user = request.user
        review.product = product
        review.save()
        template = "spiritbuzz/product_review.html"
        html = render_to_string(template, {'review': review})
        response = {'success': 'True', 'html': html}

    else:
        html = form.errors.as_ul()
        response = {'success': 'False', 'html': html}

    return JsonResponse(response)

