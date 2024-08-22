from django.db import models

# Create your models here.
class Member(models.Model):
    member_first_name = models.CharField(max_length=32)
    member_last_name = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.member_first_name} {self.member_last_name}"

class Library(models.Model):
    book_name = models.CharField(max_length=64)
    book_author = models.CharField(max_length=64)
    book_year = models.IntegerField()
    book_borrowed = models.BooleanField(default=False)
    book_holder = models.ForeignKey(Member, on_delete=models.CASCADE)
    book_return_date = models.DateField()

    def __str__(self):
        return f"{self.book_name} by {self.book_author} ({self.book_year})"