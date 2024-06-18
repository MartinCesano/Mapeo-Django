from django.db import models

class Barra(models.Model):
    numero_barra = models.CharField(max_length=50, unique=True)
    ubicacion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.numero_barra} - {self.ubicacion}"

class Consumicion(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=200)
    marca = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Venta(models.Model):
    barra = models.ForeignKey(Barra, on_delete=models.CASCADE)
    codigo = models.IntegerField()
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"Venta {self.codigo} en barra {self.barra}"

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles')
    consumicion = models.ForeignKey(Consumicion, on_delete=models.CASCADE)
    precio = models.FloatField()
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.cantidad} x {self.consumicion.nombre} (Venta {self.venta.codigo})"

class DetalleConsumicion(models.Model):
    consumicion = models.ForeignKey(Consumicion, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    cantidad_litros = models.FloatField()

    def __str__(self):
        return f"{self.cantidad_litros}L de {self.ingrediente.nombre} en {self.consumicion.nombre}"
