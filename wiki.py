import requests
from bs4 import BeautifulSoup

req = requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)')
soup = BeautifulSoup(req.text, "lxml")

soup.h1
# <h1 class="firstHeading" id="firstHeading" lang="en">Python (programming language)</h1>

soup.h1.string
# 'Python (programming language)'

soup.h1['class']
# ['firstHeading']

soup.h1['id']
# 'firstHeading'

soup.h1.attrs
# {'class': ['firstHeading'], 'id': 'firstHeading', 'lang': 'en'}

soup.h1['class'] = 'firstHeading, mainHeading'
soup.h1.string.replace_with("Python - Programming Language")
del soup.h1['lang']
del soup.h1['id']

soup.h1
# <h1 class="firstHeading, mainHeading">Python - Programming Language</h1>

soup.h1
# <h1 class="firstHeading" id="firstHeading" lang="en">Python (programming language)</h1>

soup.h1.string
# 'Python (programming language)'

soup.h1['class']
# ['firstHeading']

soup.h1['id']
# 'firstHeading'

soup.h1.attrs
# {'class': ['firstHeading'], 'id': 'firstHeading', 'lang': 'en'}

soup.h1['class'] = 'firstHeading, mainHeading'
soup.h1.string.replace_with("Python - Programming Language")
del soup.h1['lang']
del soup.h1['id']

soup.h1
# <h1 class="firstHeading, mainHeading">Python - Programming Language</h1>