# Nome: Renan Cristyan A. Pinheiro
# Matrícula: 17/0044386
# Disciplina: Estruturas de Dados 2 - 2019/2
# Professor: Maurício Serrano

# Algorítmos de Ordenação O(n^2)

from random import randint

# Testa o desempenho dos 3 algorítmos (bubble, insertion e selection)
# e exibe os resultados
def teste_de_desempenho(funcao):
    pass

# Cria um vetor aleatorio de tamanhos variaveis
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

# Implementação do Selection Sort
def selection_sort(vetor):
    menor = vetor[0]
    i_menor = 0 # Indice do menor
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

# Alguns exemplos
b = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]
i = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]
s = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]

print('bubble')
print(b)
bubble_sort(b)
print(b)

print('insertion')
print(i)
insertion_sort(i)
print(i)

print('selection')
print(s)
selection_sort(s)
print(s)
