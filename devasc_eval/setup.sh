#hola xd prueba 1234 probando 
DIR="$HOME/Documentos/devasc_eval"
mkdir -p "$DIR"

FILE="$DIR/prueba.txt"
echo "Contenido de prueba" > "$FILE"

#permisos
chmod 744 "$FILE"

#cambiar propietario a root
sudo chown root:root "$FILE"


