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
		print (rsp)
	elif rsp == "1":
		print (rsp)
	elif rsp == "2":
		print (rsp)
	elif rsp == "3":
		print (rsp)
	else:
		erro = colored('Opção não válida', 'red', attrs=['bold'])
	os.system("clear")
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
