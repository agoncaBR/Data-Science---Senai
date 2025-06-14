#aula6_desafio_1.py
import statistics as sts

# Dados das empresas
empresa1 = [2500, 2800, 3000, 9500, 12000]
empresa2 = [5000, 5200, 5300, 5400, 5500]
empresa3 = [1000, 2000, 8000, 15000, 20000]
empresa4 = [3500, 4000, 4200, 4300, 6000]
empresa5 = [1200, 1500, 1800, 2500, 10000]

# Lista das empresas
empresas = [empresa1, empresa2, empresa3, empresa4, empresa5]

# Inicializando variáveis para armazenar os resultados
melhor_empresa = None
pior_empresa = None
menor_desvio = float('inf')  # Desvio padrão mínimo
maior_desvio = float('-inf')  # Desvio padrão máximo

# Loop para calcular os valores para cada empresa
for i, empresa in enumerate(empresas, start=1):
    print(f'\nCálculos para Empresa {i}: {empresa}')
    empresa.sort()  # Ordena a lista de valores
    
    # Calcula a amplitude
    amplitude = max(empresa) - min(empresa)
    
    # Calcula variância e desvio padrão
    variancia = sts.variance(empresa)
    desvio = sts.stdev(empresa)
    
    # Exibe os resultados
    print(f'Amplitude: {amplitude}')
    print(f'Variância: {variancia}')
    print(f'Desvio padrão: {round(desvio, 2)}')

    # Determina a melhor empresa (menor desvio) e a pior empresa (maior desvio)
    if desvio < menor_desvio:
        menor_desvio = desvio
        melhor_empresa = i  # Armazena o índice da melhor empresa
    
    if desvio > maior_desvio:
        maior_desvio = desvio
        pior_empresa = i  # Armazena o índice da pior empresa

# Resultados finais
print(f'\nA melhor empresa é a Empresa {melhor_empresa} com desvio padrão de {round(menor_desvio, 2)}')
print(f'A pior empresa é a Empresa {pior_empresa} com desvio padrão de {round(maior_desvio, 2)}')
