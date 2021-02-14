import cv2
from os import sep
#Aqui será o unico lugar que irá usar 'os'
class carregar_imagens:
    def __init__(self, imagem):
        self.imagem = cv2.imread("imagens_funcionamento"+sep+imagem)
    
    def mostrar_imagem(self, tempo):
        cv2.imshow("Cranio",self.imagem)
        saida = cv2.waitKey(tempo)
        return saida