from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import random

def mail(ir):
    msg = MIMEMultipart()
    msg['From'] = "*****from*****@gmail.com"
    msg['To'] = "*****to*****@gmail.com"
    password = "**********"
    msg['Subject'] = "Code secret"
    body = "Voici votre code secret "+str(ir)
    msg.attach(MIMEText(body, 'html'))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(msg['From'], password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
    return

def intrange():
    ir = random.randrange(100000,1000000)
    return(ir)

def main():
    ir = intrange()
    mail(ir)
    print("Pour te connécter entre le code secret qui t'a été envoyé par mail !")
    erreur = True
    while erreur == True:
        erreur = False
        try:
            cs = int(input(">>> "))
            if cs != ir:
                print("Code secret invalide !")
                erreur = True
            else:
                print("Code secret bon !")
        except:
            print("Erreur de saisie !")
            erreur = True
    return
main()
