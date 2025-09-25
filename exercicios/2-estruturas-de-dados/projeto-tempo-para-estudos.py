# Criaremos um script que imprimirá na tela o total de horas que uma pessoa estudou durante um determinado período:

# 1. Crie uma variável chamada "nome" e, usando o método input(), atribua a ela um nome;
nome = str(input("Digite seu nome: "))

# 2. Crie uma variável chamada "total_dias" e, usando o método input(), solicite o total de dias dedicados ao estudo por semana;
total_dias = (int(input("Quantos dias por semana você irá dedicar aos estudos: ")))

# 3. Crie uma variável chamada "total_horas" e, usanod o método input(), solicite a média de horas estudada por dia;
total_horas = input("Quantas horas você dedica por dia aos estudos: ")

# 4. Crie uma variável chamada "curso" e, usando o método input(), solicite o título do curso desejado;
cursos = str(input("Digite o titulo do curso desejado: "))

# 5. Imprima na tela uma frase informando o nome da estudante, o total_dias dedicados aos estudos, o total horas semanais e o curso.
print('Seu nome é {}, você dedica {} dias por semana, e estuda em média {} Horas por dia, o curso que estuda é {}, '.format(nome, total_dias, total_horas, cursos))