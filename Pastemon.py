import re
import requests
from bs4 import BeautifulSoup
import time
import threading
import os
import sys

mail = sys.argv[1]

dominio = "https://pastebin.com"
url_pastebin_archive = "https://pastebin.com/archive"
links = []
files = os.listdir('/home/dante0x41/Desktop/challenge/Challenge_Fiap-master/')
# Esta função faz requisições ao pastebin
def request_pastebin(url):
    try:
        page = requests.Session()

        page.proxies = {'http': 'socks5://127.0.0.1:9050', 'https': 'socks5://127.0.0.1:9050'} #Nessa linha utilizamos a rede tor para nao sermos identificados e consequentemente banidos
        req = page.get(url, timeout=6)
        if req.status_code == 200:
            return req.text
        else:
            os.system('sudo service tor restart')
    except Exception as e:
        os.system('sudo service tor restart')

    
# Essa função "traduz" os dados retornados da função acima para um tipo de dados que possamos manipular
def parsing(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        return soup
    except Exception as e:
        print("Erro ao fazer parsing do html", e)

# Essa função procura por todos os links na página do pastebin
def return_links(soup):
    try:
        cards_pai = soup.find("div", class_="archive-table")
        cards = cards_pai.find_all("a")
        for card in cards:
            link = card["href"]
            links.append(link)
        return links
    except Exception as e:
        print("Erro ao encontrar links", e)


#essa função aplica uma expressão regular para encontrar determinado dado
def search_name(data, mail):
    try:
        mail = mail.replace(".", "\.")
        regexp = "([a-zA-Z0-9.-]+"+mail+".[\s]?[a-zA-Z0-9_-]+)"
        regexado = re.findall(r"{}".format(regexp),data)
        return regexado
    except Exception:
        pass


def thread1ng(mail):
    global files
    first_link = links.pop(0)
    req_link = request_pastebin(dominio + "/raw" + first_link)

    search = search_name(req_link, mail)
    
    if search and not (first_link.replace("/", "") in files):

        with open('txt/' + first_link.replace("/", "") ,"w+") as f:
            arq = f.write(req_link)
            
            return req_link
    else:
        pass

        

def main_paste(mail):
    
    print("\033[1;32m╔═══════════════════════════════════════════════════════════╗")
    print("\033[1;32m║  \033[1;33m Iniciando monitoramento do Pastebin em segundo plano    \033[1;32m║")
    print("\033[1;32m╠═══════════════════════════════════════════════════════════╣")
    while True:
        html = request_pastebin(url_pastebin_archive)
            
        if html:
            soup = parsing(html)
            if soup:
                linked = return_links(soup)
                #print(linked)
                            
                if linked:
                                    
                        thread1ng(mail)