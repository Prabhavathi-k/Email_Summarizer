print("FILE LOADED")
import logging
import os

from dotenv import load_dotenv

from gmail_reader import (
    authenticate_gmail,
    get_unread_emails,
    extract_email_details
)

from cleaner import clean_email
from summarizer import summarize_email
from digest_generator import create_digest
from email_sender import send_digest_email


print("FILE LOADED")


# Logging Configuration
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)

print("LOGGING CONFIGURED")

# Load Environment Variables
load_dotenv()

sender_email = os.getenv("SENDER_EMAIL")
app_password = os.getenv("APP_PASSWORD")
receiver_email = os.getenv("RECEIVER_EMAIL")


def run_email_pipeline():

    try:

        print("=" * 50)
        print("Starting Email Summarizer Pipeline...")
        print("=" * 50)

        logging.info("Pipeline Started")

        print("STEP 1")
        service = authenticate_gmail()

        print("STEP 2")
        messages = get_unread_emails(service)

        print("STEP 3")
        print(f"Found {len(messages)} unread emails")

        logging.info(
            f"Found {len(messages)} unread emails"
        )

        if not messages:

            print("No unread emails found.")

            logging.info(
                "No unread emails found"
            )

            return

        email_summaries = []

        for msg in messages:

            try:

                email_data = extract_email_details(
                    service,
                    msg["id"]
                )

                cleaned_body = clean_email(
                    email_data["body"]
                )

                summary = summarize_email(
                    cleaned_body
                )

                email_data["summary"] = summary

                email_summaries.append(
                    email_data
                )

                print(
                    f"Processed: {email_data['subject']}"
                )

                logging.info(
                    f"Processed Email: {email_data['subject']}"
                )

            except Exception as e:

                print(
                    f"Error processing email {msg['id']}: {e}"
                )

                logging.error(
                    f"Error processing email {msg['id']}: {e}"
                )

        if not email_summaries:

            print(
                "No summaries generated. Skipping email send."
            )

            logging.warning(
                "No summaries generated. Email not sent."
            )

            return

        digest = create_digest(
            email_summaries
        )

        print("\nDaily Digest Generated\n")

        logging.info(
            "Daily Digest Generated"
        )

        print(digest)

        send_digest_email(
            sender_email=sender_email,
            app_password=app_password,
            receiver_email=receiver_email,
            digest=digest
        )

        print("\nDigest Sent Successfully")

        logging.info(
            "Digest Sent Successfully"
        )

        print("=" * 50)

    except Exception as e:

        logging.exception(
            f"Pipeline Failed: {e}"
        )

        print(
            f"Pipeline Failed: {e}"
        )


if __name__ == "__main__":

    logging.info(
        "Application Started"
    )

    run_email_pipeline()