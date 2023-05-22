from django.db import models

class Cliente(models.Model):
    '''
        Classe referente a tabela de pessoa do banco de dados
    '''
    nome = models.CharField(max_length=255, null=False, blank=False)
    data_nasc = models.DateField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    profissao = models.CharField(max_length=255, null=False, blank=False) 
    