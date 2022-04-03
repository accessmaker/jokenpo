import util
from util import logica

l = logica.Game()
ss = util.Arquivo()
arqScore=ss.abrirArquivoScore()
arqUsers=ss.abrirArquivoUsers()
rodada=0
score=0
nJogos = 0 
def Menu():
    print("-"*35)
    print("Bem-vindo ao meu jokenpô")
    print("- j : Jogar -")
    print("- m : Maior Pontuação -")
    print("- s : Sair -")
    print("-"*35)

def EscolherObjeto(nRodadas):
    while True:
        print("\n"+"-"*35)
        print("- r : Pedra -")
        print("- s : Tesoura -")
        print("- p : Papel -")
        print("- e : sair -")
        print("\n" + "-"*35)
        eo = input("Escolha uma das opções: ")
        if eo not in['r','p','s','e']:
            print("Escolha inválida")
        if eo == 'e':
            break        
        else:
            global rodada 
            global score
            global nJogos
            rodada +=1
            nJogos = nRodadas
            print(nJogos)
            adv=l.VerificarObjetoAdversario()
            l.TratarEscolha(eo,adv)
            score=l.verificar(eo,adv,rodada,score)
            print("-"*35+"\n")
            print("Pontuação: ",score)
            print("Rodada: ",rodada)
            print("-"*35+"\n")
            if int(rodada) >= int(nJogos):
                ss.gravar(arqScore,arqUsers,score)
                rodada = 0
                score = 0
                break
def mostrarMaiorScore():
    while True:
        print("-"*35)
        print("O maior Pontuador: ",arqUsers[0])
        print("O maior score: ",arqScore[0])
        print("- v : Voltar -")
        print("-"*35)
        v = input("Voltar? ")
        if v !='v':
            print("Escolha inválida")
        else:
            break
while True:
    Menu()
    op = input("Escolha uma das opções: ")
    if op not in['j','s','m']:
        print("Opção Inválida")
        continue
    if op == 'j':
        nRodada = input("Qunatas rodadas? ")
        print("Começando o jogo:")
        EscolherObjeto(nRodada)
    if op == 'm':
        mostrarMaiorScore()
    if op == 's':
        print("fechando o jogo")
        break