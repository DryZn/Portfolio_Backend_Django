from django.db import models


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ("language", "Language"),
        ("framework", "Framework"),
        ("tool", "Tool"),
        ("database", "Database"),
        ("cloud", "Cloud"),
    ]

    LEVEL_CHOICES = [
        ("beginner", "Beginner"),
        ("intermediate", "Intermediate"),
        ("advanced", "Advanced"),
        ("expert", "Expert"),
    ]

    name = models.CharField(max_length=100, verbose_name="Name")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    years_experience = models.IntegerField(
        default=0, verbose_name="Years of Experience"
    )
    icon = models.CharField(max_length=100, blank=True, verbose_name="Icon")
    order = models.IntegerField(default=0, verbose_name="Order")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order", "name"]
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    def __str__(self):
        return f"{self.name} ({self.get_level_display()})"
