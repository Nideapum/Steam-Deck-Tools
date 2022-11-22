# Buscar el ID de los juegos instalados
find ~/Games/steam/steamapps/ -maxdepth 1 -type f -name '*.acf' -exec awk -F '"' '/"appid|name/{ printf $4 "|" } END { print "" }' {} \; | column -t -s '|' | sort -k 2 | grep -i <game_name>

# Ejecutar un juego por ID
steam steam://rungameid/{YourGameID}


