import os

def callpwn(mail):
    print("\033[1;32m╠═══════════════════════════════════════════════════════════╣")    
    print("\033[1;32m║              \033[1;33m  Iniciando busca na rede TOR!               \033[1;32m║")
    print("\033[1;32m╠═══════════════════════════════════════════════════════════╣") 
   
    os.system('python3 pwndb.py --target '+mail+' --output txt > txt/pwndb.txt')
