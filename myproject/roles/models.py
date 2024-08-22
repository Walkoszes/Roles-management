from django.db import models

# Create your models here.
class Role(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    name = models.CharField(max_length=50, choices=ROLE_CHOICES)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def change_role(self, new_role):
        self.role = new_role
        self.save()

    def add_to_group(self, group):
        group.users.add(self)

class Group(models.Model):
    name = models.CharField(max_length=50)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name