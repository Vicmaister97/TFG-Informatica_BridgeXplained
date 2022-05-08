# TFG-Informatica_BridgeXplained
Expert System in Python for helping begginer Bridge players to learn the basics of this card game. Among with our knowledge-based inference engine built with PyKe (http://pyke.sourceforge.net/), it gives the learner all the information, **along with its corresponding reasoning**, that can be obtained from the current game status.

Possible feature: It allows to pose questions to the user (some kind of chat), for example about what information can be known from the previous moves and which is the best action (according to our inference engine).


TASKS:


********************** TO BE DONE **********************


-	**REGLAS EJERCICIO 1 BRIDGE**

-	**CREAR TESTS!!!!!!** Para clases (test unitarios) y para el driver (test integración)



---- USABILIDAD ----

-	Sacar *lista de reglas actualizadas definidas en el .krb* para poder *preguntarlas como usuario*. Es que si no, no tiene sentido pq no van a poder hacer preguntas de razonamientos especificos.

	-	**GUARDAR PAR REGLA/EXPICACION CON FRASE**, que sea human-readable vamos. Que pregunta 

	driver.bc('bc_numbers.honores_corazones_new_post(S, 1)', True)

	Y que entienda que regla es honores_corazones_new_post:
		*regla con el numero de honores en corazones de un jugador como conclusion del motor despues de haber sacado que se conocen todos los honores en ese palo*


-	*conclusiones_fc* MEJORAR que solo se pongan las reglas verdaderas y falsas (minimo todo casi rollo lista, NO rollo log de begin y end).

	- Darle una vuelta a bc (2, uno como esta con el razonamiento y otro rollo fc lista)



-	**ARBOL DE RAZONAMIENTO/DEDUCCION!!!!!!!!!!!!!!!!!!**

	-	Representacion grafica del **arbol logico** en cada deduccion, compo hace DFS o recorrido en profundidad de las reglas logicas
	
	-	Tabular los "VIENE DE --" para visión de arbol



-	SEPARAR metodos basicos de las clases (Player... metodos create, print...) con los que son CUSTOM DE LAS REGLAS DE LOS QUE QUEREMOS METER como HC !!!!!!!

	SOL: SEPARAR MODELO de SERVICIO!!!!!!!!!!!!!!!!!!

-	Probar PREGUNTAS Y RESPUESTAS AL USUARIO

-	CREADOR DE EJERCICIOS DINÁMICO!!!!!!!!

	-	PROBAR A LEER UN ESTADO DE PARTIDA DE UN .TXT (*partida.txt*) Y CARGARLO EN EL .KFB (conjunto de hechos).

-	Comentar todos los ficheros con mis datos (correo...)

-	Mejorar todos los README con celdas para las líneas de código a ejecutar... (rollo TFG Mates)


.

.

********************** IN PROGRESS **********************


-	UNIR ManageGame con driver!!! Poner todos los métodos de ManageGame como métodos del driver para llamarlos.

	-	Quizás crear BridgeXplained.py donde se llama a driver y los métodos de ManageGames, ManagePlayers y ManageTeams

-	Logging engine stats

.

.

********************** DONE **********************

-	Estructura del proyecto: PACKAGES(+-), directorios para clases...

-	Probar a POBLAR LAS CLASES *PLAYER*, *TEAM* y *GAME* desde las propias reglas (alternativa: con los .txt de las conclusiones).

-	Gestionar accesibilidad (privado vs publico, de clase o instancia) de los métodos y atributos de las clases MANAGER. Asegurar que podemos obtener información de éstas desde driver.py u cualquier otra parte del código (los objetos se crean desde las reglas).

-	Crear excepciones de las clases creadas. Lanzar excepciones cuando fallan estas clases para gestionarlas desde driver.py.

-	LOGGING para guardar la traza del programa y las reglas probadas. Esto permite que se pueda ejecutar en el background (lo cual permite montar un *SERVER/App web*), depurar errores, entender el comportamiento del motor, extraer las reglas probadas...

	-	Logging de eventos de clases y del motor de inferencia

	-	Logging de las reglas que se piden probar junto con la conclusion (si son verdaderas o falsas)

	-	Logging debug para la traza normal. Logging info para las conclusiones de si una regla introducida es verdadera o falsa. Logging error y warning para la gestion de excepciones.

	-	Logging PONER HORA Y DIA DE STARTING PROGRAM!!

-	conclusiones_fc para guardar la traza de las pruebas que se han pedido demostrar con FC (SOLO SE VA A GUARDAR LA SENTENCIA PROBADA, *NO EL RAZONAMIENTO*)

-	Escribir los mensajes de logs de las clases y del motor de inferencia en los ficheros "sentences.py" y "driverSentences.py" correspondientes.

-	Performing de proof and subproof solo en LOG

-	BC errors solved (do not name a variable "rule")

-	Dejar basic_example fino fino.
.

.

********************** BACKLOG **********************

-	Convertir clases en BEANS, **libreria Pickle SERIALIZAR & Guardar partida!!**

-	Probar a quitar Sentences. en todas las frases importadas


-	PYKE CON PYTHON3!!! Instalar PyKE v3 en pip3

-	*PONER PRIVADOS LOS ATRIBUTOS!!* Ahora todo es público y accesible...???


.

*********** SERVER IDEA **************


BridgeXplained es un programa de enseñanza básica del Bridge.

La idea es montar un servidor básico utilizando Django (como hemos visto en la asignatura de PSI) para ilustrar la implementación real y práctica del programa.

Una opción sería que el programa estuviera en un repositorio de Github y ser un proyecto OpenSource de tal forma que el usuario se descargara el repositorio y corriera en local el programa.

Sin embargo, una verdadera implementación en la realidad sería que los usuarios se conecten a la web de BridgeXplained para realizar sus ejercicios.

Para cada usuario se lanzaría un proceso en el background del servidor donde se resuelve su ejercicio, junto con los correspondientes razonamientos. También podría consultar su fichero log para ver la traza del programa, O SE PODRÍA ESCRIBIR POR PANTALLA ESTA TRAZA DEL LOG!!!


************ ERRORES RAROS ************

NO llamar a una variable *rule* en las reglas (BC.krb) porque al traducirse las reglas en codigo Python, se sobreescribe una variable interna llamada rule...