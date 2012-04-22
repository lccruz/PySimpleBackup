# -*- coding: utf-8 -*-
#
# Copyright (c) 2012 by Luciano Camargo Cruz <luciano@lccruz.net>
#
# GNU General Public License (GPL)
#

import os
import socket
import commands
import smtplib
from settings import *

##########DEFS##########
def write_log(msg):
    """Escreve no arquivo de log"""
    log = open(LOG_PATH,'a')
    log.write(msg)
    log.close()

def send_mail(parTitulo, parMenssagem):
    """Envia email """
    titulo = "%s - %s" % (socket.gethostname(), parTitulo)
    menssagem = """From: %s
Mime-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Subject: %s

%s""" % (EMAIL_FROM, titulo, parMenssagem)

    server = smtplib.SMTP(EMAIL_SMTP)
    try:
        server.starttls()
        server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
        server.sendmail(EMAIL_FROM, EMAIL_TO, menssagem)
        server.quit()
        write_log("-Email enviado com sucesso\n")
    except Exception as (errno, strerror):
        write_log(strerror)
        server.quit()

##########SCRIPT##########
write_log("Script iniciado %s\n" % DATE_TIME_ATUAL.strftime("%d/%m/%Y %H:%M:%S"))

#Cria o arquivo tar
cmd = "tar cvfzp %s %s" % (NOME_ARQUIVO, BACKUP_PATHS)
retornoTar = os.system(cmd)
if not retornoTar:
    msgTar = "-Arquivo %s criado com sucesso\n" % (NOME_ARQUIVO)
else:
    msgTar = "-ERRO ao criar o arquivo %s\n" % (NOME_ARQUIVO)
    ERRO = True
EMAIL_MENSSAGEM += msgTar
write_log(msgTar)

#Move o arquivo tar para a pasta PATH_MV_BACKUP
cmd = "mv %s %s" % (NOME_ARQUIVO, PATH_MV_BACKUP)
retornoMv = os.system(cmd)
if not retornoMv:
    msgMv = "-Arquivo %s movido com sucesso para pasta %s\n" % (NOME_ARQUIVO, PATH_MV_BACKUP)
else:
    msgMv = "-ERRO ao mover  o arquivo %s\n" % (NOME_ARQUIVO)
    ERRO = True
EMAIL_MENSSAGEM += msgMv
write_log(msgMv)

#Envia arquivo para o servidor remoto
if ENVIAR_SERVIDOR_REMOTO:
    cmd = "scp -P %s %s/%s %s:%s" % (SERVIDOR_PORT, PATH_MV_BACKUP, NOME_ARQUIVO, SERVIDOR_REMOTO, SERVIDOR_PATH)
    retornoScp = os.system(cmd)
    if not retornoScp:
        msgScp = "-Arquivo %s movido para servidor remoto %s com sucesso para pasta %s\n" % (NOME_ARQUIVO, SERVIDOR_REMOTO, SERVIDOR_PATH)
    else:
        msgScp = "-ERRO ao mover arquivo %s para servidor remoto %s\n" % (NOME_ARQUIVO, SERVIDOR_REMOTO)
        ERRO = True
    EMAIL_MENSSAGEM += msgScp
    write_log(msgScp)
else:
    sizePathBackup = int(commands.getstatusoutput("du -sb %s" % (PATH_MV_BACKUP))[1].split('\t')[0])
    if sizePathBackup > ALERTA:
        msgAlert = "-PROBLEMA ESPACO CRITICO DA PASTA %s \n" % (PATH_MV_BACKUP)
        send_mail(msgAlert, "Tamanho da pasta em Bytes = %s" % (sizePathBackup))
        write_log(msgAlert)

#Exclui copia local
if EXCLUIR_BACKUP_LOCAL:
    cmd = "rm %s/%s" % (PATH_MV_BACKUP, NOME_ARQUIVO)
    retornoRm = os.system(cmd)
    if not retornoMv:
        msgRm = "-Arquivo %s removido com sucesso\n" % (NOME_ARQUIVO)
    else:
        msgRm = "-ERRO ao remover arquivo %s\n" % (NOME_ARQUIVO)
        ERRO = True
    EMAIL_MENSSAGEM += msgRm
    write_log(msgRm)

#Chama def que envia email e testa ERRO para modificar o titulo
if SEND_MAIL:
    titulo = ''
    if ERRO:
        titulo += "Backup ERRO"
    else:
        titulo += "Backup OK"
    send_mail(titulo, EMAIL_MENSSAGEM)

write_log("Script Finalizado %s\n" % datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
