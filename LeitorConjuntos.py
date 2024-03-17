##Aluno: Carlos Eduardo Nogueira Morciani
##Curso: Ciência da Computação
##Enunciado : O programa que você desenvolverá irá receber como entrada um arquivo de texto (.txt) contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão representadas em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas segundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de operações que estão descritas no arquivo, este número de operações será um inteiro; as linhas seguintes seguirão sempre o mesmo padrão de três linhas: a primeira linha apresenta o código da operação (U para união, I para interseção, D para diferença e C produto cartesiano), a segunda e terceira linhas conterão os elementos dos conjuntos separados por virgulas.


#Função para ler e formatar as linhas do as linhas do arquivo
def linhas_arquivo(linha):
    with open(arquivo_lido, "r" ) as arquivo:
        leitura_linhas = arquivo.readlines()
        formatar_linha = leitura_linhas[linha].strip()
        elementos = formatar_linha.split()
        conjunto = set(elementos)
        conjunto.remove(",")

  
    return conjunto

#Entrada do arquivo
arquivo_lido= input("Coloque aqui o arquivo txt:")

#União
conjunto1 = linhas_arquivo(2)
conjunto2 = linhas_arquivo(3)
uniao = conjunto1.union(conjunto2)
formartacao_uniao = ', '.join(uniao)
print("União:", f"Conjunto 1: {{{', '.join(conjunto1)}}}", f"Conjunto 2: {{{', '.join(conjunto2)}}}", f"Resultado: {{{formartacao_uniao}}}")
print("----"*32)
print(" ")

#Interseção
conjunto3 = linhas_arquivo(5)
conjunto4 = linhas_arquivo(6)
intersecao = conjunto3.intersection(conjunto4)
formartacao_intersecao = ', '.join(intersecao)
print("Interseção:", f"Conjunto 1: {{{', '.join(conjunto3)}}}", f"Conjunto 2: {{{', '.join(conjunto4)}}}", f"Resultado: {{{formartacao_intersecao}}}")
print("----"*32)
print(" ")

#Diferença
conjunto5 = linhas_arquivo(8)
conjunto6 = linhas_arquivo(9)
diferenca = conjunto5.difference(conjunto6)
formartacao_diferenca = ', '.join(diferenca)
print("Diferença:", f"Conjunto 1: {{{', '.join(conjunto5)}}}", f"Conjunto 2: {{{', '.join(conjunto6)}}}", f"Resultado: {{{formartacao_diferenca}}}")
print("----"*32)
print(" ")

#Cartesiano
conjunto7 = linhas_arquivo(11)
conjunto8 = linhas_arquivo(12)
cartesiano = set()
for dado in conjunto7:
    for dado2 in conjunto8:
        cartesiano.add((dado, dado2))
conversao = [f"({dados[0]}, {dados[1]})" for dados in cartesiano]
formartacao_cartesiano = ', '.join(conversao)
print("Cartesiano:", f"Conjunto 1: {{{', '.join(conjunto7)}}}", f"Conjunto 2: {{{', '.join(conjunto8)}}}", f"Resultado: {{{formartacao_cartesiano}}}")

    




