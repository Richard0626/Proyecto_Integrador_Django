from django.db import models

class Categoria(models.Model):
    id_cat = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100,null=False,blank=False)
    fec_re = models.DateField('Fecha de Registro')

    def __str__(self) :
        return self.nombre


class Comida(models.Model):
    id_com = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    idCategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE,verbose_name='Categoria')
    descrip = models.CharField(max_length=250,verbose_name='Descripcion')
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(blank=False,null=False)
    img= models.ImageField(upload_to='eatfood/images')

    def __str__(self):
        return self.nombre

class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    id_com = models.ForeignKey(Comida, on_delete=models.CASCADE)  
    cantidad = models.IntegerField(blank=False,null=False)
    def __str__(self):
            return self.id_com