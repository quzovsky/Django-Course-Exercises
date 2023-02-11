from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'is_active']
    list_display_links = ['id', 'name']
    fieldsets=(('Identification',{'fields':('name','price','is_active')}),('Details',{'classes':('collapse',),'fields':('category','company')}))
    list_editable=['is_active']
    actions=['make_inactive']
    def make_inactive(self,request,queryset):
        updated=queryset.update(is_active=False)
        