from django.db import models
from django.utils import timezone
from django import forms

class CadastroAluno(models.Model):
    nome = models.CharField(max_length=200)
    data_nascimento = models.DateField() 
    cpf = models.CharField(unique=True, max_length=14)
    ano_de_ingresso = models.SlugField(max_length=4, int)
    turno = models.ForeignKey('Turno')
    curso = models.ForeignKey('Curso')
    ano = models.ForeignKey('Serie')
    turma = models.ForeignKey('Turma')
    sus = models.SlugField(max_length=2, int)
    endereco = models.CharField(max_length=200)
    ponto_de_referência = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=50)
    telefone = models.CharField(max_length=9)
    celular = models.CharField(max_length=10)
    estado_civil = models.ForeignKey('Estado_Civil')
    filhos = models.SlugField(max_length=2, int)
    nome_responsavel = models.CharField(max_length=200)
    telefone_responsavel = models.CharField(max_length=10)

    escolha = [('True', 'Sim'),
               ('False', 'Não')]
    
    doença_no_coracao = forms.ChoiceField(choices=escolha, widget=forms.RadioSelect)
    doença_respiratoria = forms.ChoiceField(choices=escolha, widget=forms.RadioSelect)
    fumante = forms.ChoiceField(choices=escolha, widget=forms.RadioSelect)
    tem_hanseniase = forms.ChoiceField(choices=escolha, widget=forms.RadioSelect)
    consome_alcool = forms.ChoiceField(choices=escolha, widget=forms.RadioSelect)
    tratamento_psiquiatra = forms.ChoiceField(choices=escolha, widget=forms.RadioSelect)
    pressao_alta = forms.ChoiceField(choices=escolha, widget=forms.RadioSelect)
    tuberculose = forms.ChoiceField(choices=escolha, widget=forms.RadioSelect)
    diabetes = forms.ChoiceField(choices=escolha, widget=forms.RadioSelect)
    cancer = forms.ChoiceField(choices=escolha, widget=forms.RadioSelect)
    
    alergia = [('alimentar', 'Alimentar'),
               ('medicamentosa', 'medicamentosa'),
               ('outra', 'Outra'),
               ('nao', 'Não possui')]
    
    tipo_de_alergia = forms.ChoiceField(choices=alergia, widget=forms.RadioSelect)
    internado = forms.ChoiceField(choices=escolha, widget=forms.RadioSelect)
    remedio_controlado = forms.ChoiceField(choices=escolha, widget=forms.RadioSelect)
    fez_cirurgia = forms.ChoiceField(choices=escolha, widget=forms.RadioSelect)
    convulsao = forms.ChoiceField(choices=escolha, widget=forms.RadioSelect)
    gestante = forms.ChoiceField(choices=escolha, widget=forms.RadioSelect)
    desmaiou = forms.ChoiceField(choices=escolha, widget=forms.RadioSelect)
    vida_sexual_ativa = forms.ChoiceField(choices=escolha, widget=forms.RadioSelect)
    necessidade_especifica = forms.ChoiceField(choices=escolha, widget=forms.RadioSelect)
    outras_condicoes_de_saude = models.TextField()
    #Familiares
    pressao_alta_familia = forms.ChoiceField(choices=escolha, widget=forms.RadioSelect)
    diabetes_familia = forms.ChoiceField(choices=escolha, widget=forms.RadioSelect)
    tuberculose_familia = forms.ChoiceField(choices=escolha, widget=forms.RadioSelect)
    hanseniase_familia = forms.ChoiceField(choices=escolha, widget=forms.RadioSelect)
    cancer_familia = forms.ChoiceField(choices=escolha, widget=forms.RadioSelect)
    doença_no_coracao_familia = forms.ChoiceField(choices=escolha, widget=forms.RadioSelect)

class CadastroAtendimento(models.Model):
    cpf = 