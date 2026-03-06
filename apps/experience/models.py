from django.db import models


class Experience(models.Model):
    company = models.CharField(max_length=200, verbose_name="Company")
    position = models.CharField(max_length=200, verbose_name="Position")
    location = models.CharField(max_length=200, verbose_name="Location")
    start_date = models.DateField(verbose_name="Start Date")
    end_date = models.DateField(null=True, blank=True, verbose_name="End Date")
    current = models.BooleanField(default=False, verbose_name="Current Position")
    description = models.TextField(verbose_name="Description")
    achievements = models.JSONField(default=list, verbose_name="Achievements")
    technologies = models.JSONField(default=list, verbose_name="Technologies")
    logo = models.ImageField(upload_to="experience/", blank=True, verbose_name="Logo")
    order = models.IntegerField(default=0, verbose_name="Order")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-start_date", "order"]
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"

    def __str__(self):
        return f"{self.position} @ {self.company}"
