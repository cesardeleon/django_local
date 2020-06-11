from django.db import models
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

class Registro_Pediatras (models.Model):
    # Aquí se hace el registro de los pediatras
    Nombres = models.CharField(max_length=50)
    Apellidos = models.CharField(max_length=50)
    
    #Concatenar el nombre del Pediatra
    def Nombre_Completo(self):
        cadena = "{0} {1}"
        return cadena.format(self.Nombres, self.Apellidos)

    def __str__(self):
        return self.Nombre_Completo()

class Generar_cita(models.Model):
    #Aquí se registra la cita en el sistema
    Pediatra = models.ForeignKey(Registro_Pediatras, null=False, blank=False, on_delete=models.CASCADE)
    Email = models.EmailField(null=True, blank=False)
    Dia = models.DateField()
    Hora = models.TimeField()
    Comentarios = models.TextField(max_length=200)

    #Concatenar pediatra y cita
    def Cita_Completa(self):
        cadena = 'Cita: {0},{1},{2}'
        return cadena.format(self.Pediatra, self.Dia, self.Hora)
    
    #Concatenar Cita y comentarios para Email
    def Cita_Completa2(self):
        cadena = 'Cita: {0}, {1}, {2}. {3}'
        return cadena.format(self.Pediatra, self.Dia, self.Hora, self.Comentarios)
    
    #Envío de Correo al Pediatra
    def envio_mail(self):
        Asunto = 'Cita Agendada'
        mail = EmailMultiAlternatives(Asunto,
            self.Cita_Completa2(),
            'cdeleongalindo@gmail.com',
            [self.Email]
            )
        mail.send()
        Exito = self.Cita_Completa() + 'Envío Exitoso'
        return Exito
    
    #Muestra de la cita en la pagina y envío al pediatra
    def __str__(self):
        return self.envio_mail()
        

     

   
    
        
