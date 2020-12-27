#!/usr/bin/env python3

from bs4 import BeautifulSoup as soup 
from urllib.request import urlopen 

url = input("Inserisci il link di una pagina del sito newegg.com : ")
try:
	connessione = urlopen(url)
	html = connessione.read()
	connessione.close()

	pagina = soup(html,"html.parser")

	# Immagazinamento nomi dei prodotti
	contenitori = pagina.findAll("div",{"class":"item-container"})
	lista_nomi = []
	for i in range (0,len(contenitori)):
		a = contenitori[i].findAll("a",{"class":"item-title"})
		a = str(a)[0:len(a)-3]
		lista_nomi.append(a[str(a).rindex('>')+1:str(a).rindex('<')])
		
	# Immagazinamento prezzi dei prodotti
	contenitori = pagina.findAll("li",{"class":"price-current"})
	lista_prezzi = []
	for i in range (0,len(contenitori)):
		strong = contenitori[i].findAll("strong")
		strong = str(strong)[9:len(strong)-11]
		sup = contenitori[i].findAll("sup")
		sup = str(sup)[6:len(sup)-8]
		prezzo = str(strong) + str(sup)
		lista_prezzi.append(str(prezzo))

	# Stampa
	print("______________________________________________________________")
	for i in range(0,len(contenitori)):
		try:
			print(str(lista_nomi[i]) + '\n' + str(lista_prezzi[i]) + '\n')
		except:
			pass
	print("______________________________________________________________")
except:
	print("Impossibile aprire la pagina richiesta.")