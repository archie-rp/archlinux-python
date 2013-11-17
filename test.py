#! /usr/bin/env python
#Includes

import subprocess
from subprocess import call
import os
import sys
from termcolor import colored, cprint


#Program
#Escrever INFO
os.system("clear")
hostname = os.uname()[1]
username = os.getlogin()
name = ' Feito por ' + username + ' '
host = ' Maquina : ' + hostname + ' '
n =len(name)
h =len(host) 
if n > h :
	e = n
else:
	e = h


# Variaveis
global m_Home
m_Home = '/home/' + os.getlogin()

#Programa
print ("Menu")
menu = ["AddUser","GitHub","Apps","Limpar Apps"]
sair = ""
i = 0
erro = ""
os.system("clear")
while sair != "x":
	text = colored('Arch Linux', 'blue', attrs=['reverse', 'blink'])
	print(text)
	linha =  colored("#"*e, 'cyan')
	print (linha)
	print (name)
	print (host)
	print (linha)
	print (colored("Menu:", 'cyan', attrs=['bold']))
	for i in range(len(menu)):
		print (colored(i , 'yellow') ,menu[i])
	print ("\nx) Sair")
	i = (i + 1)
	print (erro)
	rsp=input(colored('Opção: ', 'green'))
	if rsp == "x":
		sair = "x"
	elif rsp == "0":
		os.system("clear")
		print (linha)
		print (colored("AddUser: ", 'cyan', attrs=['bold']))
		print (linha)
		utilizador=input('Nome:')
		print('\nuseradd -m -g users -G wheel,storage,video,audio,network -s /bin/bash', utilizador)
		input(colored("\nMenu principal ", 'green' )+ "<enter>")
	elif rsp == "1":
		os.system("clear")
		print (linha)
		print (colored("GitHub: ", 'cyan', attrs=['bold']))
		print (linha)
		print ('Instalar Git e xclip ...')
		print('\nsudo pacman -S git xclip')
		github_utilizador=input(colored('\nGitHub','yellow')+ colored('@', 'red') + 'Nome:')
		print ('git config --global user.name', github_utilizador)
		github_email=input(colored('GitHub','yellow') + colored('@', 'red') +  'Email:')
		print ('git config --global user.email', github_email )
		input(colored("\nMenu principal ", 'green' )+ "<enter>")
	elif rsp == "2":
		print (rsp)
	elif rsp == "3":
		os.system("clear")
		print (linha)
		print (colored("Limpar Apps: ", 'cyan', attrs=['bold']))
		print (linha)
		print('\nsudo pacman -Rsc --noconfirm $(pacman -Qqdt)')
		os.system('sudo pacman -Rsc --noconfirm $(pacman -Qqdt)')
		input(colored("\nMenu principal ", 'green' )+ "<enter>")
	else:
		erro = colored('Opção não válida', 'red', attrs=['bold'])
	os.system("clear")



#chdir(path)
#Change the current working directory to path.

#getcwd()
#Return a string representing the current working directory.

#listdir(path)
#Return a list containing the names of the entries in the directory given by path. The list is in arbitrary order. It does not include the special entries '.' and '..' even if they are present in the directory.

#mkdir(path[, mode])
#Create a directory named path with numeric mode mode. The default mode is 0777 (octal). On some systems, mode is ignored. Where it is used, the current umask value is first masked out. If the directory already exists, OSError is raised.
#remove(path) remover ficheiros
#os.removedirs('foo/bar/baz')
#shell = input('\n' + username + '@' + hostname + ':' + cwd + '> ')
#print 
#username = input("Username: ")
#print (username)
#print ("#"*(31-7))
#print ("SHELL\n")
#import os
#cmd = 'ls -al'
#os.system(cmd)
#popen
#f = os.popen('date')
#now = f.read()
#print ("Today is ", now)

#Subprocess
#import subprocess
#subprocess.call("command1")
#subprocess.call(["command1", "arg1", "arg2"])

#Output
#import subprocess
#p = subprocess.Popen("ls /", stdout=subprocess.PIPE, shell=True)
#(output, err) = p.communicate()
#print ("OUTPUT:\n", output)

#print line 
#import subprocess
#p = subprocess.Popen(["ls", "-l", "/"], stdout=subprocess.PIPE, shell=False)
#output, err = p.communicate()
#print ("*** Running ls -l command ***\n", output)
