#!/usr/bin/env python

import tomli

from utils.jobs import Jobs
from utils.UC import UC


def load_settings():
    with open('settings/settings.toml', 'r') as f:
        settings = tomli.loads(f.read())
        return settings


def main():
    settings = load_settings()

    jobs = Jobs(
        settings['api_key'],
        settings['job_keywords'],
        settings['dates'],
        settings['location']
    )

    uc = UC(
        settings['cookies']
    )

    prepared_jobs = jobs.prepare(settings['jobs']['jobs_per_day'])
    uc.post(prepared_jobs)


if __name__ == '__main__':
    main()
