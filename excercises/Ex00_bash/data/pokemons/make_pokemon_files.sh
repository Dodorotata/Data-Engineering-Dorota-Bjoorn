#!/bin/bash

# read each pockemon from pokemon_list.txt, request api and save into a json file
while read pokemon; do
    curl https://pokeapi.co/api/v2/pokemon-species/$pokemon > $pokemon.json
    sleep 2
done < pokemon_list.txt