# TFG-Informatica_BridgeXplained
Expert System in Python for helping begginer Bridge players to learn the basics of this card game. It gives the learner all the information, **along with its corresponding reasoning**, that can be obtained from the previous moves. It also poses questions to the user about what information or action can be known from the previous moves.


TASKS:


********************** TO BE DONE **********************
-	**REGLAS EJERCICIO 1 BRIDGE**


-	**CREAR TESTS!!!!!!** Para clases (test unitarios) y para el driver (test integración)

-	SEPARAR metodos basicos de las clases (Player... metodos create, print...) con los que son CUSTOM DE LAS REGLAS DE LOS QUE QUEREMOS METER como HC !!!!!!!

	SOL: SEPARAR MODELO de SERVICIO!!!!!!!!!!!!!!!!!!

-	Probar PREGUNTAS Y RESPUESTAS AL USUARIO

-	conclusiones_fc para guardar la traza de las pruebas que se han pedido demostrar con FC y han sido verdaderas (SOLO SE VA A GUARDAR LA SENTENCIA PROBADA, *NO EL RAZONAMIENTO*)

-	PROBAR A LEER UN ESTADO DE PARTIDA DE UN .TXT (*partida.txt*) Y CARGARLO EN EL .KFB (conjunto de hechos).

-	Comentar todos los ficheros con mis datos (correo...)

-	Mejorar todos los README con celdas para las líneas de código a ejecutar... (rollo TFG Mates)

-	PYKE CON PYTHON3!!! Instalar PyKE v3 en pip3

-	*PONER PRIVADOS LOS ATRIBUTOS!!* Ahora todo es público y accesible...???

.

.

********************** IN PROGRESS **********************

-	Logging PONER HORA Y DIA DE STARTING PROGRAM!!


-	LOGGING para guardar la traza del programa y las reglas probadas. Esto permite que se pueda ejecutar en el background (lo cual permite montar un *SERVER/App web*), depurar errores, entender el comportamiento del motor, extraer las reglas probadas...

-	Escribir los mensajes de logs de las clases y del motor de inferencia en los ficheros "Sentences.py" y "UserSentences.py" correspondientes.

.

.

********************** DONE **********************

-	Estructura del proyecto: PACKAGES(+-), directorios para clases...

-	Probar a POBLAR LAS CLASES *PLAYER*, *TEAM* y *GAME* desde las propias reglas (alternativa: con los .txt de las conclusiones).

-	Gestionar accesibilidad (privado vs publico, de clase o instancia) de los métodos y atributos de las clases MANAGER. Asegurar que podemos obtener información de éstas desde driver.py u cualquier otra parte del código (los objetos se crean desde las reglas).

-	Crear excepciones de las clases creadas. Lanzar excepciones cuando fallan estas clases para gestionarlas desde driver.py.

-	Logging de eventos de clases y del motor de inferencia

-	Logging de las reglas que se piden probar junto con la conclusion (si son verdaderas o falsas)

-	Logging debug para la traza normal. Logging info para las conclusiones de si una regla introducida es verdadera o falsa. Logging error y warning para la gestion de excepciones.

.

.

********************** BACKLOG **********************

-	Convertir clases en BEANS, **libreria Pickle SERIALIZAR & Guardar partida!!**

-	Probar a quitar Sentences. en todas las frases importadas

.

*********** SERVER IDEA **************


BridgeXplained es un programa de enseñanza básica del Bridge.

La idea es montar un servidor básico utilizando Django (como hemos visto en la asignatura de PSI) para ilustrar la implementación real y práctica del programa.

Una opción sería que el programa estuviera en un repositorio de Github y ser un proyecto OpenSource de tal forma que el usuario se descargara el repositorio y corriera en local el programa.

Sin embargo, una verdadera implementación en la realidad sería que los usuarios se conecten a la web de BridgeXplained para realizar sus ejercicios.

Para cada usuario se lanzaría un proceso en el background del servidor donde se resuelve su ejercicio, junto con los correspondientes razonamientos. También podría consultar su fichero log para ver la traza del programa, O SE PODRÍA ESCRIBIR POR PANTALLA ESTA TRAZA DEL LOG!!!
