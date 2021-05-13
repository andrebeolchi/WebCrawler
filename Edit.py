import os

def ajustar():
    diret = os.listdir("/home/dante0x41/Desktop/challenge/Challenge_Fiap-master/txt/")
    for arqs in diret:
        arqOld = open("/home/dante0x41/Desktop/challenge/Challenge_Fiap-master/txt/"+ arqs , "r")
        arqLines = arqOld.readlines()
        for linhaSeparada in arqLines:
            linhaSeparada = linhaSeparada.strip()
            linhaNova = linhaSeparada.replace(" ", "")
            linhaNova = linhaNova.replace("::", ";")
            linhaNova = linhaNova.replace(":", ";")
            linhaNova = linhaNova.replace("||", ";")
            linhaNova = linhaNova.replace("|", ";")
            linhaNova = linhaNova.replace("//", ";")
            linhaNova = linhaNova.replace("/", ";")
            linhaNova = linhaNova.replace("--", ";")
            linhaNova = linhaNova.replace("-", ";")
            linhaNova = linhaNova.replace("++", ";")
            linhaNova = linhaNova.replace("+", ";")
            f = open("/home/dante0x41/Desktop/challenge/Challenge_Fiap-master/txt/senhas.txt", "a")
            f.write(linhaNova +'\n')
            f.close()
