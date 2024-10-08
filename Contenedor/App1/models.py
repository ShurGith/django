from django.db import models

# Create your models here.

class AutorDb(models.Model):
    nombre = models.CharField(max_length=75, verbose_name="Nombre")
    fecha_nacimiento = models.DateField(verbose_name="Fecha Nacimiento", null=False, blank=False)
    fecha_fallecimiento = models.DateField(verbose_name="Fecha Fallecimiento", null=True,blank=True)
    nacionalidad = models.CharField(max_length=50, verbose_name="Nacionalidad")
    profesion = models.CharField(max_length=50, verbose_name="Profesion")

    class Meta:
        db_table = "Autores"
        verbose_name = "Autor"
        verbose_name_plural="Autores"

    def __str__(self) -> str:
        return self.nombre

class FraseDb(models.Model):
    cita = models.TextField(max_length=400, verbose_name="Frase")
    autor_fk = models.ForeignKey(AutorDb, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Frase o Cita"
        verbose_name_plural=  "Frases o Citas"

