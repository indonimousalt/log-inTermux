#JanganDiRecode
#KlokNgakAdaSkillNgakUsahJadiProgrammer
#Mood By Mr. Ism1

import os
import sys
import time

blue='\033[34;1m'   #biru
green='\033[32;1m'  #hujau
purple='\033[35;1m' #ungu
cyan='\033[36;1m'   #Biru Ligth
red='\033[31;1m'    #merah
white='\033[37;1m'  #putih
yellow='\033[33;1m' #kuning

print ("\033[37;1m")
os.system("cowsay -f eyes 'MuslimCyberArmy' ")
os.system("date | lolcat")
print ("\033[34;1m_______________________________________________")
print ("\033[34;1m|<-----------------[ \033[33;1mM.C.A \033[34;1m]----------------->|")
print ("\033[34;1m|_____________________________________________\033[34;1m|")
print ("\033[34;1m|-[ \033[33;1mKEJAHATANKU ADALAH RASA KEINGINTAHUANKU \033[34;1m]-|")
print ("\033[34;1m| \033[36;1mAuthor  : \033[37;1mMr. Ism1")
print ("\033[34;1m| \033[36;1mcontack : \033[37;1moppocybera39@gmail.com")
print ("\033[34;1m| \033[36;1mTEAM    : \033[37;1mMuslim Cyber Army Comuniti")
print ("\033[34;1m|_____________________________________________>")
print ("\033[33;1m")
username = 'user'
password = 'pass'

def restart():
	ngulang = sys.executable
	os.execl(ngulang, ngulang, *sys.argv)

def main():
	uname = raw_input("username : ")
	if uname == username:
		pwd = raw_input("password : ")
		os.system('clear')
		print('')

		if pwd == password:
                        print ("\033[32;1m")
                        os.system("cowsay -f eyes 'Assalamu@laikum wr.wb'")
                        print ("\033[35;1m")
                        os.system("date")
                        print ("\033[36;1m_________________________________________\033[37;1m>")
                        print ("\033[36;1m| \033[34;1mAuthor   \033[35;1m: \033[32;1mMr. Ism1 ")
                        print ("\033[36;1m| \033[34;1mTEAM     \033[35;1m: \033[32;1mMUSLIM CYBER ARMY COMUNITI ")
                        print ("\033[36;1m| \033[34;1mContack  \033[35;1m: \033[32;1mFacebook \033[35;1m$\033[37;1mAkhy Abdillah Tampanz ")
                        print ("\033[36;1m| \033[34;1mE-Mail   \033[35;1m: \033[32;1moppocybera39@gmail.com ")
                        print ("\033[36;1m|________________________________________\033[37;1m>")
			print ("\033[31;1m[~]\033[33;1m============================================\033[31;1m[~]")
			print ("\033[33;1m<----------[ \033[36;1mWellcome To My Terminal \033[33;1m]----------->")
			print ("\033[31;1m[~]\033[33;1m============================================\033[31;1m[~]")
			sys.exit()

		else:
                        print ("\033[35;1m")
			print ("Password Yang Anda Masukkan Salah")
                        print ("\033[34;1mLogin Kembali")
                        time.sleep(2)
                        os.system('clear')
			restart()

	else:
                print ("\033[35;1m")
		print ("Username yang Anda Masukkan Salah")
                print ("\033[34;1mLogin Kembali")
                time.sleep(2)
                os.system('clear')
		restart()

try:
	main()
except KeyboardInterrupt:
	os.system('clear')
	restart()

