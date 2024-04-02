import pytest
from zeep import Settings, Client
import yaml

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    wsdl_url = data['wsdl_url']

def check_text(word):
    settings = Settings(strict=False)
    client = Client(wsdl_url, settings=settings)
    result = client.service.checkText(word)[0]['s']
    return result

#print(check_text('королвство'))

'''
word = 'Королетво'
settings = Settings(strict=False)
client = Client(wsdl_url, settings=settings)
result = client.service.checkText(word)[0]['s']

print(result)
'''