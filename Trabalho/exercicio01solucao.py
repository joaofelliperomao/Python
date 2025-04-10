import threading
import random
import time


# Função original do QuickSort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]  # Elementos menores ou iguais ao pivô
    right = [x for x in arr[:-1] if x > pivot]  # Elementos maiores que o pivô
    return quicksort(left) + [pivot] + quicksort(right)


# Função do QuickSort com paralelismo
def quicksortP(arr, result):
    if len(arr) <= 1:
        result.extend(arr)
        return

    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot] # Elementos menores ou iguais ao pivô
    right = [x for x in arr[:-1] if x > pivot] # Elementos maiores que o pivô

    antesOrdenacao = []
    depoisOrdenacao = []

    t1 = threading.Thread(target=quicksortP, args=(left, antesOrdenacao)) # Cria nova thread com os menores ou iguais ao pivô
    t2 = threading.Thread(target=quicksortP, args=(right, depoisOrdenacao)) # Cria nova thread com os maiores ao pivô

    # Inicia threads
    t1.start()
    t2.start()

    # Faz o programa esperar a conclusão das threads
    t1.join()
    t2.join()

    # Retorna o resultado
    result.extend(antesOrdenacao + [pivot] + depoisOrdenacao)


# Função para gerar números aleatórios
def gerar_numeros_aleatorios(n=100, min_val=1, max_val=200):
    return [random.randint(min_val, max_val) for _ in range(n)]


if __name__ == "__main__":
    numeros = gerar_numeros_aleatorios(100)
    numerosP = numeros

    print("Números antes da ordenação Pararela:", numerosP[:10])

    numeros_ordenadosP = []
    startP = time.time()
    quicksortP(numerosP, numeros_ordenadosP)
    endP = time.time()

    print("Números antes da ordenação:", numeros[:10])
    numeros_ordenados = []
    start = time.time()
    numeros_ordenados = quicksort(numeros)
    end = time.time()

    print("\nNúmeros após a ordenação pararela:", numeros_ordenadosP, "\nTempo Paralelo:", endP - startP)
    print("\nNúmeros após a ordenação:", numeros_ordenados, "\nTempo:", end - start)