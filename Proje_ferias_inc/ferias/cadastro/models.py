from django.db import models

class Férias(models.Model):
    
    nome = models.CharField(max_length=200)
    data_in = models.DateField()
    dias = models.IntegerField( )
    
    def __str__(self) -> str:
        return self.nome
    
class Departamento(models.Model):

    departamento = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.departamento

class Funcionário(models.Model):

    id = models.AutoField(primary_key= True,)
    matricula = models.CharField(max_length=9)
    nome = models.CharField(max_length=200)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.id
