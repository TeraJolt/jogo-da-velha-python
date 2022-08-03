# Jogo da Velha
> ### 1. O porque do projeto:
* O projeto de um Jogo da Velha em Python é um ótimo desafio de programação para iniciantes, envolvendo ciclos de repetição e condições.

> ### 2. O que minha versão apresenta:
* Minha versão consiste em um jogo da velha de terminal, sendo feito para 2 jogadores.
* O primeiro jogador pode escolher o simbolo, se será ou O ou X.
* O funcionamento de localização de jogadas é feito por coordenadas, já que temos uma matriz.
* Sendo A, B e C as colunas e 1, 2 e 3 as linhas. Exemplo:
    
        [ ][A ][B ][C ]
        [1][A1][B1][C1]
        [2][A2][B2][C2]
        [3][A3][B3][C3]
* Supondo que o Jogador 1 escolheu ser o X e escolheu a célula A1 então a célula A1 receberá a marcação do Jogador 1 que neste momento é representado pelo X.

        [ ][A][B][C]
        [1][X][ ][ ]
        [2][ ][ ][ ]
        [3][ ][ ][ ]

* Quando o primeiro ou o segundo jogador alinhar o simbolo (O ou X) receberá a vitória, lançando um placar de vitórias e perguntando se desejam jogar novamente, se sim o jogo será reiniciado mas o placar não, o placar ainda é por variaveis, apenas armazena seus dados enquanto o programa é executado, quando o programa for fechado o placar zera, mas enquanto o jogo tiver novas partidas ele continuará contabilizando as vitórias.