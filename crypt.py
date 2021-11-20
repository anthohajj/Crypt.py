import colorama
from colorama import Fore
from colorama import Style

colorama.init()
print(Fore.RED + Style.BRIGHT + """
▄▄▄ . ▐ ▄  ▄▄· ▄▄▄   ▄· ▄▌ ▄▄▄·▄▄▄▄▄▪         ▐ ▄    ▄▄▄·  ▐ ▄ ·▄▄▄▄    ·▄▄▄▄  ▄▄▄ . ▄▄· ▄▄▄   ▄· ▄▌ ▄▄▄·▄▄▄▄▄▪         ▐ ▄   ▄▄▄▄▄            ▄▄▌  
▀▄.▀·•█▌▐█▐█ ▌▪▀▄ █·▐█▪██▌▐█ ▄█•██  ██  ▄█▀▄ •█▌▐█  ▐█ ▀█ •█▌▐███· ██   ██· ██ ▀▄.▀·▐█ ▌▪▀▄ █·▐█▪██▌▐█ ▄█•██  ██  ▄█▀▄ •█▌▐█  •██   ▄█▀▄  ▄█▀▄ ██•  
▐▀▀▪▄▐█▐▐▌██ ▄▄▐▀▀▄ ▐█▌▐█▪ ██▀· ▐█.▪▐█·▐█▌.▐▌▐█▐▐▌  ▄█▀▀█ ▐█▐▐▌▐█▪ ▐█▌  ▐█▪ ▐█▌▐▀▀▪▄██ ▄▄▐▀▀▄ ▐█▌▐█▪ ██▀· ▐█.▪▐█·▐█▌.▐▌▐█▐▐▌   ▐█.▪▐█▌.▐▌▐█▌.▐▌██ ▪ 
▐█▄▄▌██▐█▌▐███▌▐█•█▌ ▐█▀·.▐█▪·• ▐█▌·▐█▌▐█▌.▐▌██▐█▌  ▐█▪ ▐▌██▐█▌██. ██   ██. ██ ▐█▄▄▌▐███▌▐█•█▌ ▐█▀·.▐█▪·• ▐█▌·▐█▌▐█▌.▐▌██▐█▌   ▐█▌·▐█▌.▐▌▐█▌.▐▌▐█▌ ▄
 ▀▀▀ ▀▀ █▪·▀▀▀ .▀  ▀  ▀ • .▀    ▀▀▀ ▀▀▀ ▀█▄▀▪▀▀ █▪   ▀  ▀ ▀▀ █▪▀▀▀▀▀•   ▀▀▀▀▀•  ▀▀▀ ·▀▀▀ .▀  ▀  ▀ • .▀    ▀▀▀ ▀▀▀ ▀█▄▀▪▀▀ █▪   ▀▀▀  ▀█▄▀▪ ▀█▄▀▪.▀▀▀ 
 """ + Style.RESET_ALL)
print(Fore.RED + Style.BRIGHT + """
    _/_/_/    _/      _/        _/_/    _/      _/  _/_/_/_/_/  _/    _/    _/_/    _/      _/  _/      _/      _/_/_/_/  _/            _/    _/    _/_/          _/        _/   
   _/    _/    _/  _/        _/    _/  _/_/    _/      _/      _/    _/  _/    _/  _/_/    _/    _/  _/        _/        _/            _/    _/  _/    _/        _/        _/    
  _/_/_/        _/          _/_/_/_/  _/  _/  _/      _/      _/_/_/_/  _/    _/  _/  _/  _/      _/          _/_/_/    _/            _/_/_/_/  _/_/_/_/        _/        _/     
 _/    _/      _/          _/    _/  _/    _/_/      _/      _/    _/  _/    _/  _/    _/_/      _/          _/        _/            _/    _/  _/    _/  _/    _/  _/    _/      
_/_/_/        _/          _/    _/  _/      _/      _/      _/    _/    _/_/    _/      _/      _/          _/_/_/_/  _/_/_/_/      _/    _/  _/    _/    _/_/      _/_/         
                                                                                                                                                                                 
                                                                                                                                                                                 
""" + Style.RESET_ALL)


from hashlib import sha256
entree = input(print(Fore.GREEN + Style.BRIGHT + "Enter the name of the file to encrypt / decrypt : " + Style.RESET_ALL))
sortie = input(print(Fore.BLUE + Style.BRIGHT + "Enter the name of the final file : " + Style.RESET_ALL))
key = input(print(Fore.YELLOW+ Style.BRIGHT + "Enter the key : " + Style.RESET_ALL))
keys = sha256(key.encode('utf-8')).digest()
with open(entree,'rb') as f_entree:
	with open(sortie,'wb') as f_sortie:
	   i=0
	   while f_entree.peek():
		   c = ord(f_entree.read(1))
		   j = i % len(keys)
		   b = bytes ([c^keys[j]])
		   f_sortie.write(b)
		   i = i + 1

