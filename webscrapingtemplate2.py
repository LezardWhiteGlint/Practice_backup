import requests
from lxml import html


# Fill in your details here to be posted to the login form.
payload = {
    "email":'ifuleu66@hotmail.com',
    "pass":'yyyy6666',
    "lsd":'AVrOgnbk',
    "timezone":'-480',
    "lgndim":'eyJ3IjoxOTIwLCJoIjoxMDgwLCJhdyI6MTkyMCwiYWgiOjEwMDMsImMiOjI0fQ==',
    "lgnrnd":'194901_3wO-',
    "lgnjs":'1495507741',
    "legacy_return":'0',
    'trynum':'1--------'
    }



URL = "https://www.facebook.com/login"

# Use 'with' to ensure the session context is closed after use.
with requests.session() as s:
    p = s.post(URL,data=payload)
    r = s.get("http://data.r2games.com/platform/?r=user%2Fpayment&m=M294&p=r2games&g=wartune&server=ALL&time_start=2017-04-29&time_end=2017-05-03&show=ByDate")
    tree = html.fromstring(r.content)
    recharge = tree.xpath('//td[@class="total 2"]/text()')
    print(recharge)
