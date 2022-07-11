
#Desafio36 - Emprestimo Bancario...
""" #valorcasa = float(input("digite o valor da casa:")) 
#salario = float(input("digite o seu salario:"))
#ano = int(input("digite quantos anos ira pagar:"))
#prestacao = valorcasa / (ano * 12)
#minimo = salario * 30 /100
#print("para pagar a casa de R${:.2f} em {} anos".format(valorcasa,ano), end ="")
#print("a prestação sera de  R${:.2f}".format(prestacao))
#if prestacao <= minimo:
#    print("emprestimo concedido:")
#else:
#    print("emprestimo negado ") """

#Desafio 37 Conversor de Bases..

""" num = int(input("digite um numero inteiro:"))
print("escolha umas da opçoes para converter")
print("digite 1 para converter binario:")
print("digite 2 para converter octal:")
print("digite 3 para converter hexadecimal:")
opcao = int(input("digite a sua opção:"))

if opcao == 1:
    print("{} convertido para binario é igual a {}".format(num, bin (num)))
elif opcao ==2:
    print("{} convertido para octal é igual a {}".format(num, oct(num)))
elif opcao ==3:
    print("{} convertido para octal é igual a {}".format(num, hex(num)))
else:
    print("opção invalida tente novamente:") """

#desafio 38 - comparando numeros

""" n1 = float(input("digite o primeiro numero:"))
n2 = float(input("digite o segundo numero:"))

if n1 > n2:
    print("o numero 1 é maior:")
elif n2 > n1:
    print("o numero 2 e maior:")
elif n1 == n2:
    print("os numeros são iguais:") """

#desafio 39 -- Alistamento Militar..
""" from datetime import date 
atual = date.today().year
nasc = int(input("digite a data de nascimento:")) 
idade = atual - nasc
print("quem nasceu em {} tem {} em {}".format(nasc, idade , atual))
if idade == 18:
    print("voce deve se alistar urgentemente")

elif idade <18:
    saldo = 18 - idade
    print("voce não precisa se alistar ainda",saldo)
   

elif idade > 18:
    saldo = idade - 18
    print("ja passou o tempo do alistamento",saldo) """

#desafio 40 - Media da nota
""" n1 = float(input("digite a primeira nota:"))
if n1 >10:
    print("valor invalido:")
    exit()
n2 = float(input("digite a segunda nota:"))
if n2 > 10:
    print("valor invalido")
    exit()
media = (n1 + n2)/2

if media <5:
    print("sua media é",media,"Reprovado")
elif media >7:
    print("Parabéns sua media é:",media,"Parabéns esta aprovado:")
elif media >5 and media <7:
    print("a sua media é",media,"estude mais voce esta em recuperação:") """

#desafio 41 - Classificando os Atletas..
""" from datetime import date 
atual = date.today().year
nasc = int(input("digite a data de nascimento:")) 
idade = atual - nasc

if idade <=9:
    print("você tem",idade,"anos portanto a sua categoria é MIRIN:")
elif idade <=14:
    print("voce tem",idade,"anos portanto a sua categoria é INFANTIL:")
elif idade <=19:
    print("voce tem",idade,"anos portanto a sua categoria é JUNIOR:")
elif idade <=25:
    print("voce tem",idade,"anos portanto a sua categoria é SENIOR:")
elif idade >25:
    print("voce tem",idade,"anos portanto a sua categoria é MASTER:") """

#desafio 42 - Analisando os Triangulos
""" n1 = int(input("digite um segmento:"))
n2 = int(input("digite um segmento:"))
n3 = int(input("digite um segmento:"))

if n1 == n2 == n3:
    print("Equilatero todos os lados são iguais:")
elif n1 != n2 != n3 != n1:
    print("ESCALENO todos os lados são diferentes:")
else:
    print("ISOCELES dois lados iguais é um diferente:") """

#desafio 43 - IMC - massa corporal
""" peso = float(input("digite o seu peso:"))
altura = float(input("digite a sua altura:"))
imc = peso/ (altura **2)

if imc <18.5:
    print("abaixo do peso:",imc)
elif imc >=18.5 and imc <25:
    print("Esta no peso ideal:",imc)
elif imc >=25 and imc <30:
    print("sobrepeso:",imc)
elif imc >=30  and imc <=40:
    print("Obesidade:",imc)
elif imc >40:
    print("Obesidade morbida:",imc) """

#Desafio 44 - Gerenciador de Pagamentos..
""" print("lojinha do Wetinho")
preco = float(input("digite o valor a ser pago:"))
print("[1] á vista dinheiro.")
print("[2] á vista no cartão.")
print("[3] 2x no cartão.")
print("[4] 3x ou mais no cartão.")
opcao = str(input("digite a opção:"))
desconto = 0

if opcao == "1":
    desconto = (preco *10) / 100
    desconto1 = preco - desconto
    print(" o valor da compra era{} com o desconto ficou{}".format(preco,desconto1))
elif opcao == "2":
    desconto = (preco *5) / 100
    desconto1 = preco - desconto
    print(" o valor da compra era {} com o desconto ficou {}".format(preco,desconto1))
elif opcao == "3":
    print(" o valor da compra é:",preco)
elif opcao == "4":
    desconto = (preco *20) / 100
    desconto1 = preco + desconto
    print(" o valor da compra era {} com o juros ficou {}".format(preco,desconto1)) """

#Desafio45 -- JO KEN PO --

""" from random import randint
itens = ("Pedra","Papel","Tesoura")
computador = randint(0,2)
print("suas jogadas são")
print("[0] PEDRA")
print("[1] PAPEL")
print("[2] TESOURA")
print("O computador escolheu{}".format(itens[computador]))
jogador = int(input("Qual sua jogada?"))
print("computador jogou {}".format(itens[computador]))
print("jogador jogou {}".format(itens[jogador]))

if computador == 0: #computador jogou pedra
    if jogador ==0:
        print("EMPATE")
    elif jogador == 1:
        print("jogador Vence")
    elif jogador == 2:
        print("computaodr VENCE")
    else:
        print("jogada invalida")

elif computador ==1: #computador jogou papel
    if jogador ==0:
        print("computaodr VENCE")
    elif jogador ==1:
        print("EMPATE")
    elif jogador ==2:
        print("JOGADOR VENCE")
    else:
        print("jogada invalida")

elif computador ==2: #computador jogou tesoura
    if jogador =print(soma)=0:
        print("jogador VENCE")
    elif jogador ==1:
        print("COMPUTADOR VENCE")
    elif jogador ==2:
        print("EMPATE")
    else:
        print("jogada invalida") """

#DESAFIO 46 contagem regressiva##
""" import time
for i in range(10,-1, -1):
    time.sleep(1)
    print(i)
print("BUM! NUM! POW!!!") """

#desafio 47 mostrar numeros pares de 1 a 50
""" for i in range(2, 51, 2):
    print(i) """

#desafio 48  soma impares mutiplas de 3 
""" soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 ==0:
        cont = cont + 1
        soma  = soma + c
        print(c)
        print(" a soma de todos os valores solicitados é:",soma)
        print("foi somado:",cont,"vezes")
 """
 #desafio 49 tabuada 2.0 em FOR 
""" nume = int(input("digite um numero:"))
for c in range(1, 11):
        conta = nume * c
        print("{} x {} = {} ".format(nume,c,conta))
 """
#desafio 50 soma dos pares
""" soma = 0
cont = 0
for c in range(1,7):
    num = int(input("digite o {} valor".format(c)))
    if num % 2 ==0:
        soma = soma + num
        cont = cont +1
    print("voce informou {} pares e a soma foi {}".format(cont,soma)) """

#desafio 51 Progressão aritmetica
""" primeiro = int(input("digite o primeiro termo:"))
razao = int(input("digite a razão:"))
decimo = primeiro + (10 -1) * razao
for i in range(primeiro,decimo,razao):
    print("{}".format(i), end="-")
print("ACABOU E TRETA:") """

#desafio 52 Numeros Primos..
""" num = int(input("digite um numero:"))
for c in range(1, num+1):
    if num % c ==0:
        print("\033[34", end =" ")
    else:
        print("\033[m", end = " ")
    print("{}".format(c), end = " ")
 """
#Desafio 53 Detector de palindromo
""" frase = str(input("digite uma frase:")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""
for letra in range(len(junto) -1, -1,- 1):
    inverso += junto [letra]
print(junto, inverso)
if inverso == junto:
    print("temos um palimetro.")
else:
    print("a frase digitada não e um palimetro") """

#Desafio 54 grupo da maioridade
""" from datetime import date 
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8): 
    nasc = int(input("em que ano a {}º pessoa nasceu:".format(pess)))
    idade = atual - nasc
    print(pess)
    if idade >=18:
        totmaior += 1
    else:
        totmenor += 1
print("ao todo tivemos {} pessoa maiores de idade".format(totmaior))
print("ao todo tivemos {} pessoa menores de idade".format(totmenor)) """

#Desafio 55 maior e menor da sequencia.
""" maior = 0 
menor = 0
for p in range(1,6):
    peso = float(input("digite o peso da {} pessoa:".format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("o maior peso lido foi {}kg".format(maior))
print("o menor peso lido foi {}kg".format(menor)) """

#Desafio 56 Analisador completo -- idade,nome,sexo
""" somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ""

for p in range(1,5):
    print("-------{} pessoa ------".format(p))
    nomee = str(input("nome:")).strip()
    idade = int(input("idade:"))
    sexo = str(input("sexo[M/F]")).strip()
    somaidade += idade 
    if p == 1 and sexo in "Mm":
        maioridadehomem = idade
        nomevelho = nomee
    if sexo in "Mm" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nomee


mediaidade = somaidade /4
print("a media de idade do grupo é de {}anos".format(mediaidade))
print(" o homem mais velho tem {} anos e se chama {}".format(maioridadehomem,nomevelho)) """

### AULA 14 Estrutura de repetição WHILE ###

#Desafio 57 Validação de dados
""" cont = 0
sexo = str(input("digite seu sexo M/F:")).strip().upper()[0]
while sexo not in "MmFf":
    sexo = input("dados invalidos informe os seu sexo:").strip().upper()[0]
    cont = cont + 1
print("sexo {} registrado com sucesso".format(sexo))
print("voce errou {} vezes ".format(cont)) """

#Desafio 58 jogo da adivinhação 2.0
""" cont = 0
print("ola sou seu computador ")
print("Acabei de pensar em um numero de 1 a 10")
print("sera que você consegue adivinhar qual foi?...")
numero = int(input("qual o seu palpite?"))
while numero != 9:
    numero = int(input("Você errou tente novamente:"))
    cont = cont +1
print("parabéns você acertou o numero",numero)
print("mas foram {} tentativas".format(cont))"""

#desafio 59 criando um menu de opções
""" n1 = int(input("digite o primeiro:"))
n2 = int(input("digiteo segundo numero:"))
opcao = 0

while opcao != 5:
    print("[1]Somar [2]Multiplicar [3]Maior [4]Novos numeros [5]Fechar o programa")
    opcao = int(input("digite a sua opcão:"))
    if opcao == 1:
        soma = n1 + n2
        print("a soma do {} e {} é {}".format(n1,n2,soma))

    elif opcao ==2:
        multi = n1 * n2
        print("a multiplicação entre {} e {} é {}".format(n1,n2,multi))
    
    elif opcao ==3:
        if n1 > n2:
            maior = n1
            print("O {} e o maior".format(n1))
        else:
            print("o maior é o {}".format(n2))
    
    elif opcao == 4:
        print("informe os numeros novamentes:")
        n1 = int(input("digite o primeiro numero:"))
        n2 = int(input("digiteo segundo numero:"))

    elif opcao == 5:
        print("finalizado...")

    else:
        print("opção invalida tente novamente")    
print("FIM do programa volte sempre:")
 """

#Desafio 60 - Fatorial
""" valor = int(input("Digite um número inteiro:"))
#inicializa variáveis
contador = valor - 1
resultado = valor
saida = str(valor) + "!" + " = " + str(valor)
#print(saida)
while contador>=1:
    resultado = resultado * contador #realiza multiplicação (considerando resultado anterior)
    saida = saida + " x " + str(contador) #monta saída de dados
    print(saida) #mostra saída intermediária (não é obrigatório)
    contador = contador - 1 #decremento do contador
saida = saida + " = " + str(resultado)
print(saida) """

#Desafio 61 Progressão aritmetica
""" print("Gerador de PA:")
primeiro = int(input("primeiro termo:"))
razao = int(input("digite a razão da PA"))
termo = primeiro 
cont = 1
while cont <= 10:
    print("{} -->".format(termo), end = "-")
    termo = termo + razao
    cont += 1 """

#Desafio 64 - Tratando varios Valores
""" num = cont = soma = 0
while num != 999:
    num = int(input("digite um numero[999 para parar]"))
    soma += num
    cont += 1
    numero = num + num
print("Voce digitou {} numeros e a soma entre eles é {}".format(cont -1,soma - 999))
 """
#Desafio 65 Maior e Menores Valores
""" resp = "S"
soma = quant = media = maior = menor = 0
while resp in "Ss":
    num = int(input("digite um numero:"))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
            if num < menor:
                menor = num

    resp = str(input("Quer continuar [S/N]")).upper().strip()[0]
media = soma / quant
print("voce digitou {} numeros e a media foi {}".format(quant, media))
print("o maior valor foi {} e o menor valor foi {}".format(maior,menor))
 """

#Desafio 66 Varios numeros com flags
""" soma = cont = 0
while True:
    num = int(input("digite um numero [999] para parar o programa:"))
    if num == 999:
        break
    cont += 1
    soma += num
print("Você digitou {} vezes e a soma dos números deu {}.".format(cont,soma))    """

#Desafio 67 tabuada 3.0
""" while True:
    n = int(input("Quer ver a Tabuada de que valor?"))
    print("-" * 30)
    if n <= 0:
        break
    print("Programa de TABUADA encerrado volte sempre:")
    for c in range(1,11):
        print(" {} x {}  = {}".format(n,c, n*c))
    print("-" * 30) """

#Desafio 68 Jogo do Par ou Impar
""" from random import randint

while True:
    jogador = int(input("digite um valor:"))
    computador = randint(0,10)
    total = jogador + computador

    tipo = str(input("PAR ou INPAR:")).strip().upper
    print("voce jogou {} e o computador jogou {}".format(jogador, computador)) """

#Desafio 69 Analise de dados do grupo..
""" tot18 = toth =  totm20 = 0
while True:
    idade = int(input("Idade:"))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo: [M/F]")).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == "M":
        toth += 1
    if sexo == "F" and idade < 20:
        totm20 += 1
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer Continuar?  [S/N]")).strip().upper()[0]
    if resp == "N":
        break
print("total de pessoas com mais de 18 anos {}".format(tot18))
print("ao todo temos {} homens cadastrados".format(toth))
print("E temos {} mulheres com menos de 20 anos:".format(totm20)) """
