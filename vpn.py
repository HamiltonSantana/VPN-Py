from tkinter import *
import os

class Example(Frame):

	def __init__(self, parent): 		# Funcao que definia incializacao e chama a inicilizacao da interface
		Frame.__init__(self, parent)

		self.parent = parent
		self.initUI()

	def confirm(self):
		rt = Tk()
		rt.title("Confirmacao")
		frameMsg = Frame(rt)
		frameMsg.pack()

		lb_conf = Label(frameMsg, text="Configuração Salva")
		but_ok = Button(frameMsg, text="OK !", width=10, command= rt.destroy)

		lb_conf.pack()
		but_ok.pack(pady=5)
		rt.geometry("200x100")

		rt.mainloop()

	def initUI(self):			# Funcao que define a inicializacao da interface

		def conecta():
			try:
				os.system('C:\\PROGRA~2\\Cisco\\CISCOA~2\\vpncli.exe -s < login.data')
			except:
				os.system('taskkill /f /im vpncli')
				try:
					arq = open('login.data', 'w')
					arq.write("connect vpntef01.linx.com.br\n")
					arq.write(en_1.get())
					arq.write("\n"+en_2.get())
					arq.close()
					os.system('C:\\PROGRA~2\\Cisco\\CISCOA~2\\vpncli.exe -s < login.data')
					self.confirm()
				except:
					print('Falha ao salvar o arquivo de dados da VPN')

		self.parent.title("Conecta")
		self.pack(fill= BOTH, expand=True)

		frame1 = Frame(self)
		frame1.pack(fill=X)

		lb_title = Label(frame1, text= "Discovery")
		lb_title.pack()

		lb_1 = Label(frame1, text="Usuario", width=6)
		lb_1.pack(side= LEFT, padx=5, pady=5)

		en_1 = Entry(frame1)
		en_1.pack(fill=X, padx=5, expand=True)

		frame2= Frame(self)
		frame2.pack(fill=X)

		lb_2 = Label(frame2, text="Senha", width=6)
		lb_2.pack(side= LEFT, padx=5, pady=5)

		en_2 = Entry(frame2)
		en_2.pack(fill=X, padx=5, expand=True)

		frame3 = Frame(self)
		frame3.pack(fill=X)

		info = en_1.get()

		but_1 = Button(frame3, text="Cancelar",width =10, command= self.parent.destroy)
		but_2 = Button(frame3, text="Conecta",width =10, command= conecta)

		but_1.pack(side=RIGHT, padx=5, pady=5)
		but_2.pack(side=RIGHT, padx=5, pady=5,)

def main():

	root = Tk()
	root.geometry("300x150")
	app = Example(root)
	root.mainloop()

if __name__ == '__main__':
	main()