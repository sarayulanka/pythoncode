from django.urls import reverse
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify

# Create your models here.

class Author(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
      

class Book(models.Model):
  title = models.CharField(max_length=50)
  rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
  author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
  is_bestselling = models.BooleanField(default=False)
  slug = models.SlugField(default="", null=False, blank=True, db_index=True)

  def get_absolute_url(self):
    return reverse("book_detail", args=[self.slug])
    
  def save(self,*args,**kwargs):
    self.slug = slugify(self.title)
    super().save(*args, **kwargs)
  
  def __str__(self):
    return f"{self.title}  ({self.rating})"