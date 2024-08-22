from django.db import models
# Create your models here.


class Member(models.Model):
    roles = (
        ('admin', 'Admin'),
        ('member', 'Member')
    )

    member_username = models.CharField(max_length=32, unique=True)
    member_first_name = models.CharField(max_length=32)
    member_last_name = models.CharField(max_length=32)
    member_role = models.CharField(choices=roles, blank=True, null=True)

    def __str__(self):
        return f"{self.member_first_name} {self.member_last_name}"

class Library(models.Model):
    book_name = models.CharField(max_length=64)
    book_author = models.CharField(max_length=64)
    book_year = models.IntegerField()
    book_borrowed = models.BooleanField(default=False)
    book_holder = models.ForeignKey(Member, on_delete=models.CASCADE, blank=True, null=True)
    book_return_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.book_name} by {self.book_author} ({self.book_year})"