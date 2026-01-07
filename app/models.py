from django.db import models
from django.conf import settings


# Create your models here.
class Ebook(models.Model):
    titre=models.CharField(max_length=125)
    slug= models.SlugField(max_length=128)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='image')
    pdf=models.FileField(upload_to="pdf",null=True)
    date_ajout=models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.titre



#######

class UserEbook(models.Model):
    """
    Relie un utilisateur (Client) à un ebook téléchargé.
    Sert à construire la page 'Mes ebooks'.
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="mes_ebooks"
    )

    ebook = models.ForeignKey(
        Ebook,
        on_delete=models.CASCADE
    )

    date_telechargement = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Empêche les doublons
        unique_together = ("user", "ebook")

    def __str__(self):
        return f"{self.user.username} - {self.ebook.titre}"
