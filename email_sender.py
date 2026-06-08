import smtplib
from email.mime.text import MIMEText


def send_digest_email(
    sender_email,
    app_password,
    receiver_email,
    digest
):

    msg = MIMEText(digest)

    msg["Subject"] = "Daily Email Digest"

    msg["From"] = sender_email

    msg["To"] = receiver_email

    with smtplib.SMTP(
        "smtp.gmail.com",
        587
    ) as server:

        server.starttls()

        server.login(
            sender_email,
            app_password
        )

        server.send_message(msg)