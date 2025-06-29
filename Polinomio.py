class Polinomio:
    def __init__(self, coeficientes):
        self.coeficientes = coeficientes

    def calcular_grau(self):
        return len(self.coeficientes) - 1

    def avaliar(self):
        termos_nao_nulos = []
        termo_independente = self.coeficientes[0]

        for coef in self.coeficientes:
            if coef !=0:
                termos_nao_nulos.append(coef)


        return termo_independente,self.calcular_grau(),termos_nao_nulos
        
    def __add__(self, outro):

        tamanho_max = max(len(self.coeficientes), len(outro.coeficientes))
        
        coef_self = self.coeficientes + ([0] * (tamanho_max - len(self.coeficientes)))
        coef_outro = outro.coeficientes + ([0] * (tamanho_max - len(outro.coeficientes)))
        
        coef_soma = [a + b for a, b in zip(coef_self, coef_outro)]
        
        return Polinomio(coef_soma)

    def __str__(self) -> str:
        termos = []
        
        for i, coef in enumerate(self.coeficientes):
            if coef == 0:
                continue
            
            if i == 0:
                termos.append(f"{coef}")
            elif i == 1:
                if coef == 1:
                    termos.append("x")
                elif coef == -1:
                    termos.append("-x")
                else:
                    termos.append(f"{coef}x")
            else:
                if coef == 1:
                    termos.append(f"x^{i}")
                elif coef == -1:
                    termos.append(f"-x^{i}")
                else:
                    termos.append(f"{coef}x^{i}")
        return " + ".join(termos[::-1]).replace(" + -", " - ") if termos else "0"


def main():
    p1 = Polinomio([4,7, 1])
    p2 = Polinomio([2, 1])

    p3 = p1 + p2

    print(" P1 ".center(20, "-"))
    print(f"Representação de p1: {p1}")
    termo_independente_p1,grau_p1,termos_nao_nulos_p1 = p1.avaliar()
    print(f"Termo independente de p1: {termo_independente_p1}")
    print(f"Grau de p1: {grau_p1}")
    print(f"Coeficientes: {termos_nao_nulos_p1}\n")

    print(" P2 ".center(20, "-"))    
    print(f"Representação de p2: {p2}")
    termo_independente_p2,grau_p2,termos_nao_nulos_p2 = p2.avaliar()
    print(f"Termo independente de p2: {termo_independente_p2}")
    print(f"Grau de 2: {grau_p2}")
    print(f"Coeficientes: {termos_nao_nulos_p2}\n")

    print(" Soma ".center(20, "-"))
    print(f"Soma: {p3}\n")


if __name__ == "__main__":
    main()

#SAIDA

#-------- P1 --------
#Representação de p1: x^2 + 7x + 4
#Termo independente de p1: 4
#Grau de p1: 2
#Coeficientes: [4, 7, 1]

#-------- P2 --------
#Representação de p2: x + 2
#Termo independente de p2: 2
#Grau de p2: 1
#Coeficientes: [2, 1]

#------- Soma -------
#Soma: x^2 + 8x + 6