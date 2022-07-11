from django.shortcuts import render

import requests

from .models import Product

def index(request):
    products = Product.objects.all()

    context = {'products': products}
    return render(request, 'index.html', context)

def product(request, product_id):

    perticular_product =  Product.objects.get(id = product_id)
    recently_viewed_products = None
    if 'recently_viewed' in request.session:
        if product_id in request.session['recently_viewed']:
            request.session['recently_viewed'].remove(product_id)

        recently_viewed_products = Product.objects.filter(pk__in = request.session['recently_viewed'])
        request.session['recently_viewed'].append(product_id)
        if len(request.session['recently_viewed']) > 5:
            request.session['recently_viewed'].pop()
    else:
        request.session['recently_viewed'] = [product_id]

    request.session.modified = True

    context = {
        'product' : perticular_product,
        'recently_viewed_products' : recently_viewed_products
    }
    return render(request, 'product.html', context)

def load_products(request):
    r = requests.get('https://fakestoreapi.com/products')
    for item in r.json():
        product = Product(
            title=item['title'],
            description=item['description'],
            price=item['price'],
            image_url=item['image']
        )
        product.save()

    return render(request, 'index.html')