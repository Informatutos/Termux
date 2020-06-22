#coding:utf-8
import os,sys,time

if sys.platform in ["linux", "linux2"] :
    R = "\033[31;1m"
    V = "\033[32;1m"
    B = "\033[0m"
    C = "\033[36;1m"
    J = '\033[93m'
    M = '\033[94m'
else :
    R = ""
    V = ""
    B = ""
    c = ""
    J = ""
    M = ""

def choiX() :
    print(V+'============================')
    print(M+"1 -------->     "+J+"Install Kali")
    print(M+"2 -------->       "+J+"Lunch Kali")
    print(M+"3 -------->             "+J+"Exit")
    print('============================')
    try :
        choix = int(input(C+"===->:) "))
    except :
        sys.exit(R+"Input error")
    if(choix == 1) :
        installKali()
    elif (choix == 2 ):
        startKali()
    elif(choix == 3) :
        sys.exit(R+"Let's down kali")
    else :
        sys.exit(R+"No choice found :) !")
        #while(choix != 1 | 2 | 3) :
            #choiX()
        
def startKali() :
    print(V+"Kali Linux is Starting ...........")
    time.sleep(1)
    os.system("./start-kali.sh")
def installKali() :
    print(V+'Kali installation')
    time.sleep(0.8)
    os.system("pkg update -y && pkg upgrade -y")
    print('Termux Update and Upgrade finish')
    os.system("pkg install wget openssl-tool proot -y && hash -r")
    print("Installation of Kali components ... wait ")
    os.system("wget https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Kali/kali.sh")
    print("kali in install")
    os.system("bash kali.sh")
    print("Kali Linux successful install"+B)
    choiX()
choiX()