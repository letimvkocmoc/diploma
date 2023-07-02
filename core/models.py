from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):

    birth_date = models.DateField(null=True, blank=True)
    image = models.ImageField(
        _('image'),
        upload_to='img_users',
        null=True,
        blank=True,
    )

    def image_(self):
        if self.image:
            from django.utils.safestring import mark_safe
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="150"/></a>'.format(self.image.url))
        else:
            return ('Нет аватарки')

    image._short_description = 'Аватарка'
    image._allow_tags = True
