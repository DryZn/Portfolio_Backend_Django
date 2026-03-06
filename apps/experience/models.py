from django.db import models


class Experience(models.Model):
    company = models.CharField(max_length=200, verbose_name="Entreprise")
    position = models.CharField(max_length=200, verbose_name="Poste")
    location = models.CharField(max_length=200, verbose_name="Localisation")
    start_date = models.DateField(verbose_name="Date de début")
    end_date = models.DateField(null=True, blank=True, verbose_name="Date de fin")
    current = models.BooleanField(default=False, verbose_name="Poste actuel")
    description = models.TextField(verbose_name="Description")
    achievements = models.JSONField(default=list, verbose_name="Réalisations")
    technologies = models.JSONField(default=list, verbose_name="Technologies")
    logo = models.ImageField(upload_to='experience/', blank=True, verbose_name="Logo")
    order = models.IntegerField(default=0, verbose_name="Ordre")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-start_date', 'order']
        verbose_name = "Expérience"
        verbose_name_plural = "Expériences"

    def __str__(self):
        return f"{self.position} @ {self.company}"
