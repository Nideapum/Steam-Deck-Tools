# Herramientas para Steam Deck
Otros Githubs interesantes

### Info
- [steamdb](https://steamdb.info) - Consultar Protones.
- [steamdeckkhq](https://steamdeckhq.com/game-settings/) - Configuraciones para los juegos.
- [EPIC free game](https://rsshub.app/epicgames/freegames/es) - Juego gratis de la semana en EPIC.

### Clean
- [Steam Deck: Shader Cache Killer](https://github.com/scawp/Steam-Deck.Shader-Cache-Killer) - Limpiar shadercache y compactdata ([Leer](https://github.com/Nideapum/Steam-Deck-Tools/blob/main/readme.md#shader-cache-killer-cleanner))

### Customize
- [Startup_video](https://github.com/Nideapum/Steam-Deck-Tools/tree/main/Startup_video) - Permite cambiar el video de arranque.
- [Decky](https://github.com/SteamDeckHomebrew/decky-loader) - Plugins
- [Steam Tinker Launch](https://github.com/sonic2kk/steamtinkerlaunch)

------
## CONFIGURACIÓN
### Establecer contrasaeña de administrador
Entramos en konsole (Ctrl+Alt+T) y ejecutamos
```bash
passwd
```
Introducimos la nueva contraseña
_No cambiará nada mientras escribimos pero se estara tecleando._

### Shader Cache Killer
Herramienta para hacer limpieza de los ficheros que crea steam cuando ejecuta un juego por primera vez.
También tenéis el ejecutable en [Varios]().
```bash
curl https://raw.githubusercontent.com/FranjeGueje/DeckTools/master/Tools/steamappsCleaner.sh | bash -s
```

### Idioma en Español
```bash
curl https://raw.githubusercontent.com/Nideapum/Steam-Deck-Tools/main/Varios/deck_ES.sh | bash -s
```
Después de esto habria que modificar el input del teclado en las preferencias del sistema, para que nos ubique correctamente los caracteres.

## [NCDU](https://github.com/Nideapum/Steam-Deck-Tools/blob/main/Varios/ncdu_setup.sh)
Permite ver desde el terminal el espacio utilizado por cada directorio.
Como alternativa gráfica en el modo escritorio está __Analizer Disk Usage__.


## [Discord Overlay](https://trigg.github.io/Discover/deckaddnonsteamgame)
Para que aparezcan los avatares, superpuestos, de las personas que están hablando por Discord.
------

# COMANDOS
Acceder a gaming mode.
```
qdbus org.kde.Shutdown /Shutdown org.kde.Shutdown.logout
```
