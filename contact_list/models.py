from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=200, verbose_name='Имя:')
    last_name = models.CharField(max_length=200, verbose_name='Фамилия: ', blank=True)

    first_number = models.IntegerField()
    second_number = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        verbose_name = "контакт"
        verbose_name_plural = 'контакты'

