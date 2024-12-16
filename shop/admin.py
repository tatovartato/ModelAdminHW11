from django.contrib import admin
from shop.models import *
from django.contrib.contenttypes.admin import GenericTabularInline 

class ItemInLine(admin.StackedInline):
    model = Item 
    extra = 1

class ItemInLine1(admin.StackedInline):
    model = Item.tags.through
    extra = 1

class TagInLine(admin.StackedInline):
    model = Tag.items.through
    extra = 1

#---------------------------------------
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','description']
    search_fields = ['name']
    ordering = ['name']
    inlines = [ItemInLine]

class  ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'description']
    search_fields = ['name','description']
    ordering = ['-price']
    inlines = [ItemInLine1]

class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    inlines = [TagInLine]

#----------------------------
admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Tag, TagAdmin)
# admin.site.register(Image)