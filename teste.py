import os

def main():
	arq = open('C:\\PROGRA~2\\CISCOS~1\\VPNCLI~1\\login.data', 'r')
	os.system('C:\\PROGRA~2\\CISCOS~1\\VPNCLI~1\\vpnclient.exe '+ arq.readline())

if __name__ == '__main__':
	main()