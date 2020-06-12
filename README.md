# web-scraper-scrapy

## Requerimientos
- Scrapy

## Instalación de requerimientos
Ejecutar el comando:  
`pip install -r requirements.txt` ó  
`pip install Scrapy`  

## Ejecutar el scraper
Ejecutar el comando:  
`scrapy runspider spider.py -o stack_preguntas.csv -t csv`  
Donde:  
- *spider.py* -> nombre del archivo que contiene el spider  
- *-o stack_preguntas.csv* -> archivo de salida para almacenar datos recolectados  
- *-t csv* -> formato del archivo de salida  
