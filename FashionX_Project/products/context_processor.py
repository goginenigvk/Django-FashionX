from products.models import Products


def products_count(request):
     count=Products.objects.count()
     return ({'prod_count':count})