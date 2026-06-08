# test_reader.py

from gmail_reader import *

service = authenticate_gmail()

messages = get_unread_emails(service)

for msg in messages:

    email_data = extract_email_details(
        service,
        msg['id']
    )

    print(email_data)