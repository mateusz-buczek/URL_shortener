from django.db import models
import random
import string


class Address(models.Model):
    original = models.URLField()
    shortened = models.CharField(max_length=30, blank=True)  # input for custom name

    def __str__(self):
        return f"{self.shortened} ({self.original})"

    def get_shortened_address(self):
        return self.shortened

    def get_original_address(self):
        return self.original

    def random_address(self):  # address generator (random), provides lowercase name 4 to 10 letters long

        return

    def shorten_address(self):
        # if custom name not provided generate random one
        while self.shortened == '':
            letters = string.ascii_lowercase
            length = random.randint(4, 10)
            self.shortened = ''.join(random.sample(letters, length))
            if Address.objects.get(shortened__exact=self.shortened) == self.shortened:
                self.shortened = ''
                continue
            else:
                return self
        # if custom name provided, check if not taken
        if Address.objects.get(shortened__exact=self.shortened) == self.shortened:
            return False
        else:
            return self
