url = 'https://www.olx.ua/d/obyavlenie/bts-ukrndiagroproekt-arenda-ofisa-73-m-kv-na-solomenskoy-ploschadi-2-IDLRtAF.html#d87ad13fbe;promoted'
url =url.split('#')[0]
print(url)
import json
phone = b'{"data":{"phones":["063 729 7450"]}}'
phone = json.loads(phone)
print(phone['data']['phones'][0])
