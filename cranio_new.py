from Segunda_parte import segunda_parte
from imagens import carregar_imagens
dicionario={158:0,156:1,153:2,155:3,150:4,157:5,152:6,149:7,151:8,154:9,8:12345}
#Dicionario criado para que seja possivel capturar as chaves do teclado que será usado no IFPB
#Um dia capturando pockemom, e outro chaves, onde vamos parar?
matricula = ""
cor=(255,255,255)
primeira_imagem = carregar_imagens("cranio.jpg")
while True:
    primeira_imagem.girar_escrever(matricula,cor)
    chave = int(primeira_imagem.mostrar_imagem(0))
    print(matricula)
    #Nessa linha se carrega a imagem ao mesmo tempo que recolhe a chave do teclado
    if chave==-1 or (chave==13 and len(matricula)==12):
        break
        #Isso aqui verifica a matricula já possui o tamanho de 13 caracteres e se foi apertado o enter
    elif chave!=8:
        #A chave 8 se referi a o BlackEspace
        if len(matricula)<12:
            #Aqui essa linda função ver se a matricula ainda não está completa
            if chave==13:
                continue
                #Mais um enter, aqui ele só não reage ao que o usuario pede, por ter menos de 13 caracteres
            elif chave<100:
                #Se a chave retornar números menores que 100 siguinifica que está usando o teclado normal
                matricula+=str(chave-48)
                #No teclado normal há um padrão ao qual é respeitado, fazendo o calculo acima dar o resultado exato do número que foi apertado no teclado
            else:
                try:
                    #Aqui é para o caso de espercial dado pela escola
                    matricula+=str(dicionario[chave])
                    #Ele não respeita um padrão, se teve a nescessidade do dicionario
                except:
                    continue
    else:
        #Para caso seja o número 8 
        try:
            #Se retornar erro, é por causa que alguem deu errado e o usuario apertou uma tecla que não seria usado antes
            matricula = int(int(matricula)/10)
            #Apaga um número da matricula escrita
            matricula = str(matricula)
            #Disperça comentarios
        except:
            continue
        if matricula=="0":
            #Ao apagar toda a matricula na forma demostrada acima, corre o risco da matricula fica no final com a strig "0", aqui corrige
            matricula=""
    if len(matricula)==12:
        #Aqui muda para a cor verde ao atingir o total de números de uma matricula normal
        #Desejo trocar para ficar verde caso a matricula esteja no banco de dados
        cor=(0,255,0)
    else:
        cor=(255,255,255)
    #Pretendo Escrever na imagem de entrada, isso já tem feito no Primeira_parte, mas irei colocar junto com o arquivo de imagens.py