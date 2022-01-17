import smtplib
import os
from datetime import datetime


## Varible read logs file 

myhost = os.uname()[1]
fecha = datetime.today().strftime('%Y%m%d')
fecha2= datetime.today().strftime('%Y-%m-%d')
file = f'''dato_{fecha}.log'''

sentFront = f'''Asunto {myhost}'''
to = 'Email of Destination'

mensaje = f'''{myhost}<br/> <br/> 
body of email
'''

## reading file and adding to body email
file = open(file)
for line in file:
    mensaje += line + '<br/>'

user = 'User or Email who sent Email'

asunto = f'''Asunto {myhost}'''


email = '''From: %s 
To: %s 
MIME-Version: 1.0 
Content-type: text/html 
Subject: %s 

%s
''' % (sentFront, to, asunto, mensaje) 
try: 
    smtp = smtplib.SMTP('Server SMTP DOMAIN', PORT) 
    smtp.sendmail(user, to, email)
    smtp.close()
    
except: 
    
    print ('''Error: el correo no pudo enviarse.''')