def salvaConfig(info):
	arq = open('login.data', 'w')
	arq.write(info)
	arq.close()

info = input()
salvaConfig(info)