import requests

votes = 0
while votes <= 20:
    r = requests.post('http://158.69.76.135/level0.php', data = {'id': 244, 'holdthedoor': 'Submit+Query'})
    votes += 1
print(r.status_code)
