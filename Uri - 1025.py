"""
Todos os seus amigos estão loucos pelo filme "Interstellar". Agora eles estão postando textos no Facebook em Código Morse. 
Você precisa escrever um código para decodificar Morse!

Este Código Morse contém somente letras minúsculas (a-z) e espaços em branco.

Nota - Código Morse é uma forma de codificar caracteres em uma sequências de pontos e traços. 
Cada caracter tem uma codificação fixa. Um exemplo bem famoso é o Morse de SOS "...---..." . S é codificado como "..." 
(ponto ponto ponto) e O é codificado como "---" (traço traço traço).
Neste problema, um ponto é denotado por "=" e um traço por "===". Símbolos são separados por "." , letras são separadas por "..." 
e palavras são separadas por "......." .
Sendo assim, SOS é codificado como =.=.=...===.===.===...=.=.=
Codificações para todos os caracteres podem ser encontradas no link abaixo.

http://morsecode.scphillips.com/morse2.html

Entrada
A entrada consiste em múltiplos casos de teste.

A primeira linha de cada entrada contém o número de casos de teste (t)(1 <= t <= 10).

As próximas t linhas contém os Códigos Morse. O tamanho de cada código é menor que 1000 caracteres.


Saída
A saída é divida em linhas, que representam a mensagem decodificada de cada caso de teste.
"""
# Unecessaray, could use range(0,tam,2) instead.
def gerador(vetor):
    tam = len(vetor)
    j = 0
    while j < tam:
        if j % 2 == 1:
            yield j
        j += 1


string = """A	.-	N	-.
B	-...	O	---
C	-.-.	P	.--.
D	-..	Q	--.-
E	.	R	.-.
F	..-.	S	...
G	--.	T	-
H	....	U	..-
I	..	V	...-
J	.---	W	.--
K	-.-	X	-..-
L	.-..	Y	-.--
M	--	Z	--.."""
# The site was unavailable,so I just copied the table from Wikipedia.
string = string.lower()
string = string.split()
dicio = {}
# Make a dictionary morse ---> alphabet
for index in gerador(string):
    cod = list(string[index])
    for i in range(len(cod)):
        if cod[i] == '.':
            cod[i] = '='
        else:
            cod[i] = '==='
    string[index] = ".".join(cod)
    dicio[string[index]] = string[index - 1]
    
qtd = int(input())
# Uses the dictionary for translate 
for i in range(qtd):
    entrada = input().split(".......")
    maxi = len(entrada)
    cont = 0
    for palavra in entrada:
        cont += 1
        letras = palavra.split("...")
        for letra in letras:
            if letra in dicio:
                print(dicio[letra], end='')
        if cont < maxi:
            print(" ", end='')
    if i < qtd:
        print("\n", end="")
