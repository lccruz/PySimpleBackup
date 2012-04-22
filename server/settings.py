#-*- coding:utf-8 -*-
#
# Copyright (c) 2012 by Luciano Camargo Cruz <luciano@lccruz.net>
#
# GNU General Public License (GPL)
#

import datetime

#ALTERAR
#Diretorios e arquivos que serao incluidos no backup
BACKUP_PATHS = "/home/zope/plone/zinstance/buildout.cfg\
                /home/zope/plone/zinstance/versions.cfg\
                /home/zope/plone/zinstance/var/filestorage/Data.fs\
                /home/zope/plone/zinstance/var/blobstorage"

#Pasta que sera movido o .tar
PATH_MV_BACKUP = 'backups'

#Dados servidor remoto
SERVIDOR_REMOTO = 'HOST'
SERVIDOR_PATH = 'backups'
SERVIDOR_PORT = '22'

#Setar como False para nao enviar arquivos para o servidor remoto
ENVIAR_SERVIDOR_REMOTO = True

#Setar como True para apagar o backupt local gerado no dia
EXCLUIR_BACKUP_LOCAL = False

#Configuracao para envio de email
EMAIL_FROM = "alerta@gmail.com"
EMAIL_TO = ["to@to.com.br", "to@to.net"]
EMAIL_USERNAME = 'alerta@gmail.com'
EMAIL_PASSWORD = 'XXX'
EMAIL_SMTP = 'smtp.gmail.com:587'

#Setar como False para nao enviar email
SEND_MAIL = True

#Envia um email alertando que o estado da pasta de backup esta critico
#Somente funciona se o ENVIAR_SERVIDOR_REMOTO = False
#Tamanho em bytes
ALERTA = 10000000000 #10GB

######################### NAO ALTERAR #########################
#Arquivo de log
LOG_PATH = "%s/backup.log" % (PATH_MV_BACKUP)

#Data e hora atual
DATE_TIME_ATUAL = datetime.datetime.now()

#Nome no arquivo de backup
NOME_ARQUIVO = "backup_%s.tar.gz" % (DATE_TIME_ATUAL.strftime("%d_%m_%Y_%H_%M_%S"))

#Utilizado para informar se tem alguma falha no processo
ERRO = False

#Utilizado para concatenar as mensagens
EMAIL_MENSSAGEM = ''
