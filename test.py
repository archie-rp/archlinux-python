#! /usr/bin/env python
#Includes
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
pasta=os.getcwd()
linha =  colored("#"*e, 'cyan')
sair = ""
i = 0
u = 0
erro = ""

#Funcoes

def ficheiro(nome):
	if not os.path.exists(nome):
		pass
	else:
		os.remove(nome)
	
def oss():
	uname = os.system('uname -a >> versao.txt')
	versao = open(pasta + '/' + 'versao.txt', 'r+')
	vt = versao.read()
	ficheiro('versao.txt')
	#print (vt) 
	lib32=" lib32-mesa-libgl lib32-alsa-plugins"
	sis = vt.find('x86_64')
	if sis != -1:
		print ('Sistema x86_64')
		instalar(lib32, 'pacman') 
	else:
		print ('Sistema x86')
	return (sis)

def butil(u):
	lista=("cat /etc/passwd | grep '/home' | cut -d: -f1")
	os.system(lista + " >> .users.txt")
	users = open(pasta + '/' + '.users.txt', 'r+')
	users = users.read()
	ficheiro('.users.txt')
	utilizadores= users.split('\n') 
	u=int(u)
	u=utilizadores[u]
	print (u)
	return u

def listusers():
	os.system("clear")
	print (linha)
	print(colored("Utilizadores", 'green' ))
	print (linha)
	lista=("cat /etc/passwd | grep '/home' | cut -d: -f1")
	os.system(lista + " >> .users.txt")
	#os.system("users >> .users.txt")
	users = open(pasta + '/' + '.users.txt', 'r+')
	users = users.read()
	ficheiro('.users.txt')
	utilizadores= users.split('\n') 
	print ('\nExistentes:')
	for u in range(len(utilizadores)):
		if utilizadores[u] == '':
			pass
		else:
			print (colored(u , 'yellow') ,utilizadores[u])

def instalar(x,y):
	os.system("clear")
	print (linha)
	print (colored("Instalar pacotes: ", 'cyan', attrs=['bold']))
	print (linha)
	print (colored("A installar :", 'green') + '"' + colored(x, 'blue') + '"')
	if y == 'pacman':
		#print ('Pacman')
		os.system('pacman -Syu --noconfirm ' + x )
	else:
		#print ('yaourt ')
		#print('yaourt ' + x )
		os.system('yaourt --noconfirm -S ' + x )

	#input("regista apps")
	pass

def yaourt():
	os.system("clear")
	print (linha)
	print(colored("Instalar yaourt ", 'green' ))
	print (linha)
	os.system(' cp /etc/pacman.conf pacman.conf')
	os.system(' cp /etc/sudoers sudoers')
	os.system(" sed -e 's/SigLevel\s\s\s/#SigLevel/' pacman.conf > pacman")
	os.system(" sed -e 's/#\s%wheel\sALL=(ALL)\sALL/%wheel ALL=(ALL) ALL/' sudoers > sudo")
	uname = os.system('uname -a >> versao.txt')
	versao = open(pasta + '/' + 'versao.txt', 'r+')
	vt = versao.read()
	ficheiro('versao.txt')
	sis = vt.find('x86_64')
	if sis != -1:
		os.system(" echo -e '\n[multilib]\nInclude = /etc/pacman.d/mirrorlist' >> pacman")
	os.system(" echo -e '\n[archlinuxfr]\nServer = http://repo.archlinux.fr/$arch' >> pacman")
	os.system(' mv pacman /etc/pacman.conf')
	os.system(' mv sudo /etc/sudoers')
	os.system(' pacman -Syu --noconfirm yaourt')
	pass

def servicos():
	os.system("clear")
	print (linha)
	print(colored("\nAdicionar Servicos", 'green'))
	print (linha)
	print (colored("A iniciar Serviços!", 'yellow', attrs=['bold']))
	os.system(' systemctl enable upower')
	os.system(' systemctl enable tlp')
	os.system(' systemctl enable smbd')
	os.system(' systemctl enable nmbd')
	os.system(' systemctl enable smbnetfs')
	os.system(' systemctl enable rpc-idmapd')
	os.system(' systemctl enable rpc-mountd')
	os.system(' systemctl enable systemd-readahead-collect')
	os.system(' systemctl enable systemd-readahead-replay')
	os.system(' echo -e "vboxdrv" >> /etc/modules-load.d/virtualbox.conf')
	input(colored("\nMenu principal ", 'green' )+ "<enter>")

#Funcoes globais
ficheiro('.users.txt')
ficheiro('.apps.txt')
ficheiro('versao.txt')

#Programa
print ("Menu")
menu = ["Utilizadores","GitHub","Drivers Intel e Synaptics","Apps","Limpar Apps"]
os.system("clear")
while sair != "x":
	text = colored('Arch Linux', 'blue', attrs=['reverse', 'blink'])
	print(text)
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
		print(linha)
		listusers()
		print (colored("Gestor de Utilizadores:", 'cyan', attrs=['bold']))
		print (colored('0' , 'yellow') ,'Adicionar Utilizador')
		print (colored('1' , 'yellow') ,'Remover Utilizador')
		print(linha)
		r = input('Selecionar:')
		if r=='0':
			os.system('clear')
			print (linha)
			print (colored("Adicionar Utilizador: ", 'cyan', attrs=['bold']))
			print (linha)
			utilizador=input('Nome:')
			os.system('sudo useradd -m -g users -G wheel,storage,video,audio,network -s /bin/bash ' + utilizador)
			print (colored("Password Utilizador: ", 'red', attrs=['bold']))
			os.system('\nsudo passwd ' + utilizador)
			input(colored("\nMenu principal ", 'green' )+ "<enter>")	
		elif r=='1':
			listusers()
			print (linha)
			print (colored("Remover Utilizador: ", 'red', attrs=['bold']))
			print (linha)
			rsp=input(colored('Número: ', 'green'))
			os.system('sudo userdel -r ' + butil(rsp))
		else:
			pass	
	elif rsp == "1":
		os.system("clear")
		print (linha)
		print (colored("GitHub: ", 'cyan', attrs=['bold']))
		print (linha)
		instalar('xclip git')		
		github_utilizador=input(colored('\nGitHub','yellow')+ colored('@', 'red') + 'Nome:')
		os.system('git config --global user.name ' + github_utilizador)
		github_email=input(colored('GitHub','yellow') + colored('@', 'red') +  'Email:')
		os.system('git config --global user.email ' + github_email )
		input(colored("\nMenu principal ", 'green' )+ "<enter>")
	elif rsp == "2":
		os.system("clear")
		dri=("xf86-input-synaptics xf86-input-mouse xf86-input-keyboard xf86-video-intel intel-dri libva-intel-driver")
		print (linha)
		print (colored("Drivers: ", 'cyan', attrs=['bold'])+ dri )
		print (linha)
		dr=input('Instalar Drivers?''\n(s/n)')
		if dr == 's':
			instalar(dri, 'pacman')
	elif rsp == "3":
		os.system("clear")
		print (linha)
		print (colored("Instalar Apps: ", 'cyan', attrs=['bold']))
		print (linha)
		if not os.path.exists('.apps.txt'):
			open('.apps.txt', 'w').close()
			pkgtoinstall='mpd mpc alsa-utils alsa-plugins \
xorg-server xorg-xinit xorg-server-utils xorg-twm \
xorg-xdpyinfo xorg-xdriinfo xorg-xev xorg-xgamma \
xorg-xinput xorg-xkbcomp xorg-xkbevd xorg-xkbutils \
xorg-xkill xorg-xlsatoms xorg-xlsclients xorg-xmessage \
xorg-xmodmap xorg-xpr xorg-xprop xorg-xsetroot xorg-xvinfo \
xorg-xrandr xorg-xrdb xorg-xrefresh xorg-xset xorg-xwd \
xorg-xwininfo xorg-xwud ttf-dejavu xterm zsh \
pcmanfm thunar lxappearance mirage file-roller udisks udisks2 \
polkit polkit-gnome gvfs gvfs-smb bash-completion udiskie chromium \
zip unrar tar autofs ntfs-3g thunar-archive-plugin thunar-volman pidgin \
skype curl git wget mplayer vlc ttf-liberation ttf-freefont lxappearance \
bc rsync mlocate bash-completion pkgstats ntfs-3g dosfstools exfat-utils fuse \
fuse-exfat openssh nfs-utils samba smbnetfs  gamin rxvt-unicode pcmanfm gvfs scrot \
thunar tumbler leafpad epdfview nitrogen ttf-bitstream-vera ttf-dejavu \
wicd wicd-gtk libmtp gvfs-mtp jdk7-openjdk icedtea-web-java7 htop \
chromium firefox transmission-gtk pidgin skype gst-plugins-base \
gst-plugins-base-libs gst-plugins-good gst-plugins-bad \
gst-plugins-ugly gst-libav vlc xbmc libbluray libquicktime \
weechat imap faenza-icon-theme ttf-dejavu tamsyn-font \
libdvdread libdvdnav libdvdcss virtualbox firefox'
			extra = ('mediterraneannight-theme compton-git adwaita-x-dark-and-light-theme gtk-theme-hope zukitwo-themes \
gtk-theme-elementary mate-icon-theme-faenza weeplugins-git nano-syntax-highlighting-git \
gnome-theme-adwaita qtconfiguration zsh-syntax-highlighting android-sdk android-apktool android-sdk-build-tools \
android-sdk-platform-tools android-udev eclipse-android sublime-text gtk-theme-numix-git tlp rssh')
			os.system('pacman -Q -q >> .apps.txt')
			apps = open(pasta + '/' + '.apps.txt', 'r+')
		pkg = apps.read()
		pkgtoinstall = pkgtoinstall.split()
		pkg = pkg.split('\n')
		extras = extra.split(' ') 
		#print (extras)
		#lib32 - bibliotecas 32 | apps - aplicaçoes instaladas
		#pkg - aplicaçoes para instalar !
		#dri - drivers | extra - nao funcionam
		lapps = ""
		if 'yaourt' in pkg:
			pass
		else:
			yaourt()
		for linhas in pkgtoinstall:
			sn=linhas in pkg	
			if sn == False:
				lapps = (lapps + " " + linhas)
		#lapps - aplicaçoes para instalar!
		instalar(lapps, 'pacman')
		for pacote in extras:
			instalar(pacote, 'yaourt')
		oss()
		input ('Aplicações instaladas !')
		servicos()
		os.system("clear")
		print(linha)
		print (colored("Todas as aplicações estão instaladas!", 'green', attrs=['bold', 'blink']))
		print (colored("Todos os serviços iniciados!", 'green', attrs=['bold', 'blink']))
		print(linha)
		ficheiro('.apps.txt')
		input(colored("\nMenu principal ", 'green' )+ "<enter>")
	elif rsp == "":
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
#pacman -Qe


#getcwd()
#Return a string representing the current working directory.

#listdir(path)
#Return a list containing the names of the entries in the directory given by path. The list is in arbitrary order. It does not include the special entries '.' and '..' even if they are present in the directory.

#mkdir(path[, mode])
#Create a directory named path with numeric mode mode. The default mode is 0777 (octal). On some systems, mode is ignored. Where it is used, the current umask value is first masked out. If the directory already exists, OSError is raised.
#remove(path) remover ficheiros
#os.removedirs('foo/bar/baz')
