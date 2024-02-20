def media():
    print("*********************")
    print("O aluno foi aprovado?")
    print("*********************")

    nota1 = input("Digite a primeira nota: ")
    nota2 = input("Digite a segunda nota: ")
    nota3 = input("Digite a terceira nota: ")

    media = (float(nota1) + float(nota2) + float(nota3))/3

    if media >= 7:
        print("O aluno foi aprovado!")
    elif media > 3 and media < 7:
        print("o aluno está de prova final")
    else:
        print("o aluno está reprovado")
    
    print("média", media)
    
media()