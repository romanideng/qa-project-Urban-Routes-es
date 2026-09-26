# Proyecto de Automatización de pruebas - Urban Routes


# Tecnologías utilizadas
## - Lenguaje Python mediante Pycharm
## - Selenium WebDriver para la automatización de la aplicación web
## - Pytest para las pruebas automatizadas


 En el proyecto se realizaron un total de 9 pruebas solicitadas para la función de pedir un viaje en la aplicación de Urban Routes. <br> El resultado de todas las pruebas fueron exitosas. <br>
 El código proporcionado al inicio no funcionaba para la realización de este proyecto, por lo que se corrigieron los métodos que se intentaban utilizar, con métodos actualizados para Selenium. <br> Como segundo paso solo confirmé que una vez corregidos los métodos, el código ya funcionaba y realizaba la primera prueba exitósamente. <br> Aún así para una optimización y mejor organización realicé una estructura Page Object Model, por lo que se organizaron las líneas de código en diferentes packages y archivos.py. En donde:

### data: contiene el archivo con las constantes que vamos a utilizar para llenar la información que la página solicita
### utils: contiene el código proporcionado por Tripleten para poder obtener el código de confirmación de teléfono
### pages: aquí se ubican todos los localizadores y las funciones para interactuar con cada uno (sets, gets & clickers)
### tests: archivo que contiene las lineas de código para poder realizar cada prueba

Se utilizó de manera organizada el primero localizar cada elemento de la aplicación, luego obtenerla y finalmente realizar la acción. En otra función se le daban los valores que se necesitaba para cada campo y al final, en el codigo de tests se mandaba llamar la función correspondiente junto el assert que comparaba el resultado deseado con el resultado actual para proporcionar el resultado si la prueba pasaba.
<br> Las funciones logran que WebDriver interactúe automáticamente de manera correcta con todos los elementos solicitados para las pruebas.

### Autor - Carlos Román Irecta Durán