from .models import Brand, Mobile
from django.db.models import Q, F

def all_brands_not_in_korea_china():
    query = Brand.objects.filter(~Q(nationality='Korea') & ~Q(nationality='China'))
    return query

def some_brand_mobiles(*brand_names):
    l = []
    for i in brand_names:
        l.append(i)
    if l==[]:
        return(Mobile.objects.all())
    else:
        return(Mobile.objects.filter(brand__name__in=l))

def mobiles_brand_nation_equals_made_in():
    query = Mobile.objects.filter(brand__nationality=F('made_in'))
    return query
