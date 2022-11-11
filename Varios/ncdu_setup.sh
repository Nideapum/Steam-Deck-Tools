# NCDU
# · Utilidad para CLI, que permite ver de una forma muy visual que directorio está ocupando más
#-----------------------------------------------------
# URL						♦ https://dev.yorhel.nl/ncdu

# Descaraar y descomprimir
wget https://dev.yorhel.nl/download/ncdu-2.2.1-linux-x86_64.tar.gz
tar -xvf ncdu-2.2.1-linux-x86_64.tar.gz
rm ncdu-2.2.1-linux-x86_64.tar.gz

# Crear ruta y mover el programa
mkdir $HOME/.local/bin
mv ncdu $HOME/.local/bin

echo alias ncdu=\'$HOME/.local/bin/ncdu\' >> $HOME/.bashrc
