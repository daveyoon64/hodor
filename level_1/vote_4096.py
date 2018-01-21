import requests
from bs4 import BeautifulSoup

# set up our payload and url 
payload = {'id': 244, 'holdthedoor': 'Submit'}
url = "http://158.69.76.135/level1.php"

# get the sites HTML
site = requests.get(url)
# scrape the site for its key
soup = BeautifulSoup(site.text, 'html.parser')
secret = soup.find('input', attrs={'name':'key'})
new_cookie = secret['value']

# create and append our header
headers = {'HoldTheDoor': new_cookie}
payload.update({'key': new_cookie})
r = requests.post(url, params=payload, headers=headers)
print(r.status_code)
