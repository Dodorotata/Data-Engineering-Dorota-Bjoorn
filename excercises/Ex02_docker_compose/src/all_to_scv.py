
import requests
from bs4 import BeautifulSoup
import csv
from pathlib import Path

url = "https://sv.wikipedia.org/wiki/Lista_%C3%B6ver_Pok%C3%A9mon"

output_path = Path(__file__).parent / "data"
output_path.mkdir(exist_ok=True)
output_file = output_path / "pokemon_list.csv"
output_file.as_posix()

# Send an HTTP GET request to the URL
response = requests.get(url)

# create soup object representing parsed HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the table containing the Pokémon list
pokemon_table = soup.find("table", {"class": "wikitable"})


with open(output_file, "w", newline="", encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file)

    for row in pokemon_table.find_all("tr")[1:]:
        columns = row.find_all("td")
        
        eng_name = columns[0].get_text().strip()
        number = columns[2].get_text().strip()
        type = columns[3].get_text().strip()
        
        csv_writer.writerow([eng_name, number, type])







# css selectors
# #mw-content-text > div.mw-parser-output > table.wikitable.sortable.jquery-tablesorter

# xpath
# //*[@id="mw-content-text"]/div[1]/table[2]