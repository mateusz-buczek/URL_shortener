from django.db import models
import random
import string


class Addresses(models.Model):
    original = models.TextField()
    shortened = models.CharField(max_length=30)  # input for custom name

    def __str__(self):
        return f"{self.shortened} ({self.original})"
    #
    # def __int__(self):
    #     return id()

    def get_shortened(self):
        return self.shortened

    def random_address(self):  # address generator (random)
        letters = string.ascii_lowercase
        length = random.randint(4,10)
        return ''.join(random.sample(letters, length))

    def shorten_address(self):
        # if custom name not provided generate random one
        if not self.shortened:
            self.shortened = self.shortened.random_address()
        # check if shortened address is not already taken id DB
        if Addresses.objects.get(shortened__exact=self.shortened) == self.shortened:
            # TODO return proper warning, and choose another - should it be done in html instead of here?
            pass
        else:
            self.save()
