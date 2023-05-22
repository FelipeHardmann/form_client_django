'''
    Arquivo com poder de criar as próprias tamplatetags
    ficando a disposição do programador utilizar ou não
'''
from django import template

register = template.Library()


@register.filter(name="remover_caracter")
def remover_caracter(var, caracter):
    '''
        Função de tamplate tag com o objetivo de retirar a letra que o programador desejar
    '''
    return var.replace(caracter, '')