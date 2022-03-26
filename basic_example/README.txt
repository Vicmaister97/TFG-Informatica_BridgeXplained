Ejemplo de un programa básico con PyKE.

Ver cómo trabaja con reglas del estilo: #H(S,C)+#H(O,C)+#H(N,C)+#H(E,C)=5
    - Traducción de #H(S,C): Número de Honores en Corazones del jugador Sur
    - Traducción de la regla: La suma del número de honores en corazones de todos los jugadores debe ser 5
                              i.e: Hay 5 puntos en honores de corazones (A,K,Q,J,10)

- Posibilidad de añadir un fichero .kqb para añadir conjunto de preguntas y respuestas para mejorar el aprendizaje.

---------------------------- CORRER EL EJEMPLO ----------------------------

Terminal Linux:

python

>>> import driver

""" Usar razonamiento hacia delante (FC -- Forward Chaining) """

>>> driver.fc('rule_to_prove')
    Ejemplo concreto: >>> driver.fc('numbers.honores_corazones_new_post(S, 1)')

"""
Esto prueba con razonamiento hacia delante que el jugador Sur tiene 1 honor en corazones, algo que solo se puede concluir tras probar todas las demás reglas.

Puedes probar a demostrar cualquier otra regla definida en el fichero "fc_numbers.krb".
"""

""" Usar razonamiento hacia atrás (BC -- Backward Chaining) """

>>> driver.bc('rule_to_prove')
    Ejemplo concreto: >>> driver.bc('bc_numbers.honores_corazones_new_post(S, 1)')

"""
Esto prueba con razonamiento hacia atrás que el jugador Sur tiene 1 honor en corazones, algo que solo se puede concluir tras probar todas las demás reglas.

Puedes probar a demostrar cualquier otra regla definida en el fichero "bc_numbers.krb".
"""
