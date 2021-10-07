from django.db import models


class Mobil(models.Model):
  name = models.CharField(max_length=191, null=False, blank=False)
  prie = models.DecimalField(max_digits=4, decimal_places=2)
  description = models.TextField()
  color = models.TextField()

  def __str__(self):
      return self.name
  