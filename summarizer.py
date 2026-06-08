from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer


def summarize_email(text):

    parser = PlaintextParser.from_string(
        text,
        Tokenizer("english")
    )

    summarizer = LsaSummarizer()

    summary = summarizer(
        parser.document,
        3
    )

    result = ""

    for sentence in summary:
        result += f"• {sentence}\n"

    return result




#Summarizer.py uisng the OpenAi API..but the problem arises with the exhausted credits 

# from openai import OpenAI
# from dotenv import load_dotenv
# import os

# load_dotenv()

# client = OpenAI(
#     api_key=os.getenv(
#         "OPENAI_API_KEY"
#     )
# )

# def summarize_email(body):

#     response = client.chat.completions.create(

#         model="gpt-4.1-mini",

#         messages=[

#             {
#                 "role":"system",
#                 "content":"Summarize emails in 3 bullet points."
#             },

#             {
#                 "role":"user",
#                 "content":body
#             }

#         ]
#     )

#     return response.choices[0].message.content


# if __name__ == "__main__":

#     sample_email = """
#     Dear Team,

#     We have scheduled a client meeting tomorrow at 10 AM.

#     Please prepare the sales report and project updates.

#     Thanks
#     """

#     print(
#         summarize_email(
#             sample_email
#         )
#     )



if __name__ == "__main__":

    sample_text = """
    Dear Team,

    The meeting is scheduled tomorrow at 10 AM.

    Please prepare project updates and sales reports.

    Thanks.
    """

    print(summarize_email(sample_text))