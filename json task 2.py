import urllib.request
import urllib.parse
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    params = dict()
    params['q'] = address.strip()
    params['key'] = 42

    url = serviceurl + urllib.parse.urlencode(params)
    print('Retrieving', url)

    try:
        uh = urllib.request.urlopen(url, context=ctx)
        data = uh.read().decode()
        print(f'Retrieved {len(data)} characters')
        js = json.loads(data)
    except Exception as e:
        print('Error retrieving or parsing data:', e)
        continue
    if 'features' in js and len(js['features']) > 0:
        properties = js['features'][0]['properties']
        if 'plus_code' in properties:
            print('Plus code:', properties['plus_code'])
        else:
            print('plus_code not found in properties')
    else:
        print('No features found or failed to download data')
