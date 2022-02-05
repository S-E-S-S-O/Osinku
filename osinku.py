# coding: utf-8
from sesso.colors import *; import sys; import time; import requests
import json    

with open("config.json", "r") as sesso:
    oscur0 = json.load(sesso)

logo = """%s

     ▄██████▄     ▄████████  ▄█  ███▄▄▄▄      ▄█   ▄█▄ ███    █▄  
    ███    ███   ███    ███ ███  ███▀▀▀██▄   ███ ▄███▀ ███    ███ 
    ███    ███   ███    █▀  ███▌ ███   ███   ███▐██▀   ███    ███ 
    ███    ███   ███        ███▌ ███   ███  ▄█████▀    ███    ███ 
    ███    ███ ▀███████████ ███▌ ███   ███ ▀▀█████▄    ███    ███ 
    ███    ███          ███ ███  ███   ███   ███▐██▄   ███    ███ 
    ███    ███    ▄█    ███ ███  ███   ███   ███ ▀███▄ ███    ███ 
     ▀██████▀   ▄████████▀  █▀    ▀█   █▀    ███   ▀█▀ ████████▀  
                                             ▀                    
%s
""" % (green(), reset())

def intro():
    print(logo); credits = "       Made by %sKomodo%s and %sTakaso%s." % (blue(), reset(), red(), reset())
    for a in credits:
        time.sleep(0.2)
        sys.stdout.write(a)
        sys.stdout.flush()

class number():
    def whatsapp(number):
        # Check if number exists on whatsapp
        if " " in number:
            a = number.replace(" ", "")
        else:
            a = number
        oscuro = requests.get("https://wa.me/" + a)
        if oscuro.status_code in [a for a in range(200, 209)]:
            return True
        else:
            return False
    def general_info(number):
        bruh = number.replace(" ", "").replace("+", "")
        grr = requests.get(f"https://api.telnyx.com/anonymous/v2/number_lookup/{bruh}")
        return grr.text

class email():
    def instagram(mail):
        r = requests.post("https://instagram.com/accounts/login/ajax/", json={
            "email": mail,
            "password": "SCIENZAOSINKU"
        })
        print(r.json())         #science
        if r.status_code == 401:
            return None
        else:
            return True
                                #la po te n za
class ip():
    def lookup(ip): 
        sex_up = f"https://ipwhois.app/json/{ip}"
        grrr = requests.get(sex_up)
        print(grrr.text.replace(",", ",\n"))  

#muovi il cursore qui se sei gay:
class social():
    def github(user):
        print("Checking username on GitHub...") #sarà per tutti i social
        r = requests.get(f"https://github.com/{user}")
        if r.status_code == 200: print("Username found on github!\n"); print(f"https://github.com/{user}"); return True
    def instagram(user):
        print("Checking username on instagram...")
        r = requests.get(f"https://instagram.com/{user}")
        if r.status_code == 200: print("Username found on instagram!\n"); print(f"https://instagram.com/{user}"); return True 
        else: return False
    def facebook(user):
        print("Checking username on facebook...")
        r = requests.get(f"https://facebook.com/{user}")
        if r.status_code == 200: print("Username found o facebook!\n"); print(f"https://facebook.com/{user}"); return True
        else: return False
    def replit(user):
        matteito = requests.get(f"https://replit.com/@{user}")
        if matteito.status_code == 200: print("username found on replit!\n"); print(f"https://replit.com/@{user}")
        else: return False

def social_lookup():
    target = input('\nusername > ')
    social.github(target)
    social.instagram(target)
    social.facebook(target)
    social.replit(target)

def num():
    zioeren = input("Insert number > ")   
    print(f"""
General info:

{number.general_info(zioeren)}

""")      
    print("Whatsapp: " + str(number.whatsapp(zioeren)))

def eemail():
    sessomail = input("Type the email target > ")

def indirizzo_postale_mozzie_trava_linux_programma_per_programmare_secondo_nome_del_cracker_data_di_creazione_di_discordpy_carmine_perna_trava_mozzie_skid_trava_nn_sapete_nulla_stupidi_CLOWNS_takaso_che_chiama_la_gheng_hotface():    #AHAHAHA
    look = input("Insert the ip address > ")
    print(ip.lookup(look.replace(" ", "")))   
intro()
print("""
1 - username
2 - email
3 - number informations
4 - IP lookup
5 - exit
""")

oscuro = str(input("Which type of info do you want to sex? > "))
if oscuro == "1":
    social_lookup()
elif oscuro == "2":
    eemail()
elif oscuro == "3":
    num()
elif oscuro == "4":
    indirizzo_postale_mozzie_trava_linux_programma_per_programmare_secondo_nome_del_cracker_data_di_creazione_di_discordpy_carmine_perna_trava_mozzie_skid_trava_nn_sapete_nulla_stupidi_CLOWNS_takaso_che_chiama_la_gheng_hotface()
elif oscuro == "7":
    exit()
else:
    print("Invalid option bozo")

input()
