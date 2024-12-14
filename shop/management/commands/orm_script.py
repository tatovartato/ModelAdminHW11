from decimal import Decimal
from django.db.models import DecimalField,  ExpressionWrapper
from typing import Any
from django.db.models import FloatField
from django.core.management.base import BaseCommand
from shop.models import Tag, Category, Item
from django.db.models import (
    Sum,
    Avg,
    Count,
    Min,
    Max,
    Q,
    F,
)

class Command(BaseCommand):
    def handle(self, *args:Any, **options:Any):
        # categories = Category.categoriesm.with_item_count()
        # for category in categories:
        #     print(f"Category: {category.name}, Item Count: {category.item_count}")
        
        # items = Item.itemsm.with_tag_count()
        # for item in items:
        #     print(f"Item:{item.name} , item`s tag count:{item.tags_count}")

        popular_tags = Tag.tagm.popular_tags(min_items=2)
        for tag in popular_tags:
            print(f"Tag: {tag.name}, Item Count: {tag.items_count}")
