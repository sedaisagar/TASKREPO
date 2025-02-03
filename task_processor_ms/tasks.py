import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from celery import shared_task
from django.apps import apps
import dns.resolver
from decouple import config

# Read email_user and email_pass from environment variables
EMAIL_USER = config("EMAIL_USER", "")
EMAIL_PASS = config("EMAIL_PASS", "")


def check_mx_records(email):
    try:
        # Extract domain from email
        domain = email.split("@")[-1]

        # Query the MX records
        mx_records = dns.resolver.resolve(domain, "MX")

        # Print MX records (optional)
        mx_list = [record.exchange.to_text() for record in mx_records]
        return len(mx_list)

    except Exception as e:
        return 0


def email_send(email_payload):

    msg = MIMEMultipart()
    msg["From"] = EMAIL_USER

    msg["To"] = email_payload["email"]
    msg["Subject"] = email_payload["subject"]

    msg.attach(MIMEText(email_payload["body"], "plain"))

    # Connect to Gmail's SMTP server and send email
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_USER, EMAIL_PASS)
            server.sendmail(EMAIL_USER, email_payload["email"], msg.as_string())
        print("Email sent successfully!")
        return "completed"
    except Exception as e:
        print(f"Error: {e}")
        return "failed"


from django.db import transaction
import time, datetime


@shared_task
def email_sender(email_payload: dict, *args, **kwargs):
    # Row level lock
    with transaction.atomic():
        pk = kwargs.get("pk")
        # Before any task execution(s), set task status to processing
        Tasks = apps.get_model("tasks", "Tasks")
        task = Tasks.objects.get(pk=pk)
        task.status = "processing"
        task.save()

        # check if any mx records exists for email domain
        email_exists = check_mx_records(email_payload.get("email"))

        if email_exists:
            # If email exists then send email and get status completed or failed
            status = email_send(email_payload)
        else:
            status = "failed"

        # Toggle task status with the email sent status
        task.status = status
        task.save()

        print(task.status, f"Task saved with status {status}")
