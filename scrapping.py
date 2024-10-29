import requests
from bs4 import BeautifulSoup
import csv

# URL de la page contenant les mots arabes
url = "https://en.wiktionary.org/wiki/Appendix:Arabic_Frequency_List_from_Quran/Arabic_Frequency_List_from_Quran_1-1000"

# Récupération du contenu de la page
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extraction des mots arabes
arabic_words = [span.get_text() for span in soup.find_all("span", {"class": "Arab"})]

# Écriture des mots dans un fichier CSV
with open("arabic_words_2.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Mot Arabe"])
    for word in arabic_words:
        writer.writerow([word])

print("Les mots ont été extraits et sauvegardés dans 'arabic_words.csv'")