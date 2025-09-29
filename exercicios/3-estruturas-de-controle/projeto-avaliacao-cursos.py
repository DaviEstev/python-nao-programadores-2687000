# Nesse desafio você verificará dentro de uma lista se o item estar contido nela, caso verdadeiro deverá imprimir na tela essa informação, além disso deverá solicitar avaliação para o item e armazená-la em um dicionário.

# 1. Crie uma lista com 5 diferentes cursos do LinkedIn Learning

cursos = ['JavaScript', 'Python', 'HTML', 'CSS', 'PHP']

# 2. Crie 3 variáveis do tipo string e associe 1 curso a cada uma delas

var1 = 'JavaScript'
var2 = 'Python'
var3 = 'HTML'

# 3. Crie um dicionário vazio para armazenar a nota do curso

vazio = {}

# 4. Crie uma estrutura condicional para verificar se cada variável está contida na lista
# 5. Se o curso estiver na lista, solicite uma nota para avaliação

if (var1) in (cursos):
  print("O curso se encontra na lista!, por favor, avalie-o")
  vazio['nota_javascript'] = int(input("Digite aqui sua avaliação do curso de {}: ".format(var1)))
if (var2) in (cursos):
  print("O curso se encontra na lista!, por favor, avalie-o")
  vazio['nota_python'] = int(input("Digite aqui sua avaliação do curso de {}: ".format(var2)))
if (var3) in (cursos):
  print("O curso se encontra na lista!, por favor, avalie-o")
  vazio['nota_HTML'] = int(input("Digite aqui sua avaliação do curso de {}: ".format(var3)))
else: 
  print("O curso(s) não se encontram na lista!")

# 6. Armazene essa nota no dicionário, sendo a chave o título do curso e o valor a nota

print(vazio)
  

