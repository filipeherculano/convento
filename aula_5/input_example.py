name = input("Digite seu nome: ")
age = int(input("Digite sua idade: "))

if age >= 18:
    print ("Obrigado por se cadastrar " + name)
else:
    print ("Voce precisa ser maior de idade para se cadastrar, " + name)