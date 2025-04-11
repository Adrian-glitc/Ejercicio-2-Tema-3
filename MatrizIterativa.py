from Matriz_Base import MatrizBase

class MatrizIterativa(MatrizBase):
    def determinante_iterativo(self):
        """
        Calcula el determinante de la matriz 3x3 usando un método iterativo.
        """
        a, b, c = self.matriz[0]
        d, e, f = self.matriz[1]
        g, h, i = self.matriz[2]

        # Fórmula del determinante de una matriz 3x3
        det = (a * e * i + b * f * g + c * d * h) - (c * e * g + b * d * i + a * f * h)
        return det
