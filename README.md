# 📄 XML Attribute Extractor 📄
Un sencillo script en Python para extraer atributos específicos de un archivo XML.

## Table of Contents
1. [📝 Descripción](#Descripción)
2. [🚀 Características](#Características)
3. [ℹ️ Instrucciones de Uso](#ⓘ--instrucciones-de-Uso)
4. [🎨 Ejemplo](#Ejemplo)
5. [📝 Nota](#Nota)


## Descripción
Este script te permite extraer los valores de uno o varios atributos de un archivo XML dado. ¡No más búsquedas manuales en archivos XML voluminosos! Solo proporciona el nombre del archivo XML y los nombres de los atributos que deseas extraer, y el script se encargará del resto.

## Características
- Analiza y extrae atributos de archivos XML de manera eficiente.
- Interfaz de línea de comandos fácil de usar.
- Muestra los valores de los atributos en un formato legible.

## ⓘ  Instrucciones de Uso
1. Asegúrate de tener Python instalado en tu sistema.
2. Ejecuta el script desde la línea de comandos con el siguiente formato:


```bash
python3 script.py archivo.xml nombre_atributo1 nombre_atributo2 ...
```

Reemplaza `archivo.xml` con el nombre del archivo XML y `nombre_atributoX` con los nombres de los atributos que deseas extraer.

## Ejemplo
Supongamos que tienes un archivo XML llamado `datos.xml` con los siguientes contenidos:
```xml
<usuarios>
 <usuario id="1" nombre="Alice" />
 <usuario id="2" nombre="Bob" />
</usuarios>
```
Ejecutar el script de la siguiente manera:
```bash
python3 script.py datos.xml id nombre
```
Producirá la siguiente salida:
```
1 Alice
2 Bob
```

### Nota

Script created by c3Nz (@n0c3Nz) para trabajar con archivos XML de manera más eficiente. ¡No dudes en contribuir y mejorar este proyecto!

🔗 ¡Explora, experimenta y diviértete extrayendo atributos XML de manera más inteligente!
