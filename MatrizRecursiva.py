from Matriz_Base import MatrizBase

class MatrizRecursiva(MatrizBase):
    def determinante_recursivo(self):
        """
        Calcula el determinante de la matriz 3x3 usando un método recursivo.
        """
        def determinante_2x2(m):
            return m[0][0] * m[1][1] - m[0][1] * m[1][0]

        # Expansión por la primera fila
        det = 0
        for i in range(3):
            submatriz = [
                [self.matriz[j][k] for k in range(3) if k != i]
                for j in range(1, 3)
            ]
            signo = (-1) ** i
            det += signo * self.matriz[0][i] * determinante_2x2(submatriz)
        return det