import random

def sorteando_numero():
    return random.randint(1,100)

def verificar_chute(numero_sorteado,chute,continuar=None):
    
    if numero_sorteado > chute:
        print('Chute mais alto!!')
        
    elif numero_sorteado < chute:
        print('Chute mais baixo!!')
        
    elif numero_sorteado == chute:
        return True