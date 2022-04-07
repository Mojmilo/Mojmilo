from re import escape
import mvsafe
import colorama
from colorama import Back, Fore, Style
import keyboard

colorama.init(autoreset=True)

#mvsafe.lock("C:\\Users\\maxim\\Documents\\Projets python\\KeyApps Safe-Box\\MaximeV") # Cacher le répertoire précis
#mvsafe.unlock("C:\\Users\\maxim\\Documents\\Projets python\\KeyApps Safe-Box\\MaximeV") # Afficher le répertoire précis
#key = mvsafe.keysup() # Obtenir la touche préssé
#cd = mvsafe.cdhere() # Obtenir l'emplacement d'ici
# mvsafe.createfolder("C:\\Users\\maxim\\Documents\\Projets python\\KeyApps Safe-Box\\MaximeVozelle")
# mvsafe.deletefolder("C:\\Users\\maxim\\Documents\\Projets python\\KeyApps Safe-Box\\MaximeVozelle")
# mvsafe.createfile("1234","C:\\Users\\maxim\\Documents\\Projets python\\KeyApps Safe-Box\\Test\\data.txt")

# mvsafe.lock(mvsafe.cdhere()+"\\"+"MaximeV") # Exemple pour cacher
# mvsafe.unlock(mvsafe.cdhere()+"\\"+"MaximeV") # Exemple pour afficher
def Start():
    mvsafe.clear()
    print(f"{Fore.YELLOW}KeyApps Safe-Box v_0.0.1{Fore.WHITE}")
    mvsafe.spaces(1)
    print(f"Help Keys {Fore.GREEN}:{Fore.WHITE}")
    print(f"{Fore.GREEN}-{Fore.WHITE} Pour accéder à votre coffre-fort, appuyez sur la touche {Fore.YELLOW}'{Fore.WHITE}A{Fore.YELLOW}'{Fore.WHITE}")
    print(f"{Fore.GREEN}-{Fore.WHITE} Pour créer un coffre-fort, appuyez sur la touche {Fore.YELLOW}'{Fore.WHITE}C{Fore.YELLOW}'{Fore.WHITE}")
    print(f"{Fore.GREEN}-{Fore.WHITE} Pour afficher la liste de vos coffres-fort, appuyez sur la touche {Fore.YELLOW}'{Fore.WHITE}F{Fore.YELLOW}'{Fore.WHITE}")
    print(f"{Fore.GREEN}-{Fore.WHITE} Pour afficher les informations concerant le logiciel KeyApps, appuyez sur la touche {Fore.YELLOW}'{Fore.WHITE}I{Fore.YELLOW}'{Fore.WHITE}")
    mvsafe.spaces(1)
    print(f"{Fore.GREEN}-{Fore.WHITE} Pour retourner en arrière, appuyer sur la touche {Fore.YELLOW}'{Fore.WHITE}B{Fore.YELLOW}'{Fore.WHITE}")
    print(f"{Fore.GREEN}-{Fore.WHITE} Pour quiter l'application, appuyer sur la touche {Fore.YELLOW}'{Fore.WHITE}Q{Fore.YELLOW}'{Fore.WHITE}")
    mvsafe.spaces(1)
    EnterKeyStart()
    return

def ShowInfo():
    mvsafe.clear()
    print(f"{Fore.GREEN}-{Fore.WHITE} Pour retourner en arrière, appuyer sur la touche {Fore.YELLOW}'{Fore.WHITE}B{Fore.YELLOW}'{Fore.WHITE}")
    print(f"{Fore.GREEN}-{Fore.WHITE} Pour quiter l'application, appuyer sur la touche {Fore.YELLOW}'{Fore.WHITE}Q{Fore.YELLOW}'{Fore.WHITE}")
    mvsafe.spaces(1)
    print(f"Voici les informations concerant l'application KeyApps Safe-Box {Fore.GREEN}:{Fore.WHITE}")
    mvsafe.spaces(1)
    print(f"Version de l'application {Fore.GREEN}:{Fore.WHITE} v_0.0.1 trial_version")
    mvsafe.spaces(1)
    EnterKeyInfo()
    return

def ShowListChest():
    mvsafe.clear()
    print(f"{Fore.GREEN}-{Fore.WHITE} Pour retourner en arrière, appuyer sur la touche {Fore.YELLOW}'{Fore.WHITE}B{Fore.YELLOW}'{Fore.WHITE}")
    print(f"{Fore.GREEN}-{Fore.WHITE} Pour quiter l'application, appuyer sur la touche {Fore.YELLOW}'{Fore.WHITE}Q{Fore.YELLOW}'{Fore.WHITE}")
    mvsafe.spaces(1)
    print(f"Liste des coffres-fort {Fore.GREEN}:{Fore.WHITE}")
    mvsafe.spaces(1)
    mvsafe.ListFolder(mvsafe.cdhere2(),"data.txt")
    mvsafe.spaces(1)
    EnterKeyListChest()
    return

def MainChest(Name,Pwd):
    mvsafe.clear()
    print(f"{Fore.WHITE}Help Keys {Fore.GREEN}:{Fore.WHITE}")
    print(f"{Fore.GREEN}-{Fore.WHITE} Pour vérouiller votre coffre-fort, appuyez sur la touche {Fore.YELLOW}'{Fore.WHITE}L{Fore.YELLOW}'{Fore.WHITE}")
    print(f"{Fore.GREEN}-{Fore.WHITE} Pour dévérouiller votre coffre-fort, appuyez sur la touche {Fore.YELLOW}'{Fore.WHITE}U{Fore.YELLOW}'{Fore.WHITE}")
    print(f"{Fore.GREEN}-{Fore.WHITE} Pour ouvrir votre coffre-fort, appuyez sur la touche {Fore.YELLOW}'{Fore.WHITE}O{Fore.YELLOW}'{Fore.WHITE}")
    print(f"{Fore.GREEN}-{Fore.LIGHTRED_EX} Pour modifier le mot de pass de votre coffre-fort, appuyez sur la touche {Fore.YELLOW}'{Fore.WHITE}P{Fore.YELLOW}'{Fore.WHITE}")
    print(f"{Fore.GREEN}-{Fore.LIGHTRED_EX} Pour modifier le nom de votre coffre-fort, appuyez sur la touche {Fore.YELLOW}'{Fore.WHITE}N{Fore.YELLOW}'{Fore.WHITE}")
    print(f"{Fore.GREEN}-{Fore.LIGHTRED_EX} Pour supprimer votre coffre-fort, appuyez sur la touche {Fore.YELLOW}'{Fore.WHITE}D{Fore.YELLOW}'{Fore.WHITE}")
    mvsafe.spaces(1)
    print(f"{Fore.GREEN}-{Fore.WHITE} Pour retourner en arrière, appuyer sur la touche {Fore.YELLOW}'{Fore.WHITE}B{Fore.YELLOW}'{Fore.WHITE}")
    print(f"{Fore.GREEN}-{Fore.WHITE} Pour quiter l'application, appuyer sur la touche {Fore.YELLOW}'{Fore.WHITE}Q{Fore.YELLOW}'{Fore.WHITE}")
    mvsafe.spaces(1)
    EnterKeyMainChest(Name,Pwd)
    return

def CreateChest():
    mvsafe.clear()
    keyboard.press('escape')
    print("Entrez un nom pour votre nouveau coffre-fort !")

    List = mvsafe.ListFolder2(mvsafe.cdhere2())
    
    erreur = True
    while erreur == True:
        erreur = False
        mvsafe.spaces(1)
        Name = input(f"{Fore.LIGHTMAGENTA_EX}>>>{Fore.WHITE} Enter Name {Fore.LIGHTMAGENTA_EX}>>>{Fore.LIGHTCYAN_EX} ")
        if Name in List:
            mvsafe.spaces(1)
            print(f"{Fore.RED}Impossible de créer ce coffre-fort !{Fore.WHITE}")
            erreur = True
    mvsafe.spaces(1)       
    print("Entrez un mot de pass pour votre nouveau coffre-fort !")

    erreurmdp = True
    while erreurmdp == True:
        erreurmdp = False
        mvsafe.spaces(1)
        try:
            Pwd = int(input(f"{Fore.LIGHTRED_EX}>>>{Fore.WHITE} Enter Password {Fore.LIGHTRED_EX}>>>{Fore.LIGHTCYAN_EX} "))
            Pwd = str(Pwd)
        except:
            mvsafe.spaces(1)
            print(f"{Fore.RED}Votre mot de pass dois contenir que de chiffres !{Fore.WHITE}")
            erreurmdp = True

    mvsafe.createfolder(mvsafe.cdhere2()+"\\"+Name) # Créer le coffre-fort
    mvsafe.createfile(Pwd,mvsafe.cdhere2()+"\\"+Name+"\\"+"data.txt") # Créer le fichier mot de pass
    mvsafe.lock(mvsafe.cdhere2()+"\\"+Name+"\\"+"data.txt") # Cache le fichier mot de pass
    MainChest(Name,Pwd)
    return

def AccessChest():
    mvsafe.clear()
    keyboard.press('escape')
    print("Entrez le nom du coffre-fort souhaité, inscrit dans la liste ci-dessous !")
    mvsafe.spaces(1)
    print(f"Liste des coffres-fort {Fore.GREEN}:{Fore.WHITE}")
    mvsafe.spaces(1)
    List = mvsafe.ListFolder(mvsafe.cdhere2(),"data.txt")
    mvsafe.spaces(1)

    erreur = True
    while erreur == True:
        erreur = False
        mvsafe.spaces(1)
        Name = input(f"{Fore.LIGHTMAGENTA_EX}>>>{Fore.WHITE} Enter Name {Fore.LIGHTMAGENTA_EX}>>>{Fore.LIGHTCYAN_EX} ")
        if Name not in List:
            mvsafe.spaces(1)
            print(f"{Fore.RED}erreur de coffre-fort !{Fore.WHITE}")
            erreur = True

    mvsafe.spaces(1)
    
    PwdGood = int(mvsafe.FindFile(mvsafe.cdhere2()+"\\"+Name,"data.txt"))
    
    erreur = True
    while erreur == True:
        erreur = False
        mvsafe.spaces(1)

        erreurmdp = True
        while erreurmdp == True:
            erreurmdp = False
            try:
                Pwd = int(input(f"{Fore.LIGHTRED_EX}>>>{Fore.WHITE} Enter Password {Fore.LIGHTRED_EX}>>>{Fore.LIGHTCYAN_EX} "))
                #Pwd = str(Pwd)
            except:
                mvsafe.spaces(1)
                print(f"{Fore.RED}Votre mot de pass dois contenir que de chiffres !{Fore.WHITE}")
                mvsafe.spaces(1)
                erreurmdp = True

        if Pwd != PwdGood:
            mvsafe.spaces(1)
            print(f"{Fore.RED}erreur de mot de pass !{Fore.WHITE}")
            erreur = True
    
    MainChest(Name,Pwd)
    return

def EnterKeyStart():
    print(f"{Fore.GREEN}<<<{Fore.WHITE} Enter Key {Fore.GREEN}>>>{Fore.WHITE}")
    erreur = True
    while erreur == True:
        erreur = False
        key = mvsafe.keysup()
        if key == 'a':
            AccessChest()
        else:
            if key == 'c':
                CreateChest()
            else:
                if key == 'f':
                    ShowListChest()
                else:
                    if key == 'i':
                        ShowInfo()
                    else:
                        if key == 'b':
                            Start()
                        else:
                            if key == 'q':
                                quit()
                            else:
                                erreur = True
    return

def EnterKeyMainChest(Name,Pwd):
    print(f"{Fore.GREEN}<<<{Fore.WHITE} Enter Key {Fore.GREEN}>>>{Fore.WHITE}")
    erreur = True
    while erreur == True:
        erreur = False
        key = mvsafe.keysup()
        if key == 'l':
            mvsafe.lock(mvsafe.cdhere2()+"\\"+Name)
            MainChest(Name,Pwd)
        else:
            if key == 'u':
                mvsafe.unlock(mvsafe.cdhere2()+"\\"+Name)
                MainChest(Name,Pwd)
            else:
                if key == 'o':
                    print("Ouverture de votre coffre-fort !")
                    mvsafe.OpenFolder(mvsafe.cdhere2()+"\\"+Name)
                    MainChest(Name,Pwd)
                else:
                    if key == 'p':
                        print()
                    else:
                        if key == 'n':
                            print()
                        else:
                            if key == 'd':
                                print("Vous ne pouvez pas supprimer ce coffre-fort !")
                                MainChest(Name,Pwd)
                            else:
                                if key == 'b':
                                    Start()
                                else:
                                    if key == 'q':
                                        quit()
                                    else:
                                        erreur = True
    return

def EnterKeyListChest():
    print(f"{Fore.GREEN}<<<{Fore.WHITE} Enter Key {Fore.GREEN}>>>{Fore.WHITE}")
    erreur = True
    while erreur == True:
        erreur = False
        key = mvsafe.keysup()
        if key == 'b':
            Start()
        else:
            if key == 'q':
                quit()
            else:
                erreur = True
    return

def EnterKeyInfo():
    print(f"{Fore.GREEN}<<<{Fore.WHITE} Enter Key {Fore.GREEN}>>>{Fore.WHITE}")
    erreur = True
    while erreur == True:
        erreur = False
        key = mvsafe.keysup()
        if key == 'b':
            Start()
        else:
            if key == 'q':
                quit()
            else:
                erreur = True
    return

def main():
    Start()
    return

main()
