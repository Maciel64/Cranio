from random import randint
from os import sep
import sqlite3
import cv2
from tempo_operaçoes import operar
conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()
class segunda_parte():
	def __init__(self,matricula):
		self.matricula_sorteio=matricula
		self.parte_dois()

	def parte_dois(self):
		if self.matricula_sorteio=="123456789123":
			self.todas_imagens("imagem_informativa.png",0)
		elif self.matricula_sorteio=="":
			self.matricula_sorteio=0
		elif operar.aluno_existente(self.matricula_sorteio)==False:
			self.todas_imagens("error_matricula.png",10000)
		else:
			try:
				cursor.execute("SELECT nome,data_nascimento,turma,curso,pontos FROM alunos WHERE matricula = "+self.matricula_sorteio)
				self.dicionario_lista = cursor.fetchone()
				self.imagem_alunos()
				if operar.analisar_tempo(self.matricula_sorteio)==True:
					cursor.execute("SELECT turma FROM alunos WHERE matricula = "+self.matricula_sorteio)
					self.dicionario_lista = cursor.fetchone()
					if self.dicionario_lista[0]==1:
						self.dicionario_lista=randint(1,operar.quantidade_perguntas("SELECT id,pergunta,resposta,pontos FROM perguntas1ano"))
						cursor.execute("SELECT id,pergunta,resposta,pontos FROM perguntas1ano WHERE id = "+str(self.dicionario_lista))
					elif self.dicionario_lista[0]==2:
						self.dicionario_lista=randint(1,operar.quantidade_perguntas("SELECT id,pergunta,resposta,pontos FROM perguntas2ano"))
						cursor.execute("SELECT id,pergunta,resposta,pontos FROM perguntas2ano WHERE id = "+str(self.dicionario_lista))
					elif self.dicionario_lista[0]==3:
						self.dicionario_lista=randint(1,operar.quantidade_perguntas("SELECT id,pergunta,resposta,pontos FROM perguntas3ano"))
						cursor.execute("SELECT id,pergunta,resposta,pontos FROM perguntas3ano WHERE id = "+str(self.dicionario_lista))
					else:
						print("Error no aluno com matricula: ",self.dicionario_lista," o ano que está é ",self.dicionario_lista[3])
					try:
						self.dicionario_lista=cursor.fetchone()
						self.pergunta(self.dicionario_lista[1])
						if self.dicionario_lista[2]==1 and (self.saida==49 or self.saida==156):
							self.certa()
						elif self.dicionario_lista[2]==2 and (self.saida==50 or self.saida==153):
							self.certa()
						elif self.dicionario_lista[2]==3 and (self.saida==51 or self.saida==155):
							self.certa()
						elif self.dicionario_lista[2]==4 and (self.saida==52 or self.saida==150):
							self.certa()
						elif self.dicionario_lista[2]==5 and (self.saida==53 or self.saida==157):
							self.certa()
						else:
							self.todas_imagens("RError.png",10000)
					except:
						print("A pergunta ",self.dicionario_lista[1]," está com error")
				else:
					self.todas_imagens("tempo_insuficiente.png",10000)
			except:
				print("Error com alguma coisa no codigo")

	def certa(self):
		self.todas_imagens("RCerta.png",10000)
		operar.somar_pontos(self.dicionario_lista[3],self.matricula_sorteio)

	def girar(self,graus):
		(alt, lar) = self.imagem2.shape[:2]
		self.imagem2 = cv2.warpAffine(self.imagem2, cv2.getRotationMatrix2D((lar // 2, alt // 2), graus, 1.0), (lar, alt))

	def todas_imagens(self,nome,tempo):
		self.imagem=cv2.imread("imagens_funcionamento"+sep+nome)
		cv2.imshow("Cranio",self.imagem)
		cv2.waitKey(tempo)

	def pergunta(self,nome):
		contador = 0
		while contador<10:
			self.imagem=cv2.imread("imagens_perguntas"+sep+nome)
			self.imagem2=self.imagem[25:75,50:100]
			cv2.putText(self.imagem2,str(contador),(20,32), cv2.FONT_HERSHEY_SIMPLEX,1.2,(255,255,255),2,cv2.LINE_AA)
			self.girar(90)
			self.imagem[25:75,50:100]=self.imagem2
			cv2.imshow("Cranio",self.imagem)
			self.saida = cv2.waitKey(1000)
			contador+=1
			if self.saida!=-1:
				break
		operar.somar_tempo(self.matricula_sorteio)

	def imagem_alunos(self):
		dicionario=[523,619,685,755,820]
		imagem=cv2.imread("imagens_funcionamento"+sep+"Tela_alunos.png")
		contador=0
		for x in dicionario:
			self.imagem2=imagem[25:350,x:x+325]
			self.escrever_girar(contador)
			imagem[25:350,x:x+70]=self.imagem2[0:325,0:70]
			contador+=1
		cv2.imshow("Cranio",imagem)
		cv2.waitKey(0)

	def escrever_girar(self,x):
		dicionario=[""," anos"," ano",""," Pontos"]
		if self.dicionario_lista[4]==1:
			dicionario[4]=" Ponto"
		self.girar(-90)
		if x==1:	
			cv2.putText(self.imagem2,str(operar.idade(self.dicionario_lista[1]))+dicionario[x],(10,32), cv2.FONT_HERSHEY_SIMPLEX,1.2,(255,255,255),2,cv2.LINE_AA)
		else:
			cv2.putText(self.imagem2,str(self.dicionario_lista[x])+dicionario[x],(10,32), cv2.FONT_HERSHEY_SIMPLEX,1.2,(255,255,255),2,cv2.LINE_AA)
		self.girar(90)