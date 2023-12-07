# Aproximação de pi com base na agulha de Buffon.

# -------------------------------------------

# Imports de operações básicas

from numpy.random import rand
from numpy.random import seed as set_seed
from numpy import pi, sqrt, cos

# -------------------------------------------

# Definindo classes e funções

class Agulha:

    '''
    Aqui definimos as propriedades básicas da agulha: x, theta e l. Bem auto-explicativo, mas é relevante comentar que l possui um valor padrão de 1.
    '''

    def __init__(self, x, theta, l = 1):
        self.x = x
        self.theta = theta
        self.l = l

    '''
    Depois, definimos a função de checagem.
    '''

    def checar(self):

        # Primeiro extraímos as propriedades do objeto agulha:

        l = self.l
        theta = self.theta
        x = self.x

        # Depois calculamos L = 2l e fazemos a distância horizonal s.

        L = 2*l
        s = (l*cos(theta))/2

        '''
        Como as posições das retas sempre são x = 0 e x = L, podemos calcular
        a distância até elas fazendo L-x e x-0, mas só precisamos do menor, 
        então usamos a função min().
        '''

        b = min(x, L-x)

        # Finalmente checamos se cruza ou não

        if s >= b: 
            return True
        
        else:
            return False

    """
    Aqui definimos a função que gera uma agulha aleatória.
    Como a função rand() gera um número aleatório entre zero
    e um, basta mutliplicarmos pelo limite que queremos para 
    obter um valor aleatório no intervalo desejado.
    """

def jogada(l = 1):
    L = 2*l
    return Agulha(x = rand()*L, theta = rand()*(pi/2), l=l)


"""
Finalmente, definimos a função de cálculo de pi.
"""

def calcula_pi(N, seed = 1):
    N_acertos = 0

    # Remova o comentário abaixo para fixar a semente, caso desejado.
    
    #set_seed(seed) 

    for _ in range(N):
        agulha = jogada() # Jogamos uma agulha aleatória...

        if agulha.checar(): # Checamos se ela "acertou"...
            N_acertos += 1  # E, se sim, somamos ao número total de acertos.

    p = N_acertos/N # Finalmente, estimamos a probabilidade com a razão simples.

    pi_buffon = 1/p # Utilizamos ela para estimar pi.

    sigma = p/sqrt(N) # Depois usamos a definição dada em sala para calcular o erro da simulação.

    erro = abs(pi_buffon - pi) # E comparamos com o valor de pi do pacote numpy para determinar o erro real.

    return pi_buffon, sigma, erro # Finalmente, retornamos todos os valores em uma tupla.

# -------------------------------------------

# Executando e imprimindo:

N = int(input('Quantas iterações? '))

pi_buffon, sigma, erro = calcula_pi(N)

print(f'Resultado: \n Estimativa de pi: {pi_buffon} \n Erro da simulação: {sigma} \n Erro real: {erro}' )
