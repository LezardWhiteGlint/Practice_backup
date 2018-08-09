import requests
from lxml import html

USERNAME = "10024"
PASSWORD = "yyy666"

LOGIN_URL = "http://acc.r2games.com/main/?r=site/login"
URL = "http://data.r2games.com/platform/?r=user%2Fpayment&m=M294&p=r2games&g=wartune&server=ALL&time_start=2017-04-29&time_end=2017-05-03&show=ByDate"

def main():
    session_requests = requests.session()

    # Get login csrf token
    #result = session_requests.get(LOGIN_URL)
    #tree = html.fromstring(result.text)
    #authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]

    # Create payload
    payload = {
        "username": USERNAME, 
        "password": PASSWORD 
        #"csrfmiddlewaretoken": authenticity_token
    }

    # Perform login
    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

    # Scrape url
    result = session_requests.get(URL, headers = dict(referer = URL))
    tree = html.fromstring(result.content)
    bucket_names = tree.xpath("//div[@class='repo-list--repo']/a/text()")

    print(bucket_names)

if __name__ == '__main__':
    main()
