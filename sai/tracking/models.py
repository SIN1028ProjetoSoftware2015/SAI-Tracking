# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Country(models.Model):
    """This model represent all countries registered in APP"""
    name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name='País'
        verbose_name_plural='Países'


class UserProfile(models.Model):
    """This class is used to add more fields to User Profile as Aluno"""
    # Linking a UserProfile to a User model instance
    user = models.OneToOneField(User)
    # The aditional atttributes that we wish to include
    profile_image = models.ImageField(upload_to='profile_images', blank=True)
    birth_date = models.DateField()
    mothers_name = models.CharField(max_length=200)
    fathers_name = models.CharField(max_length=200)
    birth_local = models.CharField(max_length=150)
    nationality = models.ForeignKey(Country)
    passport = models.CharField(max_length=50)
    permanent_address = models.CharField(max_length=200)
    permanent_phone = models.CharField(max_length=20)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

    class Meta:
        verbose_name='Usuário'
        verbose_name_plural='Usuários'

