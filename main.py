import requests

headers = {
    'authority': 'answergarden.ch',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'origin': 'https://answergarden.ch',
    'content-type': 'application/x-www-form-urlencoded',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-gpc': '1',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://answergarden.ch/1',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}

def one():
    data = {
        'answer': 'Yourmessagehere',
        'action': 'websubmit',
        'id': '1',
        'output': 'html',
        'submit.x': '1111',
        'submit.y': '313'
    }
    response = requests.post('https://answergarden.ch/1', headers=headers, data=data)
    
def two():
    data = {
        'answer': 'yourmessagehere',
        'action': 'websubmit',
        'id': '1',
        'output': 'html',
        'submit.x': '1111',
        'submit.y': '313'
    }
    response = requests.post('https://answergarden.ch/1', headers=headers, data=data)

while True:
    one()
    two()
