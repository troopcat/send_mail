# By troopcat 07/09/2020(DD/MM/YYYY)
# GitHub: https://github.com/troopcat
import smtplib
from email.message import EmailMessage
from imghdr import what

# img_names,file_names,to must be list for send_mail
 
def send_mail(subject:str,content:str,to:list,email_address:str,password:str,smtp_server:str,smtp_server_port:int,img_names=[],file_names=[],html_file="",encoding_type="utf8",ok_msg=False):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = email_address
    msg["To"] = ", ".join(to)
    msg.set_content(content)

    if html_file:
        with open(html_file,"r",encoding=encoding_type) as f:
            msg.add_alternative(f.read(),subtype="html")

    if img_names:
        for img_name in img_names:
            with open(img_name,"rb") as f:
                file_data = f.read()
                file_type = what(f.name)
                file_name = f.name
                msg.add_attachment(file_data,maintype="image",subtype=file_type,filename=file_name)

    if file_names:
        for file_name in file_names:
            with open(file_name,"rb") as f:
                file_data = f.read()
                file_name = f.name
                msg.add_attachment(file_data,maintype="application",subtype="octet-stream",filename=file_name)


    with smtplib.SMTP_SSL(smtp_server,smtp_server_port) as smtp:
        smtp.login(email_address,password)
        smtp.send_message(msg)
        if ok_msg:
            print("Your mail has been sent successfully.")

def send_basic_mail(subject:str,content:str,to:str,email_address:str,password:str,smtp_server:str,smtp_server_port:int,ok_msg=False):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = email_address
    msg["To"] = to
    msg.set_content(content)

    with smtplib.SMTP_SSL(smtp_server,smtp_server_port) as smtp:
        smtp.login(email_address,password)
        smtp.send_message(msg)
        if ok_msg:
            print("Your mail has been sent successfully.")



