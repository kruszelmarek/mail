import argparse, smtplib, sys

parser = argparse.ArgumentParser()
parser.add_argument("args", nargs='*', help="args")

args = parser.parse_args()

reciever = ""
title = ""
message = ""
current = 0

for arg in (str((args.args)).replace("[", "").replace("]", "")).split(", "):
    if current == 0:
        reciever = str(arg).replace("\'", "")
        current += 1
    elif current == 1:
        title += str(arg).replace("\'", "")
        current += 1
    elif current == 2:
        if arg.startswith("\"") or arg.endswith("\""):
            arg = arg.translate(None, "\"")
        message += str(arg).replace("\'", "")
        current += 3 
    else:
        sys.exit("Wpisz to dobrze: <ADRESAT> \"<TYTUL>\" \"<WIADOMOSC>\"")

email = input("E-mail: ");
password = input("Haslo: ")

def createMessage(reciever, emailfrom, title, message):
    text = "\r\n".join([
  "From: "+ emailfrom,
  "To:  " + reciever,
  "Subject: " + title,
  "",
  message
  ])
    return text

text = createMessage(reciever, email, title, message)

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(email, password)
    server.sendmail(email, reciever, text)
    print("")
    print("Mail zostal wyslany")
except:
    print("")
    sys.exit("Nie mozna wyslac maila")
