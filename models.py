class Metro():
    def __init__(self,valor):
        self.valor = valor
        
    def para_cm(self,valor):
        valor = valor * 100 
        return valor

class Centimetro():
    def __init__(self,valor):
         self.valor = valor

    def para_m(self,valor):
        valor = valor / 100  
        return valor

#print(para_cm(5))
#print(para_m(12))
