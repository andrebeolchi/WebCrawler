from Pastemon import *
from Twitter import *
from Callwndb import *
from GoogleSearch import *
from Validate import *
from Start import *
from Edit import *
from Validate import *
from Calldir import *
from Makecsv import *
from Telebot import *
import time
import threading

if __name__ == "__main__":
    
    if len(sys.argv) == 2:
        
        mail = sys.argv[1]
        start()
        time.sleep(1)
        thread_1 = threading.Thread(target=main_paste, args=(mail,))
        thread_1.start()
        time.sleep(1)
        search_tw(mail)
        callpwn(mail)
        google(mail)
        
        ajustar()
        send_message('senhas.txt')
        time.sleep(30)
        validar()
        export_csv('creds.txt', 'cred_valida.csv')
        export_csv('senhas.txt', 'cred_encontrada.csv')
        send_message('creds.txt')
        
    elif len(sys.argv) == 4:
        brute = sys.argv[2]
        dom = sys.argv[3]
        start()
        time.sleep(1)
        thread_1 = threading.Thread(target=main_paste, args=(mail,))
        thread_1.start()
        time.sleep(1)
        search_tw(mail)
        callpwn(mail)
        google(mail)
        ajustar()
        send_message('senhas.txt')
        calldir(dom)
        validar()
        export_csv('creds.txt', 'credenciais_validas.csv')
        export_csv('senhas.txt', 'cred_encontrada.csv')
        send_message('creds.txt')
        
    else:
        print("Agumentos invalidos")