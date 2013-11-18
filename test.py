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
#Funcoes

def instalar(x):
	os.system("clear")
	print (linha)
	print (colored("Instalar pacotes: ", 'cyan', attrs=['bold']))
	print (linha)
	print ("A installar ..", x)
	os.system('sudo yaourt -S --noconfirm ' + x)
	#input(colored("\nMenu principal ", 'green' )+ "<enter>")
	pass
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
		instalar('xclip git')		
		github_utilizador=input(colored('\nGitHub','yellow')+ colored('@', 'red') + 'Nome:')
		print ('git config --global user.name', github_utilizador)
		github_email=input(colored('GitHub','yellow') + colored('@', 'red') +  'Email:')
		print ('git config --global user.email', github_email )
		input(colored("\nMenu principal ", 'green' )+ "<enter>")
	elif rsp == "2":
		#instalar('')
		os.system("clear")
		print (linha)
		print (colored("Instalar Apps: ", 'cyan', attrs=['bold']))
		print (linha)
		pasta=os.getcwd()
		if not os.path.exists('.apps.txt'):
			open('.apps.txt', 'w').close()
			pkgtoinstall=('mpd mpc xf86-input-synaptics alsa-utils alsa-plugins \
 			xorg-server xorg-xinit xorg-server-utils xorg-twm xorg-xdpyinfo xorg-xdriinfo xorg-xev xorg-xgamma \
 			xorg-xinput xorg-xkbcomp xorg-xkbevd xorg-xkbutils \
 			xorg-xkill xorg-xlsatoms xorg-xlsclients xorg-xmessage \
			xorg-xmodmap xorg-xpr xorg-xprop xorg-xsetroot xorg-xvinfo \
			xorg-xrandr xorg-xrdb xorg-xrefresh xorg-xset xorg-xwd \
            xorg-xwininfo xorg-xwud ttf-dejavu xterm zsh pcmanfm thunar lxappearance \
 			mirage file-roller udisks udisks2 polkit polkit-gnome gvfs \
 			gvfs-smb bash-completion udiskie chromium zip unrar tar autofs \
 			ntfs-3g thunar-archive-plugin thunar-volman pidgin skype curl \
 			git wget mplayer vlc ttf-liberation ttf-freefont lxappearance \
 			bc rsync mlocate bash-completion pkgstats lib32-alsa-plugins \
 			ntfs-3g dosfstools exfat-utils fuse fuse-exfat openssh rssh \
 			nfs-utils samba smbnetfs tlp xf86-input-mouse xf86-input-keyboard \
 			gamin xf86-video-intel intel-dri libva-intel-driver lib32-mesa-libgl \
 			gtk-theme-numix-git rxvt-unicode pcmanfm gvfs scrot thunar tumbler \
 			leafpad epdfview nitrogen ttf-bitstream-vera ttf-dejavu \
 			wicd wicd-gtk android-sdk android-apktool android-sdk-build-tools \
 			android-sdk-platform-tools android-udev eclipse-android libmtp\
 			gvfs-mtp jdk7-openjdk icedtea-web-java7 sublime-text htop \
 			chromium transmission-gtk pidgin skype gst-plugins-base \
 			gst-plugins-base-libs gst-plugins-good gst-plugins-bad \
 			gst-plugins-ugly gst-libav vlc xbmc libbluray libquicktime \
 			libdvdread libdvdnav libdvdcss cdrdao')
			os.system('pacman -Q -q >> .apps.txt')
		apps = open(pasta + '/' + '.apps.txt', 'r+')
		pkg = apps.read()
		pkgtoinstall = pkgtoinstall.split()
		pkg = pkg.split('\n') 
		instpkg=len(pkgtoinstall)
		inst = []
		for linha in pkgtoinstall:
			sn=linha in pkg	
			if sn == False:
				inst.append(linha) 
		print (colored("Todas as aplicações estão instaladas!", 'green', attrs=['bold', 'blink']))
		os.remove('.apps.txt')

		input(colored("\nMenu principal ", 'green' )+ "<enter>")
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
#pacman -Qe


#getcwd()
#Return a string representing the current working directory.

#listdir(path)
#Return a list containing the names of the entries in the directory given by path. The list is in arbitrary order. It does not include the special entries '.' and '..' even if they are present in the directory.

#mkdir(path[, mode])
#Create a directory named path with numeric mode mode. The default mode is 0777 (octal). On some systems, mode is ignored. Where it is used, the current umask value is first masked out. If the directory already exists, OSError is raised.
#remove(path) remover ficheiros
#os.removedirs('foo/bar/baz')
