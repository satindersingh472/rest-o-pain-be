
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import dbcreds



# the following function will over write the new data that has passed by user with the original data in the request
def add_for_patch(sent_data,required_args,original_data):
    for data in required_args:
        if(sent_data.get(data) != None):
            original_data[data] = sent_data[data]
    return original_data
    

# will verifiy end points arguments for presence
# if necessary arguments not sent then remind the user to send
def verify_endpoints_info(sent_data,required_args):
    for data in required_args:
        if(sent_data.get(data) == None):
            return f'The {data} argument is required'

def send_email(email):
    smtp_server = "smtp.gmail.com"
    port = 465  # For smtp-ssl
    sender_email = "restopainphysiotherapy@gmail.com"
    receiver_email = f"{email}"
    password = dbcreds.email_password
    # Create a secure SSL context
    context = ssl.create_default_context()
    message = MIMEMultipart("alternative")
    message["subject"] = "Thank you for registration"
    message["from"] = f"Rest-O-Pain {sender_email}"
    message["to"] = receiver_email

    html = """\
        <html>
        <body>
            Thanks for registering <br>
            this email is for test purpose only. <br>
            Please do not try to reply on this email. <br>
            Thanks
        </body>
        </html>
        """
    email_part = MIMEText(html, "html")
    message.attach(email_part)

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP_SSL(smtp_server,port,context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        # TODO: Send email here
    except Exception as e:
        # Print any error messages to stdout
        return str(e)
    finally:
        server.quit() 