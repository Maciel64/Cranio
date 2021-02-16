import cv2
from os import sep
#Aqui será o unico lugar que irá usar 'os'
class carregar_imagens:
    def __init__(self, imagem):
        self.imagem = cv2.imread("imagens_funcionamento"+sep+imagem)
        #Aqui ele fará a leitura da iamgem, coloquei para trabalhar com self pelo motivo que será reusado
        self.imagem2 = self.imagem[15:465,850:1300]
    
    def mostrar_imagem(self, tempo):
        cv2.imshow("Cranio",self.imagem)
        #Aqui demostra a imagem
        saida = cv2.waitKey(tempo)
        #Aqui irá recolher a chave apertada pelo usuario
        return saida
        #Retorna uma string
    
    def girar(self,graus):
		(alt,lar) = self.imagem2.shape[:2]
		self.imagem2 = cv2.warpAffine(self.imagem2, cv2.getRotationMatrix2D((lar // 2, alt // 2), graus, 1.0), (lar, alt))
    
    def tela_cheia(self):
		cv2.namedWindow("Cranio", cv2.WINDOW_NORMAL)
		cv2.setWindowProperty("Cranio", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    
    def girar_escrever(self,matricula,cor):
		self.girar(-90)
		cv2.putText(self.imagem2,matricula,(40,32), cv2.FONT_HERSHEY_SIMPLEX,1.2,cor,2,cv2.LINE_AA)
		self.girar(90)
        self.imagem[15:465,850:900]=self.imagem2[0:450,0:50]