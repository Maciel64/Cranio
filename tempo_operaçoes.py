import datetime
import sqlite3
conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()
class operar:
	def quantidade_perguntas(texto_numero):
		cursor.execute(texto_numero)
		texto_numero=0
		for x in cursor.fetchall():
			texto_numero+=1
		return texto_numero

	def somar_pontos(pontos,matricula_sorteio):
		cursor.execute("SELECT pontos FROM alunos WHERE matricula = "+str(matricula_sorteio))
		dicionario_lista=cursor.fetchone()
		dicionario_lista=dicionario_lista[0]
		pontos=dicionario_lista+pontos
		cursor.execute("UPDATE alunos SET pontos = ? WHERE matricula = ?" ,(pontos,matricula_sorteio))
		conexao.commit()

	def somar_tempo(matricula_sorteio):
		cursor.execute("UPDATE alunos SET tempo=? WHERE matricula = ?",(datetime.datetime.now(),matricula_sorteio))
		conexao.commit()

	def analisar_tempo(matricula_sorteio):
		cursor.execute("SELECT tempo FROM alunos WHERE matricula = "+matricula_sorteio)
		dicionario_lista=cursor.fetchone()
		dicionario_lista=dicionario_lista[0]
		dicionario_lista=datetime.datetime(int(str(dicionario_lista[0:4])),int(str(dicionario_lista[5:7])),int(str(dicionario_lista[8:10])),int(str(dicionario_lista[11:13])),int(str(dicionario_lista[14:16])),int(str(dicionario_lista[17:19])))
		tempo=datetime.datetime.now()
		if datetime.date(dicionario_lista.year,dicionario_lista.month,dicionario_lista.day)==datetime.date.today():
			return False
		elif datetime.date.fromordinal(datetime.date(dicionario_lista.year,dicionario_lista.month,dicionario_lista.day).toordinal()+1)==datetime.date.today():
			if dicionario_lista.hour>=tempo.hour:
				if dicionario_lista.minute>=tempo.minute:
					return False
			else:
				return True
		else:
			return True

	def aluno_existente(matricula_sorteio):
		cursor.execute("SELECT matricula FROM alunos")
		existente = False
		for x in cursor.fetchall():
			if int(matricula_sorteio)==x[0]:
				existente = True
				break
		return existente

	def idade(nascimento):
		tempo=datetime.date.today()
		nascimento=datetime.date(int(str(nascimento[6:10])),int(str(nascimento[3:5])),int(str(nascimento[0:2])))
		if nascimento.month>=tempo.month and nascimento.day>=tempo.day:
			nascimento=tempo.year-nascimento.year
		else:
			nascimento=(tempo.year-nascimento.year)-1
		return nascimento