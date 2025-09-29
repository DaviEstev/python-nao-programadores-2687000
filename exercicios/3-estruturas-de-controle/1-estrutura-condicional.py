# Declare 4 variáveis do tipo numérica

var1 = 10
var2 = 20
var3 = 30

# Crie uma estrutura condicional para comparar dois números

# Se a condição for verdadeira, imprima na tela uma mensagem informando que a condição foi cumprida e informando o número de maior valor

# Se a condição não for cumprida, imprima na tela uma mensagem informando que a condição é negativa e informe o número de maior valor

# Insira outras condições na estrutura condicional usando o elif

# Incremente a estrutura condicional já existente com expressões lógicas utilizando "and" ou "or"

if (var1) > (var2) or (var3):
  print("{} é maior que {}".format(var1 , var2))
elif(var3 == var2):
  print("{} é igual a {}".format(var3, var2))
else:
  print("{} não é maior que {}".format(var1 , var2))

# Crie uma estrutura condicional onde mais de uma condição seja verdadeira, e use apenas a palavra reservada "if"

if(var1) < (var2):
  print("{} é menor que {}".format(var1, var2))
if(var2) < (var3):
  print("{} é menor que {}".format(var2, var3))