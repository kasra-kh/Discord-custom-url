import clipboard
import time
from colorama import Fore, init
import os
init(convert=True)



intro = f"""{Fore.RED}

     ░█████╗░░█████╗░░░███╗░░██╗░░░██╗██████╗░██╗░░░░░
     ██╔══██╗██╔══██╗░████║░░██║░░░██║██╔══██╗██║░░░░░
     ██║░░██║██║░░██║██╔██║░░██║░░░██║██████╔╝██║░░░░░
     ██║░░██║██║░░██║╚═╝██║░░██║░░░██║██╔══██╗██║░░░░░
     ╚█████╔╝╚█████╔╝███████╗╚██████╔╝██║░░██║███████╗
     ░╚════╝░░╚════╝░╚══════╝░╚═════╝░╚═╝░░╚═╝╚══════╝

001 on top discord : ! 001#6666	 

{Fore.RESET}
                			           [{Fore.RED}>{Fore.WHITE}]{Fore.CYAN} 1:{Fore.RESET} shoro be kar
                			           [{Fore.RED}>{Fore.WHITE}]{Fore.CYAN} 2:{Fore.RESET} Discord khoshgel 001 :)
                			           [{Fore.RED}>{Fore.WHITE}]{Fore.CYAN} 3:{Fore.RESET} Restart =/


"""
cls = lambda: os.system('cls')

def discord(link):
    os.system('start ' + link)

def vanityurl():
	print(f'[{Fore.RED}>{Fore.RESET}] code invite serveret :', end=''); server = str(input('  :  '))
	if server == "exit" or server == "3" or server == "restart":
		cls()
		start()
	else:
		pass
	print(f'[{Fore.RED}>{Fore.RESET}] matni ke mikhay ', end=''); invite = str(input('  :  '))
	text = "discοrd.gg/" + invite + "||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||" + server
	clipboard.copy(text)
	print(f'[{Fore.RED}>{Fore.RESET}] {Fore.LIGHTGREEN_EX} ctrl + v bezan vase harki mikhay ba tag mire xDDDDDD')
	input()


def start():
	print(intro)
	print(f'[{Fore.RED}>{Fore.WHITE}] etekhabet :/', end=''); choice = str(input('  :  '))
	if choice == '1':
		vanityurl()
	elif choice == "2":
		discord("https://discord.gg/2TSp3GBa")
		cls()
		start()
	elif choice == "3":
		cls()
		start()
	else:
		print()
		print(f"[{Fore.RED}>{Fore.WHITE}] {Fore.RED}dadash ye chiz dorost bede kobs kesh ")
		time.sleep(1.5)
		cls()
		print(intro)
		print(f'[{Fore.RED}>{Fore.WHITE}] entekhabet :)', end=''); choice = str(input('  :  '))
		if choice == '1':
			vanityurl()		



if __name__ == '__main__':
	start()
       
