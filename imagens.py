import cv2
from os import sep
#Aqui será o unico lugar que irá usar 'os'
class carregar_imagens:
    def __init__(self, imagem):
        self.imagem = cv2.imread("imagens_funcionamento"+sep+imagem)
        #Aqui ele fará a leitura da iamgem, coloquei para trabalhar com self pelo motivo que será reusado
    
    def mostrar_imagem(self, tempo):
        cv2.imshow("Cranio",self.imagem)
        #Aqui demostra a imagem
        saida = cv2.waitKey(tempo)
        #Aqui irá recolher a chave apertada pelo usuario
        return saida
        #Retorna uma string