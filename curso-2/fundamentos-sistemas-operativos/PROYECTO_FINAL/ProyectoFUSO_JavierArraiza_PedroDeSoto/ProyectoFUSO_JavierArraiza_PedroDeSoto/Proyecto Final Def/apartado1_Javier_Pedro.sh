PAQUETES="python3 python3-dev git nano sudo bash gcc g++ musl-dev linux-headers wget curl htop"

for paquete in $PAQUETES; do
	if apk list --installed | grep -q "^${paquete}-"; then
		echo "$paquete ya instalado"
	else
		apk add "$paquete"
	fi 
done
