import requests
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
            return True                          #la po te n za
class ip():
    def lookup(ip): 
        sex_up = f"https://ipwhois.app/json/{ip}"
        grrr = requests.get(sex_up)
        print(grrr.text.replace(",", ",\n"))  
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
