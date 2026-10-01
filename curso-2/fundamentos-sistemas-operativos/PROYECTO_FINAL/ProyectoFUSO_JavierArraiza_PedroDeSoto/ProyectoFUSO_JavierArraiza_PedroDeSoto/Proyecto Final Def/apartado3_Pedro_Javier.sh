#!/bin/bash
URL="https://drive.google.com/uc?export=download&id=1PHWBGuwDHw4ZEIlCbgMTiEUrG8FmlJK2"

PATH_MAIN_PYTHON="ProyectoFUSO/generate_maps.py"
PATH_GOWALLA_FILES="DatasetsGowalla"
PATH_OUTPUT_GOWALLA_FILES="ProyectoFUSO/templates/html_files/"
ARCHIVO_ZIP="DatasetsGowalla.zip"

echo "Descargamos datos de Gowalla..."
if [ ! -f "$ARCHIVO_ZIP" ]; then
	wget --no-check-certificate "$URL" -O "$ARCHIVO_ZIP"
fi

echo -e "\nDescomprimimos el archivo..."
unzip -o "$ARCHIVO_ZIP"

touch ALL_LOCATIONS.txt
> ALL_LOCATIONS.txt	#vacio el archivo (por si acaso)

if [ -d filtered ]; then
	echo "Ya existe esta carpeta, la vaciamos por si acaso..."
	rm -f filtered/* 
else
	mkdir -p filtered
fi

for archivo in "$PATH_GOWALLA_FILES"/*.txt;
do
	
	nombre_fichero=$(basename "$archivo")	#ElPasoGowalla.txt
	nombre_ciudad=${nombre_fichero%Gowalla.txt}	#ElPaso

	cut  -f3,4,5 "$archivo" >> ALL_LOCATIONS.txt

	cut  -f1,2,5 "$archivo" > "filtered/${nombre_ciudad}filtered.txt"
done

for fichero in filtered/*.txt; 
do
	nombre_fichero=$(basename "$fichero")	#ElPasofiltered.txt
	nombre_ciudad=${nombre_fichero%filtered.txt}	#ElPaso

	usuarios=$(cut -f1 "$fichero" | sort | uniq | wc -l)
	lugares=$(cut -f3 "$fichero" | sort | uniq | wc -l)	#Fila 3 (dentro de ficheros filtrados)
	interacciones=$(sort "$fichero" | uniq | wc -l)
	
	ch_in_julio=$(grep '2010-07' "$fichero" | sort | uniq | wc -l)
	ch_in_agosto=$(grep '2010-08' "$fichero" | sort | uniq | wc -l)
	
	echo -e "\n"
	echo "Estadísticas para $nombre_ciudad"
	echo "Número de usuarios distintos: $usuarios"
	echo "Número de localizaciones distintas: $lugares"
	echo "Número de filas completas: $interacciones"
	echo "Número de checks-in 2010-07 (únicos): $ch_in_julio"
	echo "Número de checks-in-2010-08 (únicos): $ch_in_agosto"

done

echo
echo "Ahora, utilizaremos el script de Python para comparar estadisticas..."
echo
python3 python_apartado3.py

echo
echo "Ahora activaremos el entorno virtual!"
echo
source ProyectoFUSO/venv/bin/activate

#Mapas de ciudades

for ciudad in ElPaso Glasgow Manchester WashingtonDC;
do
	echo	
	echo "Generando mapa de $ciudad..."
	python3 ProyectoFUSO/generate_maps.py --input_file "DatasetsGowalla/${ciudad}Gowalla.txt" --city_name "$ciudad" --output_html "ProyectoFUSO/templates/html_files/${ciudad}GowallaMap"
	echo "Mapa correctamente generado y guardado en ProyectoFUSO/templates/html_files"
done

#Mapas individuales

usuario_ElPaso=184477
usuario_Glasgow=190024
usuario_Manchester=196514
usuario_WashingtonDC=196177

ciudades=(ElPaso Glasgow Manchester WashingtonDC)
usuarios=("$usuario_ElPaso" "$usuario_Glasgow" "$usuario_Manchester" "$usuario_WashingtonDC")

for i in "${!ciudades[@]}";	#La función "${!ciudades[@]"}" devuelve todos los índices del array ciudades
do
	ciudad="${ciudades[$i]}"
	usuario="${usuarios[$i]}"
	echo
	echo "Generando mapa de $ciudad para usuario: $usuario"
	
	python3 ProyectoFUSO/generate_individual_maps.py --input_file "DatasetsGowalla/${ciudad}Gowalla.txt" --city_name "$ciudad" --user_id "$usuario" --output_html "ProyectoFUSO/templates/html_files/${ciudad}_${usuario}GowallaMap.html"
	echo "Mapa correctamente generado y guardado en ProyectoFUSO/templates/html_files"
done

#Topn selections

PATH_OUTPUT_GOWALLA_FILES="ProyectoFUSO/templates/html_files/"
mkdir -p ProyectoFUSO/Top5

for ciudad in ElPaso Glasgow Manchester WashingtonDC; do
    INPUT_FILE="filtered/${ciudad}filtered.txt"
    TOP_OUTPUT_FILE="ProyectoFUSO/Top5/${ciudad}Gowalla_top5.txt"

    echo "Calculando top 5 usuarios para ${ciudad}..."
    python3 topn_selection_Pedro_Javier.py "${INPUT_FILE}" 5 "${TOP_OUTPUT_FILE}"

    echo "Generando mapas individuales de los usuarios top de ${ciudad}..."

    while IFS= read -r LINE; do
        # LINE = "19601: 411 visitas."
        [ -z "${LINE}" ] && continue

        # Nos quedamos solo con lo que hay antes de ":" y quitamos espacios
        USER_ID=$(echo "${LINE}" | cut -d':' -f1 | xargs)

        echo "Mapa para usuario ${USER_ID} en ${ciudad}"

        python3 ProyectoFUSO/generate_individual_maps.py \
            --input_file "DatasetsGowalla/${ciudad}Gowalla.txt" \
            --city_name "${ciudad}" \
            --user_id "${USER_ID}" \
            --output_html "${PATH_OUTPUT_GOWALLA_FILES}${ciudad}_${USER_ID}GowallaMap.html"

    done < "${TOP_OUTPUT_FILE}"
done
python3 ProyectoFUSO/main.py
