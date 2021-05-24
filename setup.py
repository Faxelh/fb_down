# !/usr/bin/python3
# coding=utf-8

import os,html,platform, sys


####################################################################################################

if "termux" in sys.prefix:
    try:
        os.system("termux-setup-storage")
    except:
        pass
    dir = "/sdcard/FbVideo"
else:
    dir = "FbVideo"
try:
    os.mkdir(dir)
except:
    pass

def _cls():
    if os.name == "nts":
        os.system("cls")
    else:
        os.system("clear")

raw_input = input
####################################################################################################
# -Importation des modules-#
try:
    import os, time,fileinput, base64, datetime, random, requests, mechanize, re, threading, json
    from datetime import datetime
    from tqdm import tqdm
    from time import sleep

    print("\033[1;92m Exigences disponibles")
    _cls()
except:
    _cls()
    print("\033[1;95m Configuration requise pour l'installation....\033[1;97m")
    os.system('pip install requests')
    os.system('pip install mechanize')
    os.system('pip install tqdm')
    _cls()


####################################################################################################
# -Automatisation-#
def Street(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.009)


def hack():
    hacking = [" ", '.', '..', '...']
    for h in hacking:
        sys.stdout.write("\r\033[1;91m[\033[38;5;112m●\033[1;91m] \033[1;92mChargement\033[1;97m" + h)
        sys.stdout.flush()
        time.sleep(1)


def load(mot):
    home = ['/', '-', '|']
    for i in range(5):
        for m in range(len(home)):
            sys.stdout.write('\r{}{}'.format(str(mot), home[m]))
            time.sleep(.3)
            sys.stdout.flush()


def charge():
    compteur = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
                "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36",
                "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53",
                "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70",
                "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87",
                "88", "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99", "100"]
    print()
    for c in compteur:
        sys.stdout.write("\r\033[1;91m[\033[38;5;245m●\033[1;91m] \033[38;5;221m©Faxel\033[1;92m " + c + " \033[1;97m%")
        sys.stdout.flush()
        time.sleep(.1)
    time.sleep(1.5)


####################################################################################################

author = (""" 
\t\t\033[38;5;28m            MES_INFORMATIONS
\t\t\033[1;97m╔═════════════════════════════════════════════╗ 
\t\t\033[1;97m║\033[38;5;29m Author    \033[1;91m: \033[38;5;112mFaxel \033[1;91m| \033[38;5;115m@faxelh                 \033[1;97m║
\t\t\033[1;97m║\033[38;5;29m Fb        \033[1;91m: \033[38;5;247mhttps://facebook.com/threatz0   \033[1;97m║
\t\t\033[1;97m║\033[38;5;29m Github    \033[1;91m: \033[38;5;247mhttps://github.com/threat0/     \033[1;97m║
\t\t\033[1;97m║\033[38;5;29m Blog      \033[1;91m: \033[38;5;247mhttps://faxelh.blogspot.com/    \033[1;97m║
\t\t\033[1;97m║\033[38;5;29m Twitter   \033[1;91m: \033[38;5;247mhttps://facebook.com/faxelhs    \033[1;97m║   
\t\t\033[1;97m║\033[38;5;29m Tool Name \033[1;91m: \033[38;5;247mFb Download                     \033[1;97m║
\t\t\033[1;97m║\033[38;5;29m Date      \033[1;91m: \033[38;5;247m18-05-2021                      \033[1;97m║
\t\t\033[1;97m║\033[38;5;29m Version   \033[1;91m: \033[38;5;198m2021.1.2                        \033[1;97m║
\t\t\033[1;97m╚═════════════════════════════════════════════╝
""")

robot = ("""   
\t\t\033[1;97m ╔═══════════════════════════╗ 
\t\t\033[1;97m ║\033[38;5;198m█████████\033[1;97m█████████\033[1;92m█████████100%\033[1;97m║
\t\t\033[1;97m ╚═══════════════════════════╝
\t\t\t\033[1;91m[\033[38;5;112mTerminer\033[1;91m]
 """)

fb_logo =("""\n\033[38;5;131m░▒\033[1;97m▓\033[38;5;214m███████████►\033[38;5;212mWrite by\033[38;5;111m Faxel\033[38;5;214m◄██████████\033[1;97m▓\033[38;5;131m▒░\n\033[38;5;131m░▒\033[1;97m▓\033[38;5;214m███████████►\033[38;5;136m╬╬╬╬╬╬╬╬╬╬╬╬╬╬\033[38;5;214m◄██████████\033[1;97m▓\033[38;5;131m▒░\n\033[38;5;131m░▒\033[1;97m▓\033[38;5;214m███►  \033[38;5;247m╔╗F╦╔═╗╔╗╔╦FF╦╔═╗╔╗╔╦F╦╔═╗\033[38;5;214m  ◄██\033[1;97m▓\033[38;5;131m▒░\n\033[38;5;131m░▒\033[1;97m▓\033[38;5;214m███►  \033[38;5;247m╠╩╗║║╣F║║║╚╗╔╝║╣F║║║║F║║╣F\033[38;5;214m  ◄██\033[1;97m▓\033[38;5;131m▒░\n\033[38;5;131m░▒\033[1;97m▓\033[38;5;214m███►  \033[38;5;247m╚═╝╩╚═╝╝╚╝F╚╝F╚═╝╝╚╝╚═╝╚═╝\033[38;5;214m  ◄██\033[1;97m▓\033[38;5;131m▒░\n\033[38;5;131m░▒\033[1;97m▓\033[38;5;214m███████████►\033[38;5;136m╬╬╬╬╬╬╬╬╬╬╬╬╬╬\033[38;5;214m◄██████████\033[1;97m▓\033[38;5;131m▒░\n\033[38;5;131m░▒\033[1;97m▓\033[38;5;214m███████████►\033[38;5;212mWrite by\033[38;5;111m Faxel\033[38;5;214m◄██████████\033[1;97m▓\033[38;5;131m▒░\n""")

####################################################################################################
#_cls()
#charge()
#_cls()
#Street("\033[1;96mVeuillez patientez le temps de verification robotique?")
#Street(robot)
#Street("\t\033[1;92mVerification reussie\033[1;97m, vous etes bien humain.\n")
#raw_input("\t\t\t\033[1;91m[\033[38;5;24m Suivant\033[1;91m]")


####################################################################################################
def identify():
    _cls()
    print("\033[38;5;214m<----------------------------------------->")
    print("\t\033[1;31m[\033[1;37m ©2021\033[1;96m Copyright\033[38;5;114m:\033[1;37m@faxelh \033[1;31m]")
    print(" \033[38;5;214m ¬\033[1;97m I'm the person whom you can never judge.\033[38;5;214m ¬")

    ids = raw_input("\033[1;31m[\033[1;37mæ\033[1;31m] \033[38;5;214m Entrer votre nom\033[1;91m : \033[38;5;108m")
    print("\033[38;5;214m<----------------------------------------->")
    if ids == "":
        print("\033[1;31m[\033[1;37m!\033[1;31m] \033[38;5;185mChamp obligatoire")
        time.sleep(1)
        identify()
    else:
        _cls()
        print(38 * '\x1b[1;97m¬')
        print(
            " Hey\033[48;5;0;38;5;197m " + ids + " \033[1;37mveuillez utiliser ce script a des faits \033[38;5;114mlégaux\033[1;97m.Merci")
        print(38 * '\x1b[1;97m¬')
        Street("""
\033[1;92mInformation \033[1;91m: \033[1;97mVous pouvez recoder, Mais n'oubliez pas de mentionner l'auteur.	
\033[1;92mInspiration \033[1;91m: \033[1;97mProgressez chaque jour avec audace vers vos\n\trêves, refusez les coups d'arrêt et rien ne pourra vous arrêter!!!
\033[1;93m------------\033[1;91m# \033[1;97mL'AVENIR C'EST MAINTENANT \033[1;91m#\033[1;93m------------- 
        """)
        Street(
            "\033[1;92mUne pensée\033[1;97m a\033[1;91m <\033[38;5;112mZachary\033[1;97m,\033[38;5;112mMec\033[1;97m,\033[38;5;112mMael\033[1;97m,\033[38;5;112mDosso\033[1;97m,\033[38;5;112mSeverin\033[1;97m,\033[38;5;112m Angel,\033[38;5;112mMiss\033[1;96m Syntiche\033[1;91m>")
        raw_input("\n\t\t\033[1;91m[ \033[38;5;24mSuivant \033[1;91m]")
        Security()


####################################################################################################
def Security():
    _cls()
    print(
        "\033[38;5;214m<-------------\033[1;97m Connexion a\033[38;5;245m Insta Video Download \033[38;5;214m----------->")
    nom = "Faxel"
    print("")
    pssd = "Faxel"
    loop = "true"
    while (loop == "true"):
        entrer_nom = raw_input(
            " \033[1;91m[\033[1;97m©\033[1;91m]\x1b[1;97m Script Name \x1b[1;91m»» \033[48;5;0;38;5;197m")
        if (entrer_nom == nom):
            entrer_pwd = raw_input(
                " \033[1;91m[\033[1;97mþ\033[1;91m]\x1b[1;97m Script Pwd  \x1b[1;91m»» \033[38;5;245m")
            if (entrer_pwd == pssd):
                print(
                    "\033[38;5;214m<-------------\033[1;97m Connexion a\033[38;5;245m Insta Video Download \033[38;5;214m----------->")
                load("\t\tChargement")
                print(
                    "\n\033[1;91m[\033[1;92m©\033[1;91m] \033[1;97mConnecté en tant que \033[1;96m" + entrer_nom)  # Dev:Faxel
                time.sleep(1)
                loop = "false"
                #os.system('xdg-open https://www.twitter.com/faxelhs')
                _cls()
                Checker()
            else:
                print("\033[1;91m[\033[1;97m×\033[1;91m] \033[1;93mMot de passe incorrect!\n")
                os.system("xdg-open https://wa.me/message/HKD56CAXOBLNC1")
                Security()
        else:
            print("\033[1;91m[\033[1;97m×\033[1;91m] \033[1;94mNom d'utilisateur incorrect!\n")
            os.system('xdg-open https://t.me/Faxelh')
            Security()


####################################################################################################
def checkInternet(url="http://www.google.com/", checktime=5):
    try:
        checkin = requests.get(url, timeout=checktime)
        checkin.raise_for_status()
        Street(
            "\t\033[1;91m[\033[38;5;112mø\033[1;91m]    \033[1;97m\033[1;92mVerification de la connexion     \033[1;91m[\033[38;5;112mø\033[1;91m]")
        Street("\t\t\033[38;5;112mVous êtes connecté à Internet\n")
        raw_input("\t\t\033[1;91m[\033[38;5;24mTaper entrer\033[1;91m]")
        return True
    except requests.HTTPError as error:
        print("La vérification de la connexion Internet a échoué, code d'état {0}.".format(error.response.status_code))
    except requests.ConnectionError:
        Street("\t\t\033[1;91mVous n'êtes pas connecté à Internet.")
    return False


####################################################################################################
def Checker():
    if checkInternet() == True:
        menu()
    else:
        Street("\t\t\033[1;91mVous n'êtes pas connecté à Internet.")
        sys.exit()


####################################################################################################
_cls()
print(fb_logo)

def menu():
    try:
        if len(list) == 2:
            if 0 in list and 1 in list:
                _cls()
                print(fb_logo)
                print("\t\t\033[1;97m╔" + 15 * "═" + 1 * "═╗")
                print("\t\t\033[1;97m║  \033[1;91m[\033[38;5;198m1.\033[1;91m] \033[38;5;112mHD       \033[1;97m║")
                print("\t\t\033[1;97m║  \033[1;91m[\033[38;5;198m2.\033[1;91m] \033[38;5;285mSD       \033[1;97m║")
                print("\t\t\033[1;97m║  \033[1;91m[\033[38;5;198m3.\033[1;91m] \033[38;5;212mUpdate   \033[1;97m║")
                print("\t\t\033[1;97m╚" + 15 * "═" + 1 * "═╝")
                print("\t\t\033[1;97m║")
                choix = raw_input("\t\t\033[1;97m╚═\033[1;31m▶\033[1;92m@\033[1;36mFaxel \033[1;31m » \033[1;33m")
                if choix == "HD" or choix == "hd" or choix == "1" or choix == "01":
                    print("\n")
                    load("\033[1;96mTéléchargement de la vidéo en qualité HD...\033[1;97m")
                    print("\n")
                    video_url = re.search(r'hd_src:"(.+?)"', html).group(1)
                    taille_fichier_demander = requests.get(video_url, stream=True)
                    taille_fichier = int(taille_fichier_demander.headers['Content-Length'])
                    taille_qualite = 1024
                    temps_fichier = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
                    t = tqdm(total=taille_fichier, unit='B', unit_scale=True, desc=nom_fichier, ascii=True)
                    with open(f"{dir}/{nom_fichier}.mp4", "wb") as f:
                        for data in taille_fichier_demander.iter_content(taille_qualite):
                            t.update(len(data))
                            f.write(data)
                    t.close()
                    print("\n\t\033[1;92mVidéo téléchargée avec succès.")
                elif choix == "SD" or choix == "sd" or choix == "2" or choix == "02":
                    print("\n")
                    load("\033[1;96mTéléchargement de la vidéo en qualité SD...\033[1;97m")
                    print("\n")
                    video_url = re.search(r'sd_src:"(.+?)"', html).group(1)
                    taille_fichier_demander = requests.get(video_url, stream=True)
                    taille_fichier = int(taille_fichier_demander.headers['Content-Length'])
                    taille_qualite = 1024
                    temps_fichier = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
                    t = tqdm(total=taille_fichier, unit='B', unit_scale=True, desc=nom_fichier, ascii=True)
                    with open(nom_fichier + '.mp4', 'wb') as f:
                        for data in taille_fichier_demander.iter_content(taille_qualite):
                            t.update(len(data))
                            f.write(data)
                    t.close()
                    print("\n\t033[1;92mVidéo téléchargée avec succès.")
                #elif choix == "3" or choix == "03":
                    #os.system("")

        if len(list) == 2:
            if 1 in list and 2 in list:
                print("\033[1;97m╔" + 27 * "═" + 1 * "═╗")
                print("\033[1;97m║ Oups! La vidéo n'est pas disponible en qualité HD.\033[1;97m║")
                print("\033[1;97m║ Souhaitez-vous le télécharger?                    \033[1;97m║")
                print("\033[1;97m╚" + 27 * "═" + 1 * "═╝")
                print("\033[1;97m║")
                _dmd = raw_input("\033[1;97m╚═\033[1;31m▶\033[1;92m@\033[1;36mFaxel \033[1;31m » \033[1;33m")
                if _dmd == 'O' or _dmd == 'o':
                    print("\n")
                    load("\033[1;96mTéléchargement de la vidéo en qualité SD...\033[1;97m")
                    print("\n")
                    video_url = re.search(r'sd_src:"(.+?)"', html).group(1)
                    taille_fichier_demander = requests.get(video_url, stream=True)
                    taille_fichier = int(taille_fichier_demander.headers['Content-Length'])
                    taille_qualite = 1024
                    temps_fichier = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
                    t = tqdm(total=taille_fichier, unit='B', unit_scale=True, desc=nom_fichier, ascii=True)
                    with open( nom_fichier + '.mp4', 'wb') as f:
                        for data in taille_fichier_demander.iter_content(taille_qualite):
                            t.update(len(data))
                            f.write(data)
                    t.close()
                    print("\n\t\033[1;92mVidéo téléchargée avec succès.")
                elif _dmd == 'n' or _dmd == 'N':
                    exit()

        if len(list) == 2:
            if 0 in list and 3 in list:
                print("\033[1;97m╔" + 27 * "═" + 1 * "═╗")
                print("\033[1;97m║ Oups! La vidéo n'est pas disponible en qualité SD.\033[1;97m║")
                print("\033[1;97m║ Souhaitez-vous le télécharger?                    \033[1;97m║")
                print("\033[1;97m╚" + 27 * "═" + 1 * "═╝")
                print("\033[1;97m║")
                _dmd = raw_input("\033[1;97m╚═\033[1;31m▶\033[1;92m@\033[1;36mFaxel \033[1;31m » \033[1;33m")
                if _dmd == 'O' or _dmd == 'o':
                    print("\n")
                    load("\033[1;96mTéléchargement de la vidéo en qualité HD...\033[1;97m")
                    print("\n")
                    video_url = re.search(r'hd_src:"(.+?)"', html).group(1)
                    taille_fichier_demander = requests.get(video_url, stream=True)
                    taille_fichier = int(taille_fichier_demander.headers['Content-Length'])
                    taille_qualite = 1024
                    temps_fichier = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
                    t = tqdm(total=taille_fichier, unit='B', unit_scale=True, desc=nom_fichier, ascii=True)
                    with open( nom_fichier + '.mp4', 'wb') as f:
                        for data in taille_fichier_demander.iter_content(taille_qualite):
                            t.update(len(data))
                            f.write(data)
                    t.close()
                    print("\n\t\033[1;92mVidéo téléchargée avec succès.")
                elif _dmd == 'n' or _dmd == 'N':
                    exit()
    except(KeyboardInterrupt):
        print("\n\t\033[1;91mProgramme Interrompu")


try:
    while True:
        url = raw_input("\n\033[1;91m[\033[1;36m©\033[1;91m] \033[1;97mEntrez l'URL de la vidéo Fb \033[1;91m : \033[1;93m")
        nom_fichier = raw_input("\033[1;91m[\033[1;36m©\033[1;91m] \033[1;97mNommer la video\033[1;91m : \033[1;95m")
        req = re.match(r'^(https:|)[/][/]www.([^/]+[.])*facebook.com', url)
        if req:
            html = requests.get(url).content.decode('utf-8')
        else:
            print("\n\t\033[1;91mUrl non lié au domaine Facebook.")
            exit()
        _qualityhd = re.search('hd_src:"https', html)
        _qualitysd = re.search('sd_src:"https', html)
        _hd = re.search('hd_src:null', html)
        _sd = re.search('sd_src:null', html)
        list = []
        _thelist = [_qualityhd, _qualitysd, _hd, _sd]
        for id, val in enumerate(_thelist):
            #if val != None:
            if val is not None:
                list.append(id)
                menu()
        dmd = raw_input("\n\033[1;97mVoulez vous télécharger une autre vidéo? (o/n)\033[1;91m : \033[1;93m").upper()
        if dmd == str("o") or dmd == str("O"):
            _cls()
            print(fb_logo)
            continue
        else:
            break
except KeyboardInterrupt:
    print("\n\t\033[1;91mProgramme Interrompu")

