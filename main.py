from Matriz_Base import MatrizBase
from MatrizRecursiva import MatrizRecursiva
from MatrizIterativa import MatrizIterativa

# Ejemplo de uso
if __name__ == "__main__":
    matriz = [
        [2, 3, 1],
        [4, 5, 6],
        [7, 8, 9]
    ]

    matriz_obj = MatrizBase(matriz)
    
    matriz_recursiva = MatrizRecursiva(matriz)
    print("Determinante (recursivo):", matriz_recursiva.determinante_recursivo())

    # Usando MatrizIterativa
    matriz_iterativa = MatrizIterativa(matriz)
    print("Determinante (iterativo):", matriz_iterativa.determinante_iterativo())