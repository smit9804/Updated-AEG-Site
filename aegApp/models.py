from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # objects = GameManager()

class Player(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    gamertag = models.CharField(max_length=45)
    gameType = models.CharField(max_length=45)
    role = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Admin(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

