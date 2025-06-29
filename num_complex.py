class Complexo:
    def __init__(self, real, img):
            #atribui
            self.real = real
            self.img = img

def complexo_novo(real, img):
    #retorna um objeto com os valores
    return Complexo(real, img)

def complexo_soma(a, b):
    #retorna um novo numero com a soma das partes
    return complexo_novo(a.real + b.real, a.img + b.img)

def complexo_imprime(a):
    #imprimir no formato padrão
    if a.img >= 0:
        print(f"{a.real} + {a.img}i") #a + bi
    else:
        print(f"{a.real} - {-a.img}i") #a - bi

def complexos_iguais(a, b):
    #se são iguais
    return a.real == b.real and a.img == b.img
    #retorna verdadeiro e falso se não forem iguais

def complexo_mult(a, b):
    return complexo_novo(a.real * b.real - a.img * b.img,
                        a.real * b.img + b.real * a.img)

def complexo_conjugado(a):
    #retorna com a parte imaginaria negativa
    return complexo_novo(a.real, -a.img)

def main():
    #cria
    a = complexo_novo(5,3)
    b = complexo_novo(2,5)
    c = complexo_soma(a, b)
    
    print('SOMA'.center(8,'-'))
    complexo_imprime(a)
    complexo_imprime(b)
    print('RESULTADO'.center(13,'-'))
    complexo_imprime(c)

    print('='.center(18,'='))
    print('='.center(18,'='))

    print('MULTIPLICAÇÃO'.center(17,'-'))
    print(f'({a.real} + {a.img}i) * ({b.real} + {b.img}i) = ({a.real}⋅{b.real} - {a.img}⋅{b.img}) + ({a.real}⋅{b.img} + {b.real}⋅{a.img})i')
    print('RESULTADO'.center(13,'-'))
    d = complexo_mult(a,b)
    complexo_imprime(d)

if __name__=='__main__':
    main()

#SAIDA

# --SOMA--
# 5 + 3i
# 2 + 5i
# --RESULTADO--
# 7 + 8i
# ==================
# ==================
# --MULTIPLICAÇÃO--
# (5 + 3i) * (2 + 5i) = (5⋅2 - 3⋅5) + (5⋅5 + 2⋅3)i
# --RESULTADO--
# -5 + 31i