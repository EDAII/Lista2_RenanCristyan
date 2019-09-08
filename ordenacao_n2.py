# Nome: Renan Cristyan A. Pinheiro
# Matrícula: 17/0044386
# Disciplina: Estruturas de Dados 2 - 2019/2
# Professor: Maurício Serrano

# Algorítmos de Ordenação O(n^2)

# Rsultados de algumas observações e experimentos:
# Selection Sort é o algoritmo mais rápido
# Insertion Sort tem desempenho mediano
# Bubble Sort é o algoritmo mais lento

import matplotlib.pyplot as plt
from random import randint
from time import time

# Testa o desempenho dos 3 algorítmos (bubble, insertion e selection)
# e exibe os resultados
def teste_de_desempenho(n):
    vetor_b = vetor_aleatorio(n)
    vetor_i = vetor_b[:]
    vetor_s = vetor_b[:]

    measure(selection_sort, vetor_s)
    measure(insertion_sort, vetor_i)
    measure(bubble_sort, vetor_b)

# Mede o desempenho de cada função individualmente
def measure(func, vetor, retornar_t_exec=False):
    start = time()
    func(vetor)
    finish = time()
    t_exec = finish - start

    print('{} ordena {} elementos em \t{} segundos'.format(func.__name__, len(vetor), t_exec))

    if retornar_t_exec:
        return t_exec

# Cria um vetor aleatorio (sem números repetidos) de tamanho variavel
def vetor_aleatorio(tam):
    vetor = []

    i = 0
    while i < tam:
        num = randint(0,tam)
        if num not in vetor:
            vetor.append(num)
            i += 1

    return vetor

# Troca os valores de posição dentro do vetor
def swap(vetor, a, b):
    aux = vetor[a]
    vetor[a] = vetor[b]
    vetor[b] = aux

# Implementação do Bubble Sort
def bubble_sort(vetor):
    tam = len(vetor)
    i, j = 0, 0

    while i < tam:
        
        while j < tam-1:
            if vetor[j] > vetor[j+1]:
                swap(vetor, j, j+1)
            j += 1
        
        i += 1
        j = 0

# Implementação do Insertion Sort
def insertion_sort(vetor):
    tam = len(vetor)
    i, j = 0, 0

    while i < tam:
        j = i

        while (j != 0) and vetor[j] < vetor[j-1]:
            swap(vetor, j, j-1)
            j -= 1
        
        i += 1

# Implementação do Selection Sort
def selection_sort(vetor):
    menor = vetor[0]
    i_menor = 0
    tam = len(vetor)
    i, j = 0, 0

    while i < tam:

        while j < tam:
            if vetor[j] < menor:
                menor = vetor[j]
                i_menor = j
            j += 1

        swap(vetor, i, i_menor)
        i += 1
        j = i
        menor = 10000000
        i_menor = 10000000

def teste_de_desempenho_aprimorado(mostrar_grafico=True):
    x = [0]
    ys, yi, yb = [0], [0], [0]

    j = 1
    while j <= 5:
        x.append(1000*j)
        ys.append(measure(selection_sort, vetor_aleatorio(1000*j), retornar_t_exec=True))
        j += 1
    plt.plot(x, ys, 'b--', label='selection sort')
    print('\n')

    j = 1
    while j <= 5:
        yi.append(measure(insertion_sort, vetor_aleatorio(1000*j), retornar_t_exec=True))
        j += 1
    plt.plot(x, yi, 'g--', label='insertion sort')
    print('\n')

    j = 1
    while j <= 5:
        yb.append(measure(bubble_sort, vetor_aleatorio(1000*j), retornar_t_exec=True))
        j += 1
    plt.plot(x, yb, 'r--', label='bubble sort')
    print('\n')
    
    if mostrar_grafico:
	    plt.axis([0, 5020, 0, 20])
	    plt.suptitle('Desempenho da função')
	    
	    plt.xlabel('numero de elementos')
	    plt.ylabel('tempo')
	    
	    plt.legend(loc='upper left')
	    plt.show()

# teste_de_desempenho(10000)
teste_de_desempenho_aprimorado()