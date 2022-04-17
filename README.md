# TFG-Informatica_BridgeXplained
Expert System in Python for helping begginer Bridge players to learn the basics of this card game. It gives the learner all the information, **along with its corresponding reasoning**, that can be obtained from the previous moves. It also poses questions to the user about what information or action can be known from the previous moves.


TASKS:


********************** TO BE DONE **********************

-	PONER TODOS LOS MÉTODOS DE LOS MANAGER A @classmethod (y no tener que instanciar un objeto)

-	Probar PREGUNTAS Y RESPUESTAS AL USUARIO.

-	PROBAR A LEER UN ESTADO DE PARTIDA DE UN .TXT (*partida.txt*) Y CARGARLO EN EL .KFB (conjunto de hechos).

-	*PONER PRIVADOS LOS ATRIBUTOS!!* Ahora todo es público y accesible...

-	QUITAR los prints y CREAR FICHEROS DE LOG para guardar la traza del programa. Así permitimos que se ejecute en el background, lo cual permite montar un *SERVER* donde para cada ejercicio se lance un programa.

-	conclusiones_fc para guardar la traza de las pruebas que se han pedido demostrar con FC y han sido verdaderas (SOLO SE VA A GUARDAR LA SENTENCIA PROBADA, *NO EL RAZONAMIENTO*)

-	**CREAR TESTS!!!!!!** Para clases (test unitarios) y para el driver (test integración)

-	Comentar todos los ficheros con mis datos (correo...)

-	Mejorar todos los README con celdas para las líneas de código a ejecutar... (rollo TFG Mates)

-	PYKE CON PYTHON3!!! Instalar PyKE v3 en pip3

.

.

********************** IN PROGRESS **********************

-	Probar a POBLAR LAS CLASES *PLAYER*, *TEAM* y *GAME* desde las propias reglas (alternativa: con los .txt de las conclusiones).

-	Probar a quitar Sentences. en todas las frases importadas

- Lanzar excepciones cuando falla el poblar estas clases para gestionarlas desde driver.py

- Escribir los mensajes al usuario de las clases y del driver en los ficheros "Sentences.py" y "UserSentences.py" correspondientes.

.

.

********************** DONE **********************

-	Estructura del proyecto: Directorio para clases, otro para ficheros...

.

.

********************** SERVER IDEA **********************

BridgeXplained es un programa de enseñanza básica del Bridge.

La idea es montar un servidor básico utilizando Django (como hemos visto en la asignatura de PSI) para ilustrar la implementación real y práctica del programa.

Una opción sería que el programa estuviera en un repositorio de Github y ser un proyecto OpenSource de tal forma que el usuario se descargara el repositorio y corriera en local el programa.

Sin embargo, una verdadera implementación en la realidad sería que los usuarios se conecten a la web de BridgeXplained para realizar sus ejercicios.

Para cada usuario se lanzaría un proceso en el background del servidor donde se resuelve su ejercicio, junto con los correspondientes razonamientos. También podría consultar su fichero log para ver la traza del programa, O SE PODRÍA ESCRIBIR POR PANTALLA ESTA TRAZA DEL LOG!!!
