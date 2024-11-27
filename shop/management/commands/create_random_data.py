import random
from faker import Faker
from django.core.management.base import BaseCommand
from shop.models import *

fake = Faker()

class Command(BaseCommand):
    help = 'Populate database with fake data'

    def handle(self, *args, **kwargs):
        self.stdout.write("Creating Categories...")
        categories = [
            Category(name=self.generate_category_name(), description=fake.paragraph(nb_sentences=3))
            for _ in range(500)
        ]
        Category.objects.bulk_create(categories)
        self.stdout.write(f"{len(categories)} Categories created.")

        categories = list(Category.objects.all())

        self.stdout.write("Creating Items...")
        items = [
            Item(
                name=self.generate_item_name(),
                category=random.choice(categories),
                price=round(random.uniform(10.0, 500.0), 2),
                description=fake.paragraph(nb_sentences=5),
            )
            for _ in range(500)
        ]
        Item.objects.bulk_create(items)
        self.stdout.write(f"{len(items)} Items created.")

        items = list(Item.objects.all())

        self.stdout.write("Creating Tags...")
        tags = [
            Tag(name=self.generate_tag_name())
            for _ in range(500)
        ]
        Tag.objects.bulk_create(tags)
        self.stdout.write(f"{len(tags)} Tags created.")

        self.stdout.write("Linking Tags to Items...")
        tags = list(Tag.objects.all())
        for tag in tags:
            related_items = random.sample(items, random.randint(1, 10))
            tag.items.add(*related_items)
        self.stdout.write("Tags linked to Items successfully.")

    def generate_category_name(self):
        """Generate a realistic category name."""
        categories = [
            "Electronics", "Books", "Clothing", "Toys", "Furniture", 
            "Food", "Health", "Automotive", "Sports", "Beauty"
        ]
        return random.choice(categories) + " " + fake.word().capitalize()

    def generate_item_name(self):
        """Generate a realistic item name."""
        products = [
            "Smartphone", "Laptop", "Table", "Chair", "Headphones",
            "Jacket", "Shoes", "Bag", "Bicycle", "Watch"
        ]
        brand = fake.company()
        return f"{brand} {random.choice(products)}"

    def generate_tag_name(self):
        """Generate a realistic tag name."""
        tags = [
            "Popular", "Sale", "New Arrival", "Limited Edition", 
            "Trending", "Exclusive", "Best Seller", "Eco-Friendly"
        ]
        return random.choice(tags)
