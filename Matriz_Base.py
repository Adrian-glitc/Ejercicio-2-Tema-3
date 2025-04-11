class MatrizBase:
    def __init__(self, matriz):
        if len(matriz) != 3 or any(len(fila) != 3 for fila in matriz):
            raise ValueError("La matriz debe ser de 3x3.")
        self.matriz = matriz


