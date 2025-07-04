import smtplib, ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "Nishantketu363@gmail.com"
    # This is your gmail app password
    password = "luwv qztc gdco ejlr"

    receiver = "Nishantketu363@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)