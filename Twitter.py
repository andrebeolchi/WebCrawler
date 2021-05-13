import tweepy
import re
import time
def search_tw(mail):
    print("\033[1;32m╠═══════════════════════════════════════════════════════════╣")
    print("\033[1;32m║                \033[1;33mInicando busca no Twitter!                 \033[1;32m║")
    print("\033[1;32m╠═══════════════════════════════════════════════════════════╣")

    time.sleep(2)
    try:
        with open('twitter-tokes.txt') as tfile:
            consumer_key = tfile.readline().strip('\n')
            consumer_secret = tfile.readline().strip('\n')
            access_token_secret = tfile.readline().strip('\n')
            access_token = tfile.readline().strip('\n')

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)

        word = mail

        tweets = tweepy.Cursor(api.search,
                                q=word,
                                ).items(1000)
        for tweet in tweets:

            mails = re.findall(r"([a-zA-Z0-9.-]+@globo\.com.[\s]?[a-zA-Z0-9_-]+)",tweet)
            if mails:
                with open('txt/twitter_mains.txt', "a+") as file:
                    file.write(mails)
            else:
                pass
        
    except Exception:
        print("\033[31;1m╠═══════════════════════════════════════════════════════════╣")
        print("\033[31;1m║             \033[1;33mNenhum dado encontrado no Twitter!            \033[31;1m║")
        print("\033[31;1m╠═══════════════════════════════════════════════════════════╣")
    return 0
