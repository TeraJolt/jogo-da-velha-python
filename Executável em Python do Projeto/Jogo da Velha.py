print("Jogo da Velha - Alpha 0.1")
player1_score=0
player2_score=0
empat_score=0
start=int(input("[1]-Iniciar \n[2]-Sair \n"))
while start == 1:
    A1=" "; A2=" "; A3=" "; B1=" "; B2=" "; B3=" "; C1=" "; C2=" "; C3=" "
    esc_simb=int(input("Escolha um simbolo para o Jogador 1 \n[1]- O  [2]- X \n*ao selecionar um simbolo para o Jogador 1 o Jogador 2 recebera o outro simbolo\n"))
    if esc_simb == 1:
        player1="O"; player2="X"
    elif esc_simb == 2:
        player1="X"; player2="O"
    print("\n   | A || B || C |")
    print("|1|[",A1,"][",B1,"][",C1,"]")
    print("|2|[",A2,"][",B2,"][",C2,"]")
    print("|3|[",A3,"][",B3,"][",C3,"]")
    while (A1==" " or A2==" " or A3==" " or B1==" " or B2==" " or B3==" " or C1==" " or C2==" " or C3==" ") and start==1:
        rep1=1
        while rep1==1 and start==1:
            jogadap1=str(input("\nInsira a coordenada da célula a ser preenchida pelo Jogador 1: "))
            if (jogadap1 == "A1" or jogadap1 == "a1") and A1==" ":
                A1=player1
                rep1=0
            elif (jogadap1 == "A2" or jogadap1 == "a2") and A2==" ":
                A2=player1
                rep1=0
            elif (jogadap1 == "A3" or jogadap1 == "a3") and A3==" ":
                A3=player1
                rep1=0
            elif (jogadap1 == "B1" or jogadap1 == "b1") and B1==" ":
                B1=player1
                rep1=0
            elif (jogadap1 == "B2" or jogadap1 == "b2") and B2==" ":
                B2=player1
                rep1=0
            elif (jogadap1 == "B3" or jogadap1 == "b3") and B3==" ":
                B3=player1
                rep1=0
            elif (jogadap1 == "C1" or jogadap1 == "c1") and C1==" ":
                C1=player1
                rep1=0
            elif (jogadap1 == "C2" or jogadap1 == "c2") and C2==" ":
                C2=player1
                rep1=0
            elif (jogadap1 == "C3" or jogadap1 == "c3") and C3==" ":
                C3=player1
                rep1=0
            else:
                print("Célula já preenchida, porfavor tente novamente!")
            if A1==A2==A3==player1 or B1==B2==B3==player1 or C1==C2==C3==player1 or A1==B1==C1==player1 or A2==B2==C2==player1 or A3==B3==C3==player1 or A1==B2==C3==player1 or A3==B2==C1==player1:
                print("\nJogador 1 é o Vencedor!!")
                player1_score = player1_score + 1
                start = 3
        print("\n   | A || B || C |")
        print("|1|[",A1,"][",B1,"][",C1,"]")
        print("|2|[",A2,"][",B2,"][",C2,"]")
        print("|3|[",A3,"][",B3,"][",C3,"]")
        rep2=1
        while rep2==1 and (A1==" " or A2==" " or A3==" " or B1==" " or B2==" " or B3==" " or C1==" " or C2==" " or C3==" ") and start==1:
            jogadap2=str(input("\nInsira a coordenada da célula a ser preenchida pelo Jogador 2: "))
            if (jogadap2 == "A1" or jogadap2 == "a1") and A1==" ":
                A1=player2
                rep2=0
            elif (jogadap2 == "A2" or jogadap2 == "a2") and A2==" ":
                A2=player2
                rep2=0
            elif (jogadap2 == "A3" or jogadap2 == "a3") and A3==" ":
                A3=player2
                rep2=0
            elif (jogadap2 == "B1" or jogadap2 == "b1") and B1==" ":
                B1=player2
                rep2=0
            elif (jogadap2 == "B2" or jogadap2 == "b2") and B2==" ":
                B2=player2
                rep2=0
            elif (jogadap2 == "B3" or jogadap2 == "b3") and B3==" ":
                B3=player2
                rep2=0
            elif (jogadap2 == "C1" or jogadap2 == "c1") and C1==" ":
                C1=player2
                rep2=0
            elif (jogadap2 == "C2" or jogadap2 == "c2") and C2==" ":
                C2=player2
                rep2=0
            elif (jogadap2 == "C3" or jogadap2 == "c3") and C3==" ":
                C3=player2
                rep2=0
            else:
                print("Célula já preenchida, porfavor tente novamente!")
            if A1==A2==A3==player2 or B1==B2==B3==player2 or C1==C2==C3==player2 or A1==B1==C1==player2 or A2==B2==C2==player2 or A3==B3==C3==player2 or A1==B2==C3==player2 or A3==B2==C1==player2:
                print("\nJogador 2 é o Vencedor!!")
                player2_score = player2_score + 1
                start = 3
            print("\n   | A || B || C |")
            print("|1|[",A1,"][",B1,"][",C1,"]")
            print("|2|[",A2,"][",B2,"][",C2,"]")
            print("|3|[",A3,"][",B3,"][",C3,"]")
    if start == 1:
        print("\nDeu Velha!!")
        empat_score = empat_score + 1
    print("\n       Placar de Pontos")
    print("|Jogador 1|Jogador 2|Empates|")
    print("|   ",player1_score,"   |   ",player2_score,"   |  ",empat_score,"  |")
    if start == 3 or start == 1:
        start=int(input("\n[1]-Iniciar nova partida\n[2]-Sair\n"))
if start == 2:
    print("Fim de Jogo!")
    
