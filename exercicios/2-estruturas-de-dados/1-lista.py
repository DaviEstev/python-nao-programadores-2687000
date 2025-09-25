# Crie uma lista apenas com elementos numéricos
elementos_numericos = [1,2,3,4,5,6,7,8,9,10]
print(elementos_numericos)

# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
todos = [1,2,3,'Davi' , 'Estevam' , 'Silva' , 1.76 , 2.50, 4.60 , True , False]
print(todos)

# Imprima na tela apenas os 5 primeiros elementos da lista

print(todos[0:5])

# Crie um slice na lista para que imprima na tela os elementos de índice par

print(todos[0:-1:2])

# Remova da lista o último item

todos.pop()
print(todos)

# Insira na lista um novo item

todos.append('Hello World')
print(todos)

# Remova da lista um item específico
todos.remove('Hello World')
print(todos)
