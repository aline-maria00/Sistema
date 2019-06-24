from django.db import models
from django.utils import timezone

class AlunoCadastro(models.Model):
    nome = models.CharField(max_length=200)
    data_nascimento = models.DateField() 
    cpf = models.CharField(unique=True, max_length=14)
    ano_de_ingresso = models.SlugField(max_length=4, int)
    turno = models.ForeignKey('Turno', on_delete=models.CASCADE)
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE)
    ano = models.ForeignKey('Serie', on_delete=models.CASCADE)
    turma = models.ForeignKey('Turma', on_delete)
    sus = models.SlugField(max_length=2, int)
    endereco = models.CharField(max_length=200)
    ponto_de_referência = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=50)
    telefone = models.CharField(max_length=9)
    celular = models.CharField(max_length=10)
    estado_civil = models.ForeignKey('Estado_Civil', on_delete=models.CASCADE)
    filhos = models.SlugField(max_length=2, int)
    nome_responsavel = models.CharField(max_length=200)
    telefone_responsavel = models.CharField(max_length=10)