from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
# ============================================================================ #


# =================================== USER =================================== #
class User(AbstractUser):

    username = models.CharField(
        'Login',
        max_length=150,
        unique=True,
        help_text='Nick name',
        validators=[
            RegexValidator(
                regex=r'^[\w.@+-]+',
                message=('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.')
            )
        ]
    )
    email = models.EmailField(max_length=254,unique=True,)
    first_name = models.CharField(max_length=150,blank=True,null=True,)
    last_name = models.CharField(max_length=150,blank=True,null=True,)
    confirmation_code = models.CharField(max_length=255,null=True,blank=False,)
    bio = models.TextField(
                            blank=True,
                            null=True,
                            help_text='User biography',
    )
    class Meta:
        ordering = ('username',)

    def __str__(self) -> str:
        return self.username