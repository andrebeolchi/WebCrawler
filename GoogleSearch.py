import requests
import json
from bs4 import BeautifulSoup
import re
import sys


def google_search(domain): 
    print("\033[1;32m╠═══════════════════════════════════════════════════════════╣")
    print("\033[1;32m║                 \033[1;33mIniciando busca no Google!                \033[1;32m║")
    print("\033[1;32m╠═══════════════════════════════════════════════════════════╣")

    try:
        paste_links = []
        txt = """site:pastebin.com intext:"""+domain

        #print(txt)
        search_google = requests.get("https://www.googleapis.com/customsearch/v1?key=AIzaSyCl9gJy-9vUONp8mPcSJJM7oBrsrYLn_8Y&cx=014606014560221332141:nsi5zalizas&q="+txt, timeout=6)
        json_data = json.loads(search_google.text)
        list_links = json_data.get("items")
        cont = 0
        for link in list_links:
            paste_links.append(list_links[cont].get("link"))
            if cont == 15:
                break
            else:
                cont += 1
        #print(paste_links)
        return paste_links
    except Exception as e:
        print("google search error", e)

def request_pastebin_links(list_pastebin_links, mail):
    for link in list_pastebin_links:
        requested_link = requests.get(link)

        search_emails(requested_link.text, mail)
    return True
def parsing_pastebin_links(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        return soup
    except Exception as e:
        print("Erro ao fazer parsing do html pastebin", e)

def search_emails(data_for_emails, mail):
    try:
        mail = mail.replace(".", "\.")
        regexp = "([a-zA-Z0-9.-]+"+mail+".[\s]?[a-zA-Z0-9_-]+)"
        regexado = re.findall(r"{}".format(regexp),data_for_emails)
        if regexado:
            print("\033[1;32m╠═══════════════════════════════════════════════════════════╣")
            print("\033[1;32m║                \033[1;33m Credenciais encontradas                   \033[1;32m║")
            print("\033[1;32m╠═══════════════════════════════════════════════════════════╣")  
            for regex in regexado:
                f = open('/home/dante0x41/Desktop/challenge/Challenge_Fiap-master/txt/google.txt', 'a')
                f.write(regex+"\r\n")
                f.close
        return regexado
    except Exception as e:
        print("erro no regex",e)


def google(mail):
    
    googled = google_search(mail)
    if googled:
        request_pastebin_links(googled, mail)   