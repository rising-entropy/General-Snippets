import requests
from bs4 import BeautifulSoup
import re


resp = requests.get("https://adoption.com/baby-names/origin/russian")  # + page 

# <td id="c1" class="c1"><a href="/meaning-of-aamish.aspx">Aamish (ఆమిష)</a></td>

soup = BeautifulSoup(resp.text, 'html.parser')
allTDTags = list(soup.find_all('tr'))

ans = []

for theTag in allTDTags:
    theTag = str(theTag)
    soup2 = BeautifulSoup(theTag, 'html.parser')
    a = []
    try:
        a = list(soup2.find_all('td', {"class": "text-wrap"}))[0]
    except:
        pass
    if a != []:
        match = re.findall(r"\">.*<\/", theTag)[0]
        match = match.split(">")[1].split("<")[0]
        ans.append(match)

print(ans)
