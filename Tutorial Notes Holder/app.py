import smtplib
from config import EMAIL_ADDRESS, PASSWORD
from email.message import EmailMessage

with open('message.html', 'r') as file:
    message_content = file.read()

addresses_to_pitch = ['daxevol413@liaphoto.com']

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, PASSWORD)

    for address in addresses_to_pitch:
        msg = EmailMessage()
        msg['Subject'] = 'I\'ll build you a spectacular personal website'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = address
        msg.add_header('Content-Type','text/html')
        msg.set_payload(message_content)

        smtp.send_message(msg)
