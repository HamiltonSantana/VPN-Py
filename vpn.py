from tkinter import *
from tkinter import ttk
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

		self.style = ttk.Style()
		self.style.theme_use('winnative')

		def conecta():
			content = self.combo.get()
			print(content)
			if 'Cisco AnyConnect' == content:
				try:
					print('começa Try Cisco AnnyConnect')
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
			if 'VPN Client' == content:
				try:
					print('comeca try VPN Cliet')
					os.system('C:\\PROGRA~2\\CISCOS~1\\VPNCLI~1\\vpnclient.exe -s < login.data')
				except:
					os.system('taskkill /f /im vpncli')
					try:
						arq = open('login.data', 'w')
						arq.write("connect DISCOVERY\n")
						arq.write(en_1.get())
						arq.write("\n"+en_2.get())
						arq.close()
						arq.open('login.data', 'r')
						os.system('echo C:\\PROGRA~2\\CISCOS~1\\VPNCLI~1\\vpnclient.exe '+arq.readline())
						self.confirm()
					except:
						print('Falha ao salvar o arquivo de dados da VPN')

		self.parent.title("Conecta")
		self.pack(fill= BOTH, expand=True)

		frameTitle = Frame(self)
		frameTitle.pack(fill=X)

		#bitmap = BitmapImage(file="bitmap.xbm")
		#bitmap = BitmapImage(file="bitmap.xbm", foreground="black", background="red")

		#lb_logo = Label(frameTitle, image=bitmap)
		#lb_logo.pack(side=LEFT)
		"""
		cv_logo = Canvas(frameTitle, width=20, height=20)
		cv_logo.pack(side=LEFT)

		cv_logo.create_rectangle(0,0,20,20, fill="black")
		"""
		lb_title = Label(frameTitle, text= "Discovery")
		lb_title.pack(side=LEFT)
		
		frame1 = Frame(self)
		frame1.pack(fill=X)

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

		self.combo = ttk.Combobox(frame3, values=["Cisco AnyConnect", "VPN Client"])
		self.combo.pack(side=RIGHT, padx= 5, pady= 5)
		"""
		button = Button(frame3, text='OK')
		button['command'] = self.change_style
		button.pack(side=RIGHT, padx=5, pady=5)
		"""
		frame4 = Frame(self)
		frame4.pack(fill=X)

		info = en_1.get()

		but_1 = Button(frame4, text="Cancelar",width =10, command= self.parent.destroy)
		but_2 = Button(frame4, text="Conecta",width =10, command= conecta)

		but_1.pack(side=RIGHT, padx=5, pady=3)
		but_2.pack(side=RIGHT, padx=5, pady=3)

	def change_style(self, event=None):
		content = self.combo.get()
		try:
			self.style.theme_use(content)
		except tkinter.TclError as err:
			messagebox.showerror('Error', err)

def main():

	root = Tk()
	root.geometry("300x150")
	app = Example(root)
	root.mainloop()

if __name__ == '__main__':
	main()