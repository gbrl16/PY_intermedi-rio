'''pilha = [ 1, 1, 2, 3,5]
print('pilha', pilha)
pilha.append(8)
print('inserindo um elemento: ' , pilha)
pilha.append(13)
print('inserindo outro elemnto:' , pilha)
pilha.pop()
print('removendo um elemento:' , pilha)
pilha.pop()
print('removento outro elemento' , pilha)'''


""" livro = [ 1, 2, 3, 4, 5]
print('livro' , livro)
livro.append(6)
print('inserindo um elemento:', livro)
livro.pop()
print('removendo um elemento:' , livro)
print('ultimo elemento:' , livro[-1])
livro.pop()
print('removendo um elemento:' , livro)
livro.pop()
print('removendo um elemento:' , livro)
livro.pop()
print('removendo um elemento:' , livro)
livro.append(4)
print('inserindo um elemento:' , livro)
livro.append(5)
print('inserindo um elemento:' , livro) """


'''L=[]
def adicionar(livro):
    L.append(livro)
adicionar('l1')
adicionar('l2')
adicionar('l3')
adicionar('l4')
adicionar('l5')
print(L)'''


""" ps = []
def adicionar():
    ps.append('x')
    print(ps)

def lavar():
    if len(ps) > 0:
        ps.pop()
    else:
        print('sem pratos sujos')

while True:
    escolha = int(input("1 para adicionar e 2 para lavar:"))
    if escolha == 1:
        adicionar()
    elif escolha == 2:
        lavar()
    else:
        print("opção invalida")

adicionar('p1')
adicionar('p2')
adicionar('p3')
adicionar('p4')
print(ps)



lavar()
lavar()
lavar()
print(ps)
 """


