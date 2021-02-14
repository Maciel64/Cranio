from Segunda_parte import segunda_parte
#O nome será esse temporariamente
from imagens import carregar_imagens
dicionario_lista={158:0,156:1,153:2,155:3,150:4,157:5,152:6,149:7,151:8,154:9,8:12345}
#Dicionario criado para que seja possivel capturar as chaves do teclado que será usado no IFPB
#Um dia capturando pockemom, e outro chaves, onde vamos parar?
while True:
    matricula=""
    cor=(255,255,255)
    recolher_matricula()
    if saida==-1:
        break
    segunda_parte(matricula_sorteio)
    while True:
        self.imagem_pricipal()
        if self.saida==-1 or (self.saida==13 and len(self.matricula_sorteio)==12):
            break
        elif self.saida!=8:
            if len(self.matricula_sorteio)<12:
                if self.saida==13:
                    continue
                elif self.saida<100:
                    self.matricula_sorteio+=str(self.saida-48)
                else:
                    try:
                        self.matricula_sorteio+=str(self.dicionario_lista[self.saida])
                    except:
                        continue
        else:
            try:
                self.matricula_sorteio = int(self.matricula_sorteio)/10
                self.matricula_sorteio = int(self.matricula_sorteio)
                self.matricula_sorteio = str(self.matricula_sorteio)
            except:
                continue
            if self.matricula_sorteio=="0":
                self.matricula_sorteio=""
        if len(self.matricula_sorteio)==12:
            self.cor=(0,255,0)
        else:
            self.cor=(255,255,255)