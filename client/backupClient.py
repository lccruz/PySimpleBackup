# -*- coding: utf-8 -*-
#
# Copyright (c) 2012 by Luciano Camargo Cruz <luciano@lccruz.net>
#
# GNU General Public License (GPL)
#

import os
import glob
import socket
import commands
import smtplib
import datetime
from settingsClient import *

##########DEFS##########
def send_mail(parTitulo, parMenssagem):
    """Envia email """
    titulo = "%s - %s" % (socket.gethostname(), parTitulo)
    menssagem = """From: %s
Mime-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Subject: %s

%s""" % (EMAIL_FROM, titulo, parMenssagem)

    server = smtplib.SMTP(EMAIL_SMTP)
    server.starttls()
    server.login(EMAIL_FROM, EMAIL_PASSWORD)
    server.sendmail(EMAIL_FROM, EMAIL_TO, menssagem)
    server.quit()


##########SCRIPT##########
#Move o arquivo tar para a pasta referente ao ano_mes
listArquivos = glob.glob('%s/*.tar.gz' % (PATH_BACKUP))

for arquivo in listArquivos:
    mtime = os.path.getmtime(arquivo)
    data = datetime.datetime.fromtimestamp(mtime)
    path_name = "%s_%s" % (data.year,data.month)
    path_month = "%s/%s" % (PATH_BACKUP, path_name)
    if not os.path.exists(path_month):
        os.mkdir(path_month)

    cmd = "mv %s %s" % (arquivo, path_month)
    retornoMv = os.system(cmd)
    if retornoMv:
        msgMv = "-ERRO ao mover o arquivo %s\n" % (arquivo)
        send_mail("ERRO", msgMv)

#Testa tamanho da pasta
sizePathBackup = int(commands.getstatusoutput("du -sb %s" % (PATH_BACKUP))[1].split('\t')[0])
if sizePathBackup > ALERTA:
    msgAlert = "-PROBLEMA ESPACO CRITICO DA PASTA %s \n" % (PATH_BACKUP)
    send_mail(msgAlert, "Tamanho da pasta em Bytes = %s" % (sizePathBackup))
