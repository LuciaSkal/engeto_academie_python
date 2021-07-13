import requests
from bs4 import BeautifulSoup as BS
import csv
import sys

def vyber_zoznam_dat(objekt):
	return list(zip(vyber_cisla_obce(soup), vyber_nazvu_obce(soup), vyber_X_obce(soup)))

def zapis_do_csv(zoznam_dat):
	link = 'https://www.volby.cz/pls/ps2017nss/'
	resp = requests.get(link + zoznam_dat[0][2])
	hl_soup = BS(resp.text, 'html.parser')
	hlavicka = csv_hlavicka(hl_soup)
	with open(f'{soubor}.csv', 'w', newline='') as file:
		zapis = csv.writer(file)
		zapis.writerow(hlavicka)
		for data in zoznam_dat:
			link = 'https://www.volby.cz/pls/ps2017nss/'
			resp = requests.get(link + data[2])
			soup = BS(resp.text, 'html.parser')
			vysledky = vyber_vysledky(soup)
			zapis.writerow([data[0], data[1]] + vysledky)

def vyber_cisla_obce(sp):
	td_elements = vyber_elementov(sp, 't1sa1 t1sb1', 't2sa1 t2sb1', 't3sa1 t3sb1')
	td_cisla = []
	for td in td_elements:
		if td.find('a'):
			td_cisla.append(td.find('a').text)
	return td_cisla

def vyber_nazvu_obce(objekt):
	td_elements = vyber_elementov(objekt, 't1sa1 t1sb2', 't2sa1 t2sb2', 't3sa1 t3sb2')
	nazev_obce = []
	for td in td_elements:
		nazev_obce.append(td.text)
	return nazev_obce

def vyber_X_obce(objekt):
	td_elements = vyber_elementov(objekt, 't1sa1 t1sb1', 't2sa1 t2sb1', 't3sa1 t3sb1')
	td_links = []
	for td in td_elements:
		if td.find('a'):
			td_links.append(td.find('a').get('href'))
	return td_links

def vyber_elementov(objekt, *args):
	td_elementy = []
	for arg in args:
		td_elementy += objekt.select(f'td[headers="{arg}"]')
	return td_elementy

def csv_hlavicka(objekt):
	hlavicka = ['Kód obce', 'Názov obce', 'Registrovaný voliči', 'Vydané obálky', 'Platné hlasy']
	nazvy_stran = vyber_volebnych_stran(objekt)
	return hlavicka + nazvy_stran

def vyber_volebnych_stran(objekt):
	td_elements = vyber_elementov(objekt, 't1sa1 t1sb2', 't2sa1 t2sb2')
	nazvy_stran = []
	for td in td_elements:
		nazvy_stran.append(td.text)
	return nazvy_stran

def vyber_vysledky(objekt):
	return vyber_volici_obalky_hlasy(objekt) + vyber_platnych_hlasov(objekt)

def vyber_volici_obalky_hlasy(objekt):
	info_headers = ['sa2', 'sa3', 'sa6']
	info_values = []
	for info_header in info_headers:
		value_element = objekt.find('td', {'headers':f'{info_header}'})
		info_values.append(value_element.text)
	return info_values

def vyber_platnych_hlasov(objekt):
	td_elements = vyber_elementov(objekt, 't1sa2 t1sb3', 't2sa2 t2sb3')
	platne_hlasy = []
	for td in td_elements:
			platne_hlasy.append(td.text)
	return platne_hlasy

if __name__ == '__main__':
	link = input('Link pre pozadovany okres: ')
	resp = requests.get(link)
	soup = BS(resp.text, 'html.parser')
	data = vyber_zoznam_dat(soup)
	soubor = input('Nazov suboru (bez suffixu): ')
	zapis_do_csv(data)
