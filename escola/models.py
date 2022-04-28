from datetime import datetime
from django.db import models


def path_and_rename():
    """Rename the 'Aluno.foto' file received from user """
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        time_now = datetime.now()
        if instance.pk:
            filename = '{}.{}'.format(str( instance.pk) +'_'+ str(time_now) , ext)
        else:
            # set filename as timestamp string
            filename = '{}.{}'.format(str(time_now), ext)
        # return the whole path to the file
        return filename
    return wrapper


class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    celular = models.CharField(max_length=11, default="")
    foto = models.ImageField(blank = True, upload_to = path_and_rename() )

    def __str__(self):
        return str(self.nome)

class Curso(models.Model):
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado')
    )
    codigo_curso = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False,default='B')

    def __str__(self):
        return str(self.descricao)

class Matricula(models.Model):
    PERIODO = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno')
    )
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=1, choices=PERIODO, blank=False, null=False,default='M')
