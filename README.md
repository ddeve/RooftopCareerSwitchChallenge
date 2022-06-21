# Rooftop Career Switch Challenge

El repositorio contiene todo el código fuente para resolver el challenge de ingreso.
Se tuvo en cuenta el uso de buenas prácticas de programación y escritura de código. Además se realizó el algoritmo de la función **chech**  de la forma más eficiente posible. 
La solución fue realizada en python 3.8.10, sobre ubuntu 20.04

### Instalación

Clonar el repositorio a un entorno local
```shell
git clone https://github.com/ddeve/RooftopCareerSwitchChallenge.git
```
Se recomienda el uso de un entorno virtual, para crearlo y activarlo
```shell
python -m venv venv
source venv/bin/activate
```

Para poder ejecutar la solución es necesario instalar las librerías listadas en requirements.txt: 

```shell
pip install -r requirements.txt
```

### Ejecución

Dentro del paquete ***source*** en el módulo ***main*** se encuentra el punto de entrada para ejecutar la solución:

>python main.py

realiza la ejecución por defecto, usando la llamada a la API de Rooftop.

Usando el comando:

>python main.py -h

Se mostrará el siguiente mensaje de ayuda con las opciones posibles para ejecutar:

Usage:

> python main.py [-h --help] [--use-mock] [--email=nombre@empresa.com] [-v]

Options:

 - -h --help:  Show help information.
 - --use-mock: Optional. The process is applied using mock data.
 - --email: Optional. Set email used for ask the token to Rooftop API.
 - -v: Optional. Show Riddle and solution blocks.

Notes: 

(*) Default behavior. The process is applied using Rooftop API.

Examples: 

- python main.py                                (*)
- python main.py -h
- python main.py --help
- python main.py --use-mock
- python main.py --email=daniel.deve@rooftop.com
- python main.py -v

Se usa  **PyTest** como librería para la ejecución de tests.

Dentro del paquete ***test*** en el módulo ***test_riddle*** se encuentra el test unitario. 
Se realiza un test usando mocks para evitar el llamado a la API.

Dentro del test se valida:

- Que la cantidad de Bloques del enigma sea igual a la cantidad de Bloques de la solución.
- Que la solución del enigma sea correcta.

la ejecución se realiza usando el comando:

>pytest test/