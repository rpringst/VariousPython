import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.pokemonpets.com/Bulbasaur-Pokemon-Pokedex-1')
soup = BeautifulSoup(r.content, "html.parser")
#print(soup.prettify())
print(soup.body)
