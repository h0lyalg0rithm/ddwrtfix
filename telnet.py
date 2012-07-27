import getpass
import sys
import telnetlib

HOST = raw_input("Enter router ip address : ")
user = raw_input("Enter your router username : ")
password = raw_input("Enter your router password : ")
encrypt =  "psk2"
method = "aes"
passphrase = raw_input("Enter the passphrase : ")



tn = telnetlib.Telnet(HOST)

print tn.read_until("login: "),
tn.write(user + "\n")
print tn.read_until("Password:")
tn.write(password + "\n")
print tn.read_until("$",5),
tn.write("nvram show | grep wl0_\n")
print tn.read_until("$",5),
print "\n"
tn.write("nvram set wl0_akm="+encrypt+"\n")
print tn.read_until("$",5),
tn.write("nvram set wl0_crypto="+method+"\n")
print tn.read_until("$",5),
tn.write("nvram set wl0_wpa_psk="+passphrase+"\n")
print tn.read_until("$",5),
tn.write("nvram get wl0_akm\n")
print tn.read_until("$",5),
tn.write("nvram get wl0_crypto\n")
print tn.read_until("$",5),
tn.write("nvram get wl0_wpa_psk\n")
print tn.read_until("$",5),
tn.write("nvram commit\n")
print tn.read_until("$",5),
tn.write("reboot\n")
