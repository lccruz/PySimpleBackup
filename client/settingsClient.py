#-*- coding:utf-8 -*-
#
# Copyright (c) 2012 by Luciano Camargo Cruz <luciano@lccruz.net>
#
# GNU General Public License (GPL)
#

#ALTERAR
#Pasta dos backups
PATH_BACKUP = 'backups'

#Configuracao para envio de email
EMAIL_FROM = "alerta@gmail.com"
EMAIL_TO = ["to@to.com.br", "to@to.net"]
EMAIL_USERNAME = 'alerta@gmail.com'
EMAIL_PASSWORD = 'XXX'
EMAIL_SMTP = 'smtp.gmail.com:587'

#Envia um email alertando que o estado da pasta de backup esta critico
#Tamanho em bytes
ALERTA = 10000000000 #10GB
