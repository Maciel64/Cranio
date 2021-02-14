from Segunda_parte import segunda_parte
from imagens import carregar_imagens
dicionario_lista={158:0,156:1,153:2,155:3,150:4,157:5,152:6,149:7,151:8,154:9,8:12345}
#Dicionario criado para que seja possivel capturar as chaves do teclado que será usado no IFPB
#Um dia capturando pockemom, e outro chaves, onde vamos parar?
matricula = ""
cor=(255,255,255)
while True:
    chave = int(carregar_imagens("cranio.jpg").mostrar_imagem(0))
    print(matricula)
    #Nessa linha se carrega a imagem ao mesmo tempo que recolhe a chave do teclado
    if chave==-1 or (chave==13 and len(matricula)==12):
        break
        #Isso aqui verifica a matricula já possui o tamanho de 13 caracteres e se foi apertado o enter
        #A chave 8 se referi a o BlackEspace
    elif chave!=8:
        if len(matricula)<12:
            if chave==13:
                continue
                #Mais um enter, aqui ele só não reage ao que o usuario pede, por ter menos de 13 caracteres
            elif chave<100:
                matricula+=str(chave-48)
            else:
                try:
                    matricula+=str(dicionario_lista[chave])
                except:
                    continue
    else:
        try:
            matricula = int(int(matricula)/10)
            #Apaga um número da matricula escrita
            matricula = str(matricula)
            #Volta ao formato que estava sendo trabalhado antes
        except:
            continue
        if matricula=="0":
            matricula=""
    if len(matricula)==12:
        cor=(0,255,0)
    else:
        cor=(255,255,255)
    #Desculpa, pretendo colocar todas os comentarios depois
    #Depois verei uma melhor forma de tirar isso tudo daqui
    #Além de que pretendo Escrever na imagem de entrada, isso já tem feito no Primeira_parte, mas irei colocar junto com o arquivo de imagens.py