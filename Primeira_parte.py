import cv2
from os import sep
from Segunda_parte import segunda_parte
class jogo():
	def __init__(self):
		while True:
			self.matricula_sorteio=""
			self.cor=(255,255,255)
			self.dicionario_lista={158:0,156:1,153:2,155:3,150:4,157:5,152:6,149:7,151:8,154:9,8:12345}
			self.recolher_matricula()
			if self.saida==-1:
				break
			segunda_parte(self.matricula_sorteio)

	def recolher_matricula(self):
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

	def imagem_pricipal(self):
		self.imagem=cv2.imread("imagens_funcionamento"+sep+"cranio.png")
		self.imagem2=self.imagem[15:465,850:1300]
		self.girar_escrever()
		self.imagem[15:465,850:900]=self.imagem2[0:450,0:50]
		#self.tela_cheia()
		cv2.imshow("Cranio",self.imagem)
		self.saida = cv2.waitKey(0)

	def girar(self,graus):
		(alt,lar) = self.imagem2.shape[:2]
		self.imagem2 = cv2.warpAffine(self.imagem2, cv2.getRotationMatrix2D((lar // 2, alt // 2), graus, 1.0), (lar, alt))

	def tela_cheia(self):
		cv2.namedWindow("Cranio", cv2.WINDOW_NORMAL)
		cv2.setWindowProperty("Cranio", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

	def girar_escrever(self):
		self.girar(-90)
		cv2.putText(self.imagem2,self.matricula_sorteio,(40,32), cv2.FONT_HERSHEY_SIMPLEX,1.2,self.cor,2,cv2.LINE_AA)
		self.girar(90)