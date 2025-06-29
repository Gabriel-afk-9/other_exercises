class Lista:
    def __init__(self, capacidade_maxima=100):
     
        self.capacidade_maxima = capacidade_maxima
        self.vetor = [None] * capacidade_maxima 
        self.tamanho = 0    
    def lista_vazia(self):
        return self.tamanho == 0

    def lista_cheia(self):
        return self.tamanho == self.capacidade_maxima

    def inserir(self, valor):
        if self.lista_cheia():
            print("Erro: Lista cheia!")
            return False
        
        pos = 0 
        while pos < self.tamanho and self.vetor[pos] < valor:
            pos += 1
        
        for i in range(self.tamanho, pos, -1):
            self.vetor[i] = self.vetor[i-1]
        
        
        self.vetor[pos] = valor
        self.tamanho += 1
        
        print(f"Inserido: {valor} || Lista: {self.vetor[:self.tamanho]}") 
        return True

    def remover(self, valor): 
        removidos = 0 
        i = 0        
        while i < self.tamanho:
            if self.vetor[i] == valor:
                for j in range(i, self.tamanho - 1):
                    self.vetor[j] = self.vetor[j + 1]
                
                self.tamanho -= 1  
                removidos += 1
            else:
                i += 1
        
        if removidos > 0:
            print(f"Removido: {valor} ({removidos} ocorrências) || Lista: {self.vetor[:self.tamanho]}")
            return True
        else:
            print(f"Valor {valor} não encontrado na lista")
            return False

    def busca_binaria(self, valor):
        esquerda, direita = 0, self.tamanho - 1 
        
        while esquerda <= direita:
            meio = (esquerda + direita) // 2 
            
            if self.vetor[meio] == valor:
                print(f"Valor {valor} encontrado na posição {meio}")
                return meio
            
            elif self.vetor[meio] < valor:
                esquerda = meio + 1
            
            else:
                direita = meio - 1 
        
        print(f"Valor {valor} não encontrado na lista")
        return -1 

    def imprimir(self):
        print("Lista:", end=" ")
        for i in range(self.tamanho):
            print(self.vetor[i], end=" ")
        print()

    def verificar_ordenada(self):

        for i in range(self.tamanho - 1):
            if self.vetor[i] > self.vetor[i + 1]:
                return False
        return True


if __name__ == "__main__":
    lista = Lista(10)
    
    lista.inserir(30)  
    lista.inserir(10)  
    lista.inserir(20)  
    lista.inserir(40)  
    lista.inserir(30)  
    lista.inserir(50)  
    
    
    lista.busca_binaria(20)  
    lista.busca_binaria(35)  
    
   
    lista.remover(30) 
    lista.remover(48) 
    

    lista.imprimir()

         #SAÍDA

# Inserido: 30 || Lista: [30]
# Inserido: 10 || Lista: [10, 30]
# Inserido: 20 || Lista: [10, 20, 30]
# Inserido: 40 || Lista: [10, 20, 30, 40]
# Inserido: 30 || Lista: [10, 20, 30, 30, 40]
# Inserido: 50 || Lista: [10, 20, 30, 30, 40, 50]
# Valor 20 encontrado na posição 1
# Valor 35 não encontrado na lista
# Removido: 30 (2 ocorrências) || Lista: [10, 20, 40, 50]
# Valor 48 não encontrado na lista
# Lista: 10 20 40 50