#!/bin/bash

# list pokemons from pokemon_list file in terminal
while read pokemon; do
  echo "pokemon: $pokemon"
done < pokemon_list.txt