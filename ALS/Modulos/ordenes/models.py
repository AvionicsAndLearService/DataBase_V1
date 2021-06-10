from django.db import models

# Create your models here.

class orden(models.Model):
    ot=models.CharField(max_length=40, primary_key=True)
    matricula=models.CharField(max_length=150)
    cliente=models.CharField(max_length=15, null=True, blank=True)
    hangar=models.CharField(max_length=40)
    modelo=models.CharField(max_length=40)
    serie=models.CharField(max_length=40, null=True, blank=True)
    tt_planeador=models.CharField(max_length=40, null=True, blank=True)
    ct_planeador=models.CharField(max_length=40, null=True, blank=True)
    tt_motor1=models.CharField(max_length=40, null=True, blank=True)
    ct_motor1=models.CharField(max_length=40, null=True, blank=True)
    tt_motor2=models.CharField(max_length=40, null=True, blank=True)
    ct_motor2=models.CharField(max_length=40, null=True, blank=True)
    reporte=models.TextField(max_length=7000)
    acciones_correctivas=models.TextField(max_length=7000)
    estados= [
         ('C', 'Concluido'),
         ('P', 'Pendiente'),
         ('T', 'Trabajando')
    ]
    estado=models.CharField(max_length=1, choices=estados, default='P')
    observaciones=models.TextField(max_length=7000)
    tecnico=models.CharField(max_length=100)
    horas=models.CharField(max_length=15)
    fecha=models.TimeField(auto_now_add=True)

    def __str__(self):
        txt="{0}  {1}  {2}"
        return txt.format(self.ot, self.matricula, self.estado)
    
    class Meta:
        verbose_name='Orden'
        verbose_name_plural='Ordenes'

class contabilidad(models.Model):
    orden_trabajo=models.ForeignKey(orden, null=False, blank=False, on_delete=models.CASCADE)
    precio=models.CharField(max_length=40)
    pagos= [
         ('C', 'Concluido'),
         ('P', 'Pendiente'),
         ('T', 'Trabajando')
    ]
    pago=models.CharField(max_length=1, choices=pagos, default='P')
    observaciones=models.TextField(max_length=7000)
    fecha=models.TimeField(auto_now_add=True)

    def __str__(self):
        txt="{0}  {1}  {2}"
        return txt.format(self.orden_trabajo, self.precio, self.pago)
    
    class Meta:
        verbose_name='Contabilidad'
        verbose_name_plural='Contabilidad'