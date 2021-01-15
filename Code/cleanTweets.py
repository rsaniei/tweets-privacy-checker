import re
import string


#  These scripts receive a string(in this case a tweet) as an input and remove emojis,
#  URLs, htmls, and punctuations, respectively.

#removing the emojis
def remove_emoji(string):
    emoji_pattern = re.compile(
        "["
          u"\U0001F600-\U0001F64F"  # emoticons
          u"\U0001F300-\U0001F5FF"  # symbols & pictographs
          u"\U0001F680-\U0001F6FF"  # transport & map symbols
          u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "]+" , flags = re.UNICODE,)

    return emoji_pattern.sub(r"", string)


#removing URLs
def remove_URL(text):
    url = re.compile(r"https?://\S+|www\.\S+")
    return url.sub(r"", text)


#removing html
def remove_html(text):
    html = re.compile(r"<.*?>")
    return html.sub(r"", text)

#removing punctuations
def remove_punct(text):
    table = str.maketrans("", "", string.punctuation)
    return text.translate(table)