<h1>felixconsejo</h1>
<h3>Automtiza el envío de frases populares (o lo que quieras) con este script</h3>
*Escrito en Python3.6*

Con **felixconsejo** puedes tener una lista de frases populares y enviarla por correo a una lista de destinatarios.

<h3>Sugerencias</h3>

Si quieres introducir más de un destinatario, recuerda usar ```COMMASPACE = ', '``` para que no de error con tuplas de destinatarios.
Si solo lo vas a enviar a un destinatario, puedes dejar comentado esa línea. 
¡Sientete libre de añadir las frases que quieras!

Usa ```crontab - e``` en Linux para programar la ejecución automática del script:

```
un@muggle:~/cron$ crontab -e
# Edit this file to introduce tasks to be run by cron.

01 09 * * 1-5 /usr/bin/python3.6 /home/usuario/directorio/felixconsejo.sh
```
