#!/usr/bin/python3
# -*- encoding: utf8 -*-

import random
import smtplib
from email.mime.text import MIMEText


COMMASPACE = ', '


# Función para enviar el correo
def send_email():
    email_from = 'remitente@example.com'
    email_to = 'destinatario_1@example.com', 'destinatario_2@example.com', 'destinatario_3@example.com'
    email_body_str = ''
    for line in email_body:
        email_body_str += line + '\n'
    mensaje = MIMEText(email_body_str)
    mensaje['From'] = email_from
    mensaje['To'] = COMMASPACE.join(email_to)
    mensaje['Subject'] = "Félixconsejo del día"
    server_smtp = smtplib.SMTP('smtp.gmail.com', 587)
    server_smtp.ehlo()
    server_smtp.starttls()
    server_smtp.ehlo()
    server_smtp.login(email_from, 'password')
    server_smtp.sendmail(email_from, email_to, mensaje.as_string())
    server_smtp.close()


felixconsejo = ['¡Ay mi Barrabás!',
                'Los cojones al suelo',
                'Me vas a comer la polla por debajo del culo sin tocarme los huevos',
                'Eres más bonica que un remolque recién pintao',
                'Muy amigo muy amigo... pero el borrico en la linde',
                'Cuando no está el gallo hasta el pollo se pone salido',
                'Para vosotros la vida',
                'Relaja la fresita princesita',
                'Cuando el tonto coge la linde, la linde acaba pero el tonto sigue',
                'En todos los pueblos hay un tonto y una cigüeña. Con todas las cigüeñas que hay en Madrid... imagínate la de tontos'
                ]

consejo_del_dia = random.choice(felixconsejo)


email_body = ['Félix dice: ' + consejo_del_dia]
send_email()