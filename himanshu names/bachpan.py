import requests
from bs4 import BeautifulSoup
import re


resp = requests.get("https://www.bachpan.com/telugu-boy-names-e.aspx")  # + page 

# <td id="c1" class="c1"><a href="/meaning-of-aamish.aspx">Aamish (ఆమిష)</a></td>

soup = BeautifulSoup(resp.text, 'html.parser')
allTDTags = soup.find_all('td', {"id": "c1", "class": "c1"})

allTDTags = list(allTDTags)

theNames = []

for td in allTDTags:
    theTag = str(td)
    match = re.findall(r"aspx\">.*<\/a", theTag)[0]
    match = match.split(">")[1].split()[0]
    theNames.append(match)

def isOneSyllable(name):
    c=0
    for character in name:
        character = character.lower()
        if character == "a" or character == "e" or character == "i" or character == "o" or character == "u":
            c += 1
    if c == 1:
        return True
    return False

finalNames = []
for name in theNames:
    if isOneSyllable(name):
        finalNames.append(name)

print(finalNames)