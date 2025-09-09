from django.db import models

class Sueno(models.Model):
    ESTADOS = [
        ("PENDING", "Pendiente"),
        ("APPROVED", "Aprobado"),
        ("REJECTED", "Rechazado"),
    ]

    iniciales = models.CharField("Tres Iniciales", max_length=3, blank=False)
    titulo = models.CharField("Título", max_length=200)
    mensaje = models.TextField("Mensaje")
    fecha = models.DateTimeField("Fecha de creación", auto_now_add=True)
    estado = models.CharField(
        "Estado",
        max_length=9,
        choices=ESTADOS,
        default="PENDING"
    )

    def __str__(self):
        return f"[{self.iniciales}] {self.titulo}"
