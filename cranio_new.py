from Segunda_parte import segunda_parte
from imagens import carregar_imagens
dicionario_lista={158:0,156:1,153:2,155:3,150:4,157:5,152:6,149:7,151:8,154:9,8:12345}
#Dicionario criado para que seja possivel capturar as chaves do teclado que será usado no IFPB
#Um dia capturando pockemom, e outro chaves, onde vamos parar?
while True:
    matricula=""
    cor=(255,255,255)
    chave = carregar_imagens("cranio.png").mostrar_imagem(0)
    """
    if chave==-1:
        break
    segunda_parte(matricula)
    while True:
        if chave==-1 or (chave==13 and len(matricula)==12):
            break
        elif chave!=8:
            if len(matricula)<12:
                if chave==13:
                    continue
                elif chave<100:
                    matricula+=str(chave-48)
                else:
                    try:
                        matricula+=str(dicionario_lista[chave])
                    except:
                        continue
        else:
            try:
                matricula = int(matricula)/10
                matricula = int(matricula)
                matricula = str(matricula)
            except:
                continue
            if matricula=="0":
                matricula=""
        if len(matricula)==12:
            cor=(0,255,0)
        else:
            cor=(255,255,255)
    """