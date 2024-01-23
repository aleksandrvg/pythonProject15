from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils import timezone
from django.utils.translation import gettext as _
class MyUser(AbstractUser):
    birth_date = models.DateField()
    avatar = models.ImageField(blank=True, null=True)

# GENRE_CHOICES = (
#     (1,_("Not selected")),
#     (2,_("Comedy")),
#     (3,_("Action")),
#     (4,_("Beauty")),
#     (5,_("Other"))
# )
#
# class Author(models.Model):
#     pseudonym = models.CharField(max_length=120,
#                                  blank=True,
#                                  null=True)
#     name = models.CharField(max_length=120)
#     def __str__(self):
#         return self.name
# class Article(models.Model):
#     author = models.ForeignKey(Author,on_delete=models.CASCADE,
#                                null=True,related_name='articles')
#     text = models.TextField(max_length=10000,null=True)
#     created_at = models.DateTimeField(default=timezone.now)
#     updated_at = models.DateTimeField(default=timezone.now)
#     genre = models.IntegerField(choices=GENRE_CHOICES,default=1)
#     def __str__(self):
#         return f"Author - {self.author.name},genre - {self.genre}, id - {self.id}"
# class Comment(models.Model):
#     text = models.CharField(max_length=10000)
#     article = models.ForeignKey(Article,on_delete=models.DO_NOTHING)
#     comment = models.ForeignKey('myFirstApp.Comment',null=True,
#                                 blank=True,
#                                 on_delete=models.DO_NOTHING, related_name="comments"
#                                 )
#     user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
#     def __str__(self):
#         return f"{self.text} by {self.user.username}"
#
# class Like(models.Model):
#     user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
#     article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
#     def __str__(self):
#         return f"By user {self.user.username} to article {self.article.id}"

# class Customer(models.Model):
#     name = models.CharField(max_length=120)
#     age = models.IntegerField
# class CustomerSettings(models.Model):
#     preferred_color = models.CharField()
#     customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='cus')
#
# class Publications(models.Model):
#     title = models.CharField(max_length=120)
#
#     class Meta:
#         ordering = ['title']
#     def __str__(self):
#         return self.title
# class Article(models.Model):
#     headline = models.CharField(max_length=120)
#     publications = models.ManyToManyField(Publications)
#
#     class Meta:
#         ordering = ['headline']
#     def __str__(self):
#         return self.headline
#
# class Book(models.Model):
#     name = models.CharField(max_length=120)
#     col_str = models.CharField(max_length=5)
#
#     class Meta:
#         ordering = ['name']
#     def __str__(self):
#         return self.name
#
# class Author(models.Model):
#     name = models.CharField(max_length=120)
#     phone = models.CharField(max_length=15)
#     book = models.ManyToManyField(Book)
#
#     class Meta:
#         ordering = ['name']
#     def __str__(self):
#         return self.name
#
# class Library(models.Model):
#     title = models.CharField(max_length=120)
#     author = models.ManyToManyField(Author)
#
#     class Meta:
#         ordering = ['title']
#     def __str__(self):
#         return self.title
# # Create your models here.
