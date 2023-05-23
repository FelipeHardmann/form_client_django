from django.db import models

class Endereco(models.Model):
    ESTADO_CHOICES = (
        ('AC', 'Acre'), 
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranão'),
        ('MG', 'Minas Gerais'),
        ('MS', 'Mato Grosso do Sul'),
        ('MT', 'Mato Grosso'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PE', 'Pernanbuco'),
        ('PI', 'Piauí'),
        ('PR', 'Paraná'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('RS', 'Rio Grande do Sul'),
        ('SC', 'Santa Catarina'),
        ('SE', 'Sergipe'),
        ('SP', 'São Paulo'),
        ('TO', 'Tocantins')
    )
    rua = models.CharField(max_length=255, null=False, blank=False)
    numero = models.IntegerField(null=False, blank=False)
    bairro = models.CharField(max_length=255, null=False, blank=False)
    cidade = models.CharField(max_length=255, null=False, blank=False)
    estado = models.CharField(choices=ESTADO_CHOICES, max_length=2, null=False, blank=False)


class Cliente(models.Model):
    '''
        Classe referente a tabela de pessoa do banco de dados
    '''
    nome = models.CharField(max_length=255, null=False, blank=False)
    data_nasc = models.DateField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    profissao = models.CharField(max_length=255, null=False, blank=False) 
    endereco = models.OneToOneField(to=Endereco, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f'{self.nome} - {self.email}'
    # 


class Dependente(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    telefone = models.CharField(max_length=12, null=False, blank=False)
    titular = models.ForeignKey(to=Cliente, on_delete=models.CASCADE, null=False, blank=False)
