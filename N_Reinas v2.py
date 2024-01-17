import time
# import matplotlib .pyplot as plt

def es_seguro(tablero, fila, columna, n):
    for i in range(fila):
        if tablero[i] == columna or \
           tablero[i] - i == columna - fila or \
           tablero[i] + i == columna + fila:
            return False
    return True

def colocar_reinas(tablero, fila, n, estrategia_poda=True, estrategia_heuristica=False):
    if fila == n:
        return 1
    
    soluciones_encontradas = 0
    for columna in range(n):
        if estrategia_heuristica and fila == 0:
            tablero[fila] = 0
        else:
            tablero[fila] = columna
        
        if not estrategia_poda or es_seguro(tablero, fila, columna, n):
            soluciones_encontradas += colocar_reinas(tablero, fila + 1, n, estrategia_poda, estrategia_heuristica)
    
    tablero[fila] = -1  # Retrocede si no es posible colocar la reina actual
    return soluciones_encontradas

def resolver_n_reinas(n, estrategia_poda=True, estrategia_heuristica=False):
    tablero = [-1] * n
    return colocar_reinas(tablero, 0, n, estrategia_poda, estrategia_heuristica)

def medir_tiempo(func, *args):
    inicio = time.time()
    func(*args)
    fin = time.time()
    return fin - inicio

def generar_grafica(tiempos, estrategia):
    tamanios_problema = list(range(4, 9))  # Reducir el rango a 4 a 8 para obtener resultados más rápidos
    
   # plt.plot(tamanios_problema, tiempos, marker='o', label=estrategia)
   # plt.xlabel('Tamaño del problema (N)')
   # plt.ylabel('Tiempo de ejecución (segundos)')
   # plt.title('Rendimiento del algoritmo de N reinas')
   # plt.legend()
   # plt.show()

def comparar_rendimiento():
    estrategias = ["Sin optimización", "Estrategia de poda", "Estrategia heurística"]
    
    for i, estrategia in enumerate(estrategias):
        tiempos_ejecucion = []
        for n in range(4, 9):  # Medir tiempos para N de 4 a 8
            tiempo_promedio = medir_tiempo(resolver_n_reinas, n, i == 1, i == 2)
            tiempos_ejecucion.append(tiempo_promedio)
        generar_grafica(tiempos_ejecucion, estrategia)

comparar_rendimiento()
