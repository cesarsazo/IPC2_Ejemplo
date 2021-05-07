import re

texto = """
otroemail321@hotmail.gt
Just a young gun with the quick fuse correo1@gmail.com
I was uptight, wanna let loose
I was dreaming of bigger things
And wanna leave correo2@gmail.com my own life behind
cesar321@hotmail.com Not a yes sir, not a follower
persona3@yahoo.es
Fit the box, fit the mold persona1@yahoo.com
Have a seat in the foyer, take a number
I was lightning before the thunder correo3@gmail.com
"""

def findEmail(texto):
    pattern = re.compile('[\w]+@\S+\.\S+')
    match = re.findall(pattern, texto)
    emails = []
    for email in match:
        emails.append(email)
    return emails