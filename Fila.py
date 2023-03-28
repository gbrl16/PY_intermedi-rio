""" fila = [10, 20, 30, 40, 50]
fila.append(60)
print(fila)
print(fila.pop(0))
print(fila)
print(fila.pop(0))
print (fila)
print(fila.pop(0))
print(fila) """


""" fila = []
senha= 0
def proximo():
    global senha 
    senha += 1
    fila.append(senha)
    print(fila) 

def chamar():
    print( fila.pop(0) )
    print (fila)

while True:
    escolha =int(input('1 pegar senha e 2 chamar:'))
    if escolha == 1:
        proximo()
    elif escolha == 2:
        chamar()
    else:
        print("inválido")

 """