import re
from bs4 import BeautifulSoup


def clean_email(text):

    soup = BeautifulSoup(
        text,
        "html.parser"
    )

    text = soup.get_text()

    text = re.sub(
        r'\s+',
        ' ',
        text
    )

    return text.strip()