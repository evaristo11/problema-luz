import time
#se importa la biblioteca time para utilizar sus funciones


hora.inicio = int(input(" ¿ Que hora es ? (horario militar 24h)"))
#Variable de hora solo toma numeros del 1 al 24

hora.encendido = int(input(" ¿ A que hora quiere que se encienda la luz ? (horario militar 24h)"))
#variable de prendidio de luz solo toma numeros del 1 al 24

hora.apagado = int(input(" ¿ A que hora quiere que se apage la luz ? (horario militar 24h)"))
#variables de apagado de la luz solo toma numeros del 1 al 24

While true
#se crea un while de un ciclo infinito, ya que queremos un monitoreo a toda hora

	if hora.inicio < hora.encendido and hora.inicio >= hora.apagado
		print("0")
	else
		print("1")
	end
#un if que imprime la senal de encendido o apagado dependiendo de la hora

	time.sleep(3600)
#causa un paro en el ciclo por 3600 segundos, o una hora. La comprobacion se realiza cada hora
	if hora.inicio == 24
		hora.inicio = 0
	end
#se crea un if que resetea la hora a 1 cuando ya se cumplio el ciclo de 24 horas

	hora.inicio  = hora.inicio + 1

end
