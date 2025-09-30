# Crie uma função para selecionar o curso desejado em uma trilha profissional

def selecionaCurso():
  print("Selecione o curso que deseja: 1 - HTML , 2 - CSS , 3 - JavaScript")
  seleciona = int(input("Digite Aqui: "))
  if (seleciona) == 1:
      print("Curso selecionado: HTML")
  elif (seleciona) == 2:
     print("Curso selecionado: CSS")
  elif (seleciona) == 3:
     print("Curso selecionado: JavaScript")
  else:
     print("Valor Inválido")

  return seleciona
     

# Crie uma função para percorrer todos os níveis de um curso e imprimir na tela a informação do nível atual

def nivelCurso():
   niveis = range(11)
   for item in niveis:
      print("Nível atual do curso: {}".format(item))
   else:
      print("Parabéns, você finalizou o curso")

   return niveis

# Execute as funções

selecionaCurso()
nivelCurso()

        