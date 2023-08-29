from django.contrib import admin

from .models import *


class CategoryInline(admin.StackedInline):
    model = Category
class CompanyInline(admin.StackedInline):
    model=Company
class ProductInline(admin.StackedInline):
    model=Product
    extra=0
class ProductInline2(admin.TabularInline):
    model=Product
    extra=0
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'company', 'price']
    list_filter=['category','company']
    #inlines=[CompanyInline,CategoryInline]
    sortable_by=['price']
    list_display_links=['id','name']

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display=['postal_address','city']
    list_filter=['city']
    
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    inlines=[ProductInline2]
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines=[ProductInline]
    
