from django.db import models
import random
import string


class Addresses(models.Model):
    original = models.URLField()
    shortened = models.CharField(max_length=30, blank=True)  # input for custom name

    def __str__(self):
        return f"{self.shortened} ({self.original})"
    #
    # def __int__(self):
    #     return id()

    def get_shortened_address(self):
        return self.shortened

    def get_original_address(self):
        return self.original

    def random_address(self):  # address generator (random), provides lowercase name 4 to 10 letters long
        letters = string.ascii_lowercase
        length = random.randint(4, 10)
        return ''.join(random.sample(letters, length))

    def shorten_address(self):
        # if custom name not provided generate random one
        while not self.shortened:
            self.shortened = self.shortened.random_address()
            if Addresses.objects.get(shortened__exact=self.shortened) == self.shortened:
                continue
            else:
                return self.shortened
        # if custom name provided, check if not taken
        if Addresses.objects.get(shortened__exact=self.shortened) == self.shortened:
            return False
        else:
            return True
