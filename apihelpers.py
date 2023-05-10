
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
    smtp_server = "smtp.office365.com"
    port = 587  # For starttls
    sender_email = "info@restopainphysio.ca"
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
            Thanks for registering 
        </body>
        </html>
        """
    email_part = MIMEText(html, "html")
    message.attach(email_part)

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        # TODO: Send email here
    except Exception as e:
        # Print any error messages to stdout
        return str(e)
    finally:
        server.quit() 