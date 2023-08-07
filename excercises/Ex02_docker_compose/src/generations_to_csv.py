# this part scrapes the correct table from wiki

import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_Pok%C3%A9mon"

response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")

tables = soup.find_all("table", {"class": "wikitable"})
# select 3rd table on the page
generation_table = tables[2]

# add code where pokemons in row 3 in table indicate start of a new generation



# this part writes to 9 files???????

import csv

original_file_path = "./pokemon_list.csv"
with open(original_file_path, "r") as original_file:
    csv_reader = csv.reader(original_file)
    
    # Define the row numbers at which to break the file manually
    break_points = [152, 252, 387, 494, 650, 722, 810, 906]
    
    current_break = 0  # Index for the break_points list
    current_file_number = 1
    output_file_path = f"generation{current_file_number}.csv"

    with open(output_file_path, "w", newline="") as output_file:
        csv_writer = csv.writer(output_file)
        
        # Loop through the original file and write rows to smaller files
        for index, row in enumerate(csv_reader, start=1):
            csv_writer.writerow(row)
            
            if index == break_points[current_break]:
                current_break += 1
                current_file_number += 1
                
                output_file_path = f"generation{current_file_number}.csv"
                with open(output_file_path, "w", newline="") as new_output_file:
                    csv_writer = csv.writer(new_output_file)
