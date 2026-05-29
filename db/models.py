from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)
    bonus = models.CharField(max_length=255)
    # The skill must be deleted when the race is deleted (models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name} ({self.race.name})"


class Guild(models.Model):
    name = models.CharField(max_length=255, unique=True)
    # Can be null means null=True. Often blank=True is also used for text fields.
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Player(models.Model):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255)  # EmailField defaults to non-unique
    bio = models.CharField(max_length=255)
    # Player must be deleted when the race is deleted (models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    # Player should NOT be deleted when the guild is deleted (models.SET_NULL)
    # This requires null=True so the field can be cleared safely
    guild = models.ForeignKey(Guild, on_delete=models.SET_NULL, null=True, blank=True)
    # Automatically set to the current time when the object is first created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.nickname
