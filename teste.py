#aula6_funcoes_estatisitcas.py
from collections import Counter
import statistics as st

def moda(lista):
    # Conta quantos elementos tem na lista - Conta a quantidade de ocorrências de cada valor.
    frequencias = Counter(lista)
    
    # Encontrar a maior frequência
    maior_frequencia = max(frequencias.values())
    print(f'maior_frequencia: {maior_frequencia}')
   
    # Se a maior frequência for 1, utiliza-se o primeiro item da lista ordenada
    # Mesmo caso do mulodo statistics
    if maior_frequencia == 1:
        return sorted(lista)[0]
    
    # Obter todos os valores que possuem a maior frequência
    modas = []
    for item, freq in frequencias.items():
        if freq == maior_frequencia:
            modas.append(item)
    
    # Se há mais de um valor com a maior frequência, retorna uma lista
    # Caso contrário, retorna o único valor como um número
    if len(modas) == 1:
        return modas[0]  # Retorna o único valor se for unimodal
    return modas  # Retorna todos os valores se for multimodal

def mediana(lista):
    # Ordena a lista
    lista_ordenada = sorted(lista)
    
    # Número de elementos na lista - retorna o tamanho de um objeto
    n = len(lista_ordenada)
    
    # Se o número de elementos for ímpar, a mediana é o valor do meio
    if n % 2 != 0:
        return lista_ordenada[n // 2]
    
    # Se o número de elementos for par, a mediana é a média dos dois valores centrais
    else:
        meio1 = lista_ordenada[(n // 2) - 1]
        print(f'meio1: {meio1}')
        meio2 = lista_ordenada[n // 2]
        print(f'meio2: {meio2}')

        return (meio1 + meio2) / 2
'''
# Exemplos de uso
dados_impar = [7, 1, 3, 5, 9]
dados_par = [7, 1, 3, 5]

print(f'Mediana (ímpar): {mediana(dados_impar)}')  # Saída esperada: 5
print(f'Mediana (par): {mediana(dados_par)}')      # Saída esperada: 4
'''

def media(lista):
    # Verifica se a lista não está vazia
    if len(lista) == 0:
        return None  # Retorna None se a lista estiver vazia, para evitar divisão por zero
    
    # Calcula a soma de todos os elementos
    soma = sum(lista)
    
    # Calcula a quantidade de elementos
    n = len(lista)
    
    # Calcula a média
    return soma / n
'''
# Exemplos de uso
dados = [1, 2, 3, 4, 5]
print(f'Média: {media(dados)}')  # Saída esperada: 3.0

dados_vazios = []
print(f'Média (lista vazia): {media(dados_vazios)}')  # Saída esperada: None
'''