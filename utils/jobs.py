import requests
import sys

from itertools import cycle
from random import sample

from utils.date import parse_dates
from utils.templates import create_templates

SEARCH_BASE_URL = 'https://www.reed.co.uk/api/1.0/search'


class Jobs:
    def __init__(self, api_key, keywords, dates, location):
        self.api_key = api_key
        self.keywords = keywords
        self.dates = parse_dates(dates)
        self.results = self.job_search(location)
        self.jobs = self.parse_jobs()

    def job_search(self, location):
        results = {}
        for keyword in self.keywords:
            url = SEARCH_BASE_URL + (
                f'?keywords={keyword}'
                f'&locationName={location["city"]}'
                f'&distanceFromLocation={location["mile_radius"]}'
            )
            results[keyword] = requests.get(url, auth=(self.api_key, '')).json()['results']
        return results

    def parse_jobs(self):
        jobs = set()
        for keyword in self.results:
            for listing in self.results[keyword]:
                jobs.add((listing['employerName'], listing['jobTitle']))
        return list(jobs)

    def prepare(self, jobs_per_day):
        total_jobs = jobs_per_day * len(self.dates)
        if total_jobs > len(self.jobs):
            print('Not enough jobs found. Either add more keywords or reduce jobs per day')
            sys.exit()
        notes = create_templates(total_jobs)
        return sorted(
            list(zip(sample(self.jobs, total_jobs), cycle(self.dates), notes)),
            key=lambda x: x[1]
        )
