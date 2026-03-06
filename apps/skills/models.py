from django.db import models


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ("language", "Langage"),
        ("framework", "Framework"),
        ("tool", "Outil"),
        ("database", "Base de données"),
        ("cloud", "Cloud"),
    ]

    LEVEL_CHOICES = [
        ("beginner", "Débutant"),
        ("intermediate", "Intermédiaire"),
        ("advanced", "Avancé"),
        ("expert", "Expert"),
    ]

    name = models.CharField(max_length=100, verbose_name="Nom")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    years_experience = models.IntegerField(
        default=0, verbose_name="Années d'expérience"
    )
    icon = models.CharField(max_length=100, blank=True, verbose_name="Icône")
    order = models.IntegerField(default=0, verbose_name="Ordre")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order", "name"]
        verbose_name = "Compétence"
        verbose_name_plural = "Compétences"

    def __str__(self):
        return f"{self.name} ({self.get_level_display()})"
