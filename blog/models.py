from django.conf import settings
from django.db import models
from django.utils import timezone
from multiselectfield import MultiSelectField


class Recipe(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    is_vegan = models.BooleanField("Vegan", default=False)
    is_veggie = models.BooleanField("Vegetarisch", default=False)
    cuisine_types = (
        ('DEF', ''),
        ('INT', 'Internationale Kueche'),
        ('ASI', 'Asiatische Kueche'),
        ('AFR', 'Afrikanische Kueche'),
        ('EUR', 'Europäische Kueche'),
        ('AME', 'Amerikanische Kueche'),
        ('SUA', 'Suedamerikanische Kueche'),)
    cuisine = models.CharField(max_length=30, choices=cuisine_types, default='DEF')
    allergen_types = (
        ("NA", "None"),
        ("nuts", "Nuesse"),
        ("glut", "Gluten"),
        ("lact", "Kuhmilch"),
        ("fish", "Fisch"),
        ("egg", "Huehnereier"),
    )
    contained_allergen = MultiSelectField(choices=allergen_types)
    instruction = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title