def create_digest(email_summaries):

    digest = ""

    for index, email in enumerate(
        email_summaries,
        start=1
    ):

        digest += f"""
Email {index}

Sender:
{email['sender']}

Subject:
{email['subject']}

Summary:
{email['summary']}

{'='*50}

"""
    return digest
