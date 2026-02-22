#!/usr/bin/env python
import os
os.system("apt-get install figlet")
os.system("clear")
def menu():
	try:
		while True:
			os.system("figlet WordPress Scanner")
			print(""" 
1)Fast Scan
2)Plugin Scan
3)Theme Scan
4)Admin Username Scan
			""")	
			islemn = input("Enter process you want: ")
			site = input("Enter site name: ")
			
			if(islemn == "1"):
				os.system("wpscan --url " + site )
				break
			elif(islemn == "2"):
				os.system("wpscan --url " + site  + " --enumerate p")
				break
			elif(islemn == "3"):
				os.system("wpscan --url " + site + " --enumerate at")
				break
			elif(islemn == "4"):
				os.system("wpscan --url " + site + " --enumerate u ")
				break
			else:
				print("Wrong Input")
				os.system(wordpres.py) 
	except KeyboardInterrupt:
		print(" Exiting...")
if __name__ == "__main__":
	menu()
