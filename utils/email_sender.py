import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import dns.resolver


def check_mx_records(email):
    try:
        # Extract domain from email
        domain = email.split("@")[-1]

        # Query the MX records
        mx_records = dns.resolver.resolve(domain, "MX")

        # Print MX records (optional)
        mx_list = [record.exchange.to_text() for record in mx_records]
        return f"Valid MX records found: {mx_list}"

    except Exception as e:
        return f"Error checking MX records: {e}"


EMAIL_USER = "ramsoft8484@gmail.com"

mxs = check_mx_records("bishal.chaulagain@softbenz.com.np")

print(mxs)

EMAIL_PASS = "bttzkdlfhqhggwms"
# Email sender and receiver
sender_email = EMAIL_USER
receiver_email = "1@gmail.com"
password = EMAIL_PASS  # Use an App Password if using Gmail

# Create the email
subject = "Test Email from Python"
body = "Hello, this is a test email sent from Python."


import smtplib


def verify_email(email):
    domain = email.split("@")[-1]
    message = ""
    try:
        # Get the mail server (MX record)

        mx_records = dns.resolver.resolve(domain, "MX")
        for i in mx_records:
            mx_record = i.exchange.to_text()
            print(mx_record, ">>>>><<<")
            try:
                # Connect to the mail server
                server = smtplib.SMTP(mx_record)
                server.set_debuglevel(0)  # Set to 1 for debugging output
                server.helo()
                server.mail(EMAIL_USER)  # Replace with a real sender
                code, message = server.rcpt(email)
                server.quit()

                # 250 means the email exists, 550 means it does not
                if code == 250:
                    message = f"✅ Email exists: {email}"
                elif code == 550:
                    message = f"❌ Email does not exist: {email}"
                else:
                    message = f"⚠️ Unknown response ({code}): {message.decode()}"
                break
            except Exception as e:
                print(e.args)
        return message
    except Exception as e:
        return f"Error checking email: {e}"


# Example usage
# print(verify_email("bishal.chaulagain@softbenz.com.np"))
print(verify_email("softbenzsagarsedai@gmail.com"))

"""
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject
msg.attach(MIMEText(body, "plain"))

# Connect to Gmail's SMTP server and send email
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Secure the connection
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
"""
