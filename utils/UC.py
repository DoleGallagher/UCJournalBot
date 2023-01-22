import sys

from lxml import html
from requests import Session

UC_BASE_URL = 'https://www.universal-credit.service.gov.uk'


class UC:
    def __init__(self, cookies):
        self.cookies = cookies
        self.session = self.load_session()
        self.csrf_token = self.get_csrf_token()

    def get_csrf_token(self):
        last_entry_url = self.last_entry_url()
        r = self.session.get(last_entry_url)
        doc = html.fromstring(r.content.decode('utf-8'))
        hidden_input = doc.xpath('//input[@type="hidden"]')[0]
        return hidden_input.get('value')

    def last_entry_url(self):
        r = self.session.get(UC_BASE_URL + '/work-search')
        session_token = self.session.cookies.get('sessionId', domain='www.universal-credit.service.gov.uk')
        if session_token == 'expired':
            print('Invalid session cookies')
            sys.exit()
        doc = html.fromstring(r.content)
        link = doc.xpath('//a[@class="job-list__item-link"]')[0]
        return UC_BASE_URL + link.attrib['href']

    def load_session(self):
        session = Session()
        session.cookies.update(self.cookies)
        return session

    def post(self, jobs):
        for job in jobs:
            data = {
                "csrfToken": self.csrf_token,
                "jobTitle": job[0][1],
                "employer": job[0][0],
                "jobStatus": "APPLIED",
                "applicationDate.day": job[1].day,
                "applicationDate.month": job[1].month,
                "applicationDate.year": job[1].year,
                "notes":  job[2],
                "submit": "Save"
            }
            self.session.post(UC_BASE_URL + ':443/work-search/job', data=data)
