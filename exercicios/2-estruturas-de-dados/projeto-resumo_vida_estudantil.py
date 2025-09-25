# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica

nome = str(input("Digite seu nome: "))
conheceuLinkedin = int(input("Digite o ano em que conheceu o linkedin: "))
anoAtual = int(input("Digite o ano atual: "))
cursos = str(input("Digite todos os cursos que você realizou no linkedin, separador pro virgula e em ordem cronológica: "))

# 2. Armazene esses dados em um dicionário

dados = {'nome' : nome , 'Ano que conheceu o Linkedin' : conheceuLinkedin , 'Ano Atual' : anoAtual , 'Cursos' : cursos.split(', ')}

# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.

total_anos = dados['Ano Atual'] - dados['Ano que conheceu o Linkedin']
total_cursos = len(dados['Cursos'])

print('\n Seu nome é {}, você conheceu o Linkedin no ano de {}, você já está no linkedin a {} Anos, você já realizou {} cursos no LinkedIn Learning, sendo seu primeiro {}, e seu último curso feito {}'
      .format(dados['nome'], dados['Ano que conheceu o Linkedin'], total_anos, total_cursos, dados['Cursos'][0], dados['Cursos'][-1]),'.')