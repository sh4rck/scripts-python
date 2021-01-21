
import requests
import re
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

print('Automação iniciada...')
time.sleep(2)
print('')

print('Acessando site INDEED vagas de emprego...')
time.sleep(3)
print('')



print('Iniciando captura de emails...')
print('')
print('')

x = 0

with open('lista-de-emails.txt','w') as arquivo:
    
    for i in range(0,51):
        url = (f"https://br.indeed.com/empregos?q=E+Mail+Para+Curriculo&l=Nova+Odessa,+SP&fromage=last&start={x}")

        html_page = requests.get(url)
        html_source = html_page.text
        
        emails = re.findall('\w+@\w+\.{1}\w+', html_source)

        for email in emails:
            if email == '0252655a41544fd28ae41f8b8ff36917@sentry.indeed':
                pass
            else:
                
                print(email)
                print(email,file=arquivo)

        x = x+10
        
print('')
print('')
print('Lista de emails capturada e salva...')
time.sleep(2)
print('')

print('Acessando a lista de emails...')
time.sleep(2)
print('')

#NÃO ESQUEÇA DE ATIVAR 'AUTORIZAR PROGRAMAS MENOS SEGUROS' NA SUA CONTA GMAIL!
#O GMAIL SÓ AUTORIZA 500 EMAILS POR DIA...NÃO ABUSE!

lista = []

with open('lista-de-emails.txt','r') as arquivo:
    for linha in arquivo:
        lista.append(linha)

with open('curriculo.txt','r',encoding='utf-8') as arquivo2:
    curriculo = arquivo2.read()


print('Iniciando o envio de emails para empresas...')
time.sleep(2)
print('')
print('.')
print('.')
print('.')
print('')

for i in range(1, 499):	
    fromaddr = "seuemail@gmail.com"
    toaddr = lista[i]
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "CURRICULO"

    body = curriculo

    msg.attach(MIMEText(body, 'plain'))

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, "senha-do-seu-gmail")
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()

    print(f'Email {i}/499 enviado com sucesso!')
    #time.sleep(30)

            
print('')
print('.')
print('.')
print('.')
print('')
print('Automação concluida com sucesso!')
